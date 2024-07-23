import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
from sorting_visualizer import SortingApp  # Adjust the import as necessary


class TestSortingApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()

        # Patch the ttkbootstrap.Style class
        self.patcher = patch("ttkbootstrap.Style", autospec=True)
        self.mock_style = self.patcher.start()

        self.app = SortingApp(self.root)

    def tearDown(self):
        # Clean up the Tk instance
        self.root.destroy()
        self.patcher.stop()

    def test_fixed_window_size(self):
        geometry = self.root.geometry()  # e.g., "1x1+0+0"

        try:
            # Split the geometry string
            parts = geometry.split("x")
            if len(parts) != 2:
                raise ValueError(f"Invalid format in geometry string: {geometry}")

            width_part, height_part = parts[0], parts[1].split("+")[0]

            # Convert to integers
            width = int(width_part)
            height = int(height_part)

            # Check if width and height are reasonable
            self.assertGreater(width, 0, "Width should be greater than 0")
            self.assertGreater(height, 0, "Height should be greater than 0")

        except (ValueError, IndexError) as e:
            self.fail(f"Invalid geometry format: {geometry} - {str(e)}")

    # Other test methods here...


if __name__ == "__main__":
    unittest.main()
