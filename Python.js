let display = document.getElementById("display");

function appendToDisplay(value) {
  display.value += value;
}

function clearDisplay() {
  display.value = "";
}

function calculate() {
  try {
    // Replace '×' with '*' for calculation
    let expression = display.value.replace("×", "*");
    // Use Function constructor instead of eval for better security
    display.value = new Function("return " + expression)();
  } catch (error) {
    display.value = "Error";
    setTimeout(clearDisplay, 1000);
  }
}

// Add keyboard support
document.addEventListener("keydown", function (event) {
  const key = event.key;

  if (/[0-9+\-*/.=]/.test(key)) {
    event.preventDefault();
    if (key === "=" || key === "Enter") {
      calculate();
    } else if (key === "Backspace") {
      display.value = display.value.slice(0, -1);
    } else if (key === "Escape") {
      clearDisplay();
    } else if (key === "*") {
      appendToDisplay("×");
    } else {
      appendToDisplay(key);
    }
  }
});
