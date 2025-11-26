// Select the display element
const display = document.getElementById('display');

// Function to append number or operator to the display
function appendToDisplay(input) {
    display.value += input;
}

// Function to clear the display
function clearDisplay() {
    display.value = "";
}

// Function to delete the last character
function deleteLast() {
    display.value = display.value.slice(0, -1);
}

// Function to calculate the result
function calculateResult() {
    try {
        // Use eval() to calculate the result
        // Note: eval() is used here for simplicity as requested for beginner level.
        // In a real-world production app, safer alternatives should be used.
        display.value = eval(display.value);
    } catch (error) {
        display.value = "Error";
    }
}
