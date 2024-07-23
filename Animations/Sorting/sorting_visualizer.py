import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
import random
import time
import threading
from algorithms import (
    BubbleSort,
    SelectionSort,
    InsertionSort,
    MergeSort,
    QuickSort,
    HeapSort,
)


class SortingApp:
    def __init__(self, root):
        themeList = [
            "cosmo",
            "cyborg",
            "darkly",
            "flatly",
            "journal",
            "litera",
            "lumen",
            "minty",
            "morph",
            "pulse",
            "sandstone",
            "simplex",
            "solar",
            "superhero",
            "united",
            "vapor",
            "yeti",
        ]
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")

        self.current_theme = "cosmo"  # Default theme from ttkbootstrap
        self.style = Style(theme=self.current_theme)
        self.root.style = self.style

        self.root.configure(bg=self.style.colors.bg)  # Set window background color

        # Calculate 80% of screen width and set fixed size for the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = int(screen_width * 0.8)
        height = 600  # Fixed height
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.array = []
        self.original_array = []  # Store original generated array
        self.speed = 0.1  # Adjust sorting speed as needed
        self.sorting_algorithm = None
        self.sorting_thread = None
        self.start_time = None  # Track start time for sorting

        # Frame for vertical buttons on the left
        self.buttons_frame = tk.Frame(self.root, bg=self.style.colors.bg)
        self.buttons_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.num_elements_label = tk.Label(
            self.buttons_frame, text="Number of Elements:"
        )
        self.num_elements_label.pack(pady=5)
        self.num_elements_entry = tk.Entry(self.buttons_frame)
        self.num_elements_entry.pack(pady=5)

        self.generate_button = tk.Button(
            self.buttons_frame,
            text="Generate Array",
            command=self.generate_array_with_elements,
        )
        self.generate_button.pack(pady=5, fill=tk.X, expand=True)

        # Speed Slider
        self.speed_label = tk.Label(self.buttons_frame, text="Speed (s):")
        self.speed_label.pack(pady=5)

        # Speed Slider value label
        self.speed_value_label = tk.Label(self.buttons_frame, text="0.1")
        self.speed_value_label.pack(pady=5)

        self.speed_slider = tk.Scale(
            self.buttons_frame,
            from_=0.01,
            to=1.0,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            command=self.update_speed,
        )
        self.speed_slider.set(0.1)  # Default speed
        self.speed_slider.pack(pady=5, fill=tk.X, expand=True)

        self.bubble_sort_button = tk.Button(
            self.buttons_frame,
            text="Bubble Sort",
            command=lambda: self.start_sorting(BubbleSort),
        )
        self.bubble_sort_button.pack(pady=5, fill=tk.X, expand=True)

        self.selection_sort_button = tk.Button(
            self.buttons_frame,
            text="Selection Sort",
            command=lambda: self.start_sorting(SelectionSort),
        )
        self.selection_sort_button.pack(pady=5, fill=tk.X, expand=True)

        self.insertion_sort_button = tk.Button(
            self.buttons_frame,
            text="Insertion Sort",
            command=lambda: self.start_sorting(InsertionSort),
        )
        self.insertion_sort_button.pack(pady=5, fill=tk.X, expand=True)

        self.merge_sort_button = tk.Button(
            self.buttons_frame,
            text="Merge Sort",
            command=lambda: self.start_sorting(MergeSort),
        )
        self.merge_sort_button.pack(pady=5, fill=tk.X, expand=True)

        self.quick_sort_button = tk.Button(
            self.buttons_frame,
            text="Quick Sort",
            command=lambda: self.start_sorting(QuickSort),
        )
        self.quick_sort_button.pack(pady=5, fill=tk.X, expand=True)

        self.heap_sort_button = tk.Button(
            self.buttons_frame,
            text="Heap Sort",
            command=lambda: self.start_sorting(HeapSort),
        )
        self.heap_sort_button.pack(pady=5, fill=tk.X, expand=True)

        # Frame for bottom right controls
        self.control_frame = tk.Frame(self.root, bg=self.style.colors.bg)
        self.control_frame.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

        self.play_button = tk.Button(
            self.control_frame, text="Play", command=self.resume_sorting
        )
        self.play_button.pack(side=tk.RIGHT, padx=5)

        self.pause_button = tk.Button(
            self.control_frame, text="Pause", command=self.pause_sorting
        )
        self.pause_button.pack(side=tk.RIGHT, padx=5)

        self.reset_button = tk.Button(
            self.control_frame, text="Reset", command=self.reset_operations
        )
        self.reset_button.pack(side=tk.RIGHT, padx=5)

        # Disable control buttons initially
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)

        # Dropdown menu for themes
        self.theme_var = tk.StringVar()
        self.theme_var.set(self.current_theme)
        self.theme_dropdown = ttk.Combobox(
            self.buttons_frame,
            textvariable=self.theme_var,
            state="readonly",
            values=themeList,
        )
        self.theme_dropdown.pack(pady=5, side=tk.LEFT, fill=tk.X, expand=True)
        self.theme_dropdown.bind("<<ComboboxSelected>>", self.switch_theme)

        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def generate_array_with_elements(self):
        try:
            num_elements = int(self.num_elements_entry.get())
            if num_elements <= 0:
                raise ValueError("Number of elements should be a positive integer.")

            self.original_array = [random.randint(1, 100) for _ in range(num_elements)]
            self.array = self.original_array[:]  # Copy original array for sorting
            self.draw_array(self.array, [])
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def switch_theme(self, event=None):
        theme_name = self.theme_var.get()

        if theme_name != self.current_theme:
            self.current_theme = theme_name
            self.style.theme_use(self.current_theme)
            self.root.style = self.style

            self.root.configure(
                bg=self.style.colors.bg
            )  # Update window background color

            # Update all widgets that might change appearance based on the theme
            self.generate_button.configure(bg=self.style.colors.primary)
            self.bubble_sort_button.configure(bg=self.style.colors.primary)

            # Regenerate the array if it's empty
            if not self.array:
                self.generate_array()
            else:
                self.draw_array(self.array, [])

    def generate_array(self):
        self.original_array = [random.randint(1, 100) for _ in range(15)]
        self.array = self.original_array[:]  # Copy original array for sorting
        self.draw_array(self.array, [])

    def draw_array(self, array, highlight):
        self.canvas.delete("all")
        canvas_height = 400
        canvas_width = 800

        if len(array) == 0:
            return  # Avoid division by zero if array is empty

        bar_width = canvas_width / len(array)

        # Calculate sorting time
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            time_text = f"Sorting time: {elapsed_time:.2f} seconds"
            self.canvas.create_text(
                10,
                10,
                anchor=tk.NW,
                text=time_text,
                fill="limegreen",
                font=("Arial", 14),
            )

        # Draw bars and values
        for i, height in enumerate(array):
            x0 = i * bar_width
            y0 = canvas_height - height * 3
            x1 = (i + 1) * bar_width
            y1 = canvas_height
            color = (
                "limegreen" if i in highlight else self.style.colors.primary
            )  # Use primary color for bars
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            text_color = self.style.colors.get(
                self.current_theme + ".text_color"
            )  # Get text color based on current theme
            self.canvas.create_text(
                (x0 + x1) / 2,
                y0,
                anchor=tk.S,
                text=str(height),
                fill=text_color,
                font=("Arial", 10, "bold"),
            )

        self.root.update_idletasks()

    def update_speed(self, value):
        self.speed = float(value)
        self.speed_value_label.config(text=f"{float(value):.2f}")

    def start_sorting(self, algorithm):
        if self.sorting_thread and self.sorting_thread.is_alive():
            self.sorting_algorithm.pause()  # Pause the current sorting algorithm

        # Reset sorting state
        self.sorting_algorithm = None
        self.sorting_thread = None
        self.start_time = None

        self.array = self.original_array[:]  # Use original array for sorting
        self.sorting_algorithm = algorithm(self.array, self.draw_array, self.speed)
        self.sorting_thread = threading.Thread(target=self.sorting_algorithm.sort)
        self.start_time = time.time()  # Start timing the sorting

        # Set sorting thread as daemon
        self.sorting_thread.daemon = True
        self.sorting_thread.start()

        # Update button states
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.NORMAL)

        # Disable sorting buttons while sorting is in progress
        self.disable_sorting_buttons()

    def pause_sorting(self):
        if self.sorting_algorithm:
            self.sorting_algorithm.pause()

    def resume_sorting(self):
        if self.sorting_algorithm and self.sorting_algorithm.is_paused():
            self.sorting_algorithm.resume()

    def reset_operations(self):
        if self.sorting_thread and self.sorting_thread.is_alive():
            self.sorting_algorithm.pause()  # Pause the current sorting algorithm

        # Reset sorting state
        self.sorting_algorithm = None
        self.sorting_thread = None
        self.start_time = None

        # Reset array to original generated values
        self.array = self.original_array[:]
        self.draw_array(self.array, [])

        # Reset button states
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)

        # Enable sorting buttons
        self.enable_sorting_buttons()

    def disable_sorting_buttons(self):
        # Disable all sorting buttons while sorting is in progress
        self.bubble_sort_button.config(state=tk.DISABLED)
        self.selection_sort_button.config(state=tk.DISABLED)
        self.insertion_sort_button.config(state=tk.DISABLED)
        self.merge_sort_button.config(state=tk.DISABLED)
        self.quick_sort_button.config(state=tk.DISABLED)
        self.heap_sort_button.config(state=tk.DISABLED)

    def enable_sorting_buttons(self):
        # Enable all sorting buttons when sorting is stopped or reset
        self.bubble_sort_button.config(state=tk.NORMAL)
        self.selection_sort_button.config(state=tk.NORMAL)
        self.insertion_sort_button.config(state=tk.NORMAL)
        self.merge_sort_button.config(state=tk.NORMAL)
        self.quick_sort_button.config(state=tk.NORMAL)
        self.heap_sort_button.config(state=tk.NORMAL)

    def on_closing(self):
        if self.sorting_thread and self.sorting_thread.is_alive():
            self.sorting_algorithm.pause()  # Pause the current sorting algorithm

        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
