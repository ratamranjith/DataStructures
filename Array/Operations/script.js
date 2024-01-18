// scripts.js

document.addEventListener('DOMContentLoaded', function () {
    // Call generate_random when the page loads
    generate_random();
});

function generate_random() {
    let length = 15;
    let arrayContainer = document.querySelector('.arrayData');

    // Clear existing content in the array container
    arrayContainer.innerHTML = "";

    for (let i = 0; i < length; i++) {
        let value = Math.floor(Math.random() * (length * i));

        // Create a fieldset element
        let fieldset = document.createElement("fieldset");
        fieldset.className = "fieldClass"
        // Create a legend element and set its text content to the index
        let legend = document.createElement("legend");
        legend.textContent = `Index : ${i}`;

        // Create a div element for the random number
        let element = document.createElement("div");
        element.className = "arrayElement";
        element.setAttribute('name', 'eleData');
        element.textContent = value;

        // Append the legend and div elements to the fieldset
        fieldset.appendChild(legend);
        fieldset.appendChild(element);

        // Append the fieldset to the arrayContainer
        arrayContainer.appendChild(fieldset);

        console.log(value);
    }
}

function performArrayOperation() {
    // Get selected operation (insert, delete, search, sorting)
    let operation = document.querySelector('input[name="oprs"]:checked').value;
    let itemsList = [];
    document.querySelectorAll('.arrayData fieldset legend').forEach((legend) => {
        itemsList.push(legend.textContent.split(':')[1].trim());
    });
    console.log(itemsList);
    // Get user input and position values
    let userInput = document.getElementById('userinput').value;
    let position = document.getElementById('position');
    positionValue = position.value;

    // Get the array container
    var arrayContainer = document.querySelector('.arrayData1');

    // Clear existing content in the array container
    arrayContainer.innerHTML = "";

    // Perform the selected array operation based on the values obtained above
    if (operation === 'insert') {
        // Implement your logic for insertion using 'positionValue'
        // For now, let's just display a message
        arrayContainer.innerHTML = `Insert operation selected at position ${positionValue}`;
    } else if (operation === 'delete') {
        // Implement your logic for deletion
        // For now, let's just display a message
        arrayContainer.innerHTML = "Delete operation selected";
    } else if (operation === 'search') {
        // Implement your logic for search
        // For now, let's just display a message
        arrayContainer.innerHTML = `Search operation selected with user input ${userInput} and position ${positionValue}`;
    } else if (operation === 'sorting') {
        // Implement your logic for sorting
        // For now, let's just display a message
        arrayContainer.innerHTML = "Sorting operation selected";
    }
}