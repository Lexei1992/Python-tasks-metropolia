"use strict";

const input = document.getElementById("calculation");
const button = document.getElementById("start");
const result = document.getElementById("result");

button.addEventListener("click", function () {
    const text = input.value;
    let num1, num2, answer;

    if (text.includes("+")) {
        const parts = text.split("+");
        num1 = Number(parts[0]);
        num2 = Number(parts[1]);
        answer = num1 + num2;

    } else if (text.includes("-")) {
        const parts = text.split("-");
        num1 = Number(parts[0]);
        num2 = Number(parts[1]);
        answer = num1 - num2;

    } else if (text.includes("*")) {
        const parts = text.split("*");
        num1 = Number(parts[0]);
        num2 = Number(parts[1]);
        answer = num1 * num2;

    } else if (text.includes("/")) {
        const parts = text.split("/");
        num1 = Number(parts[0]);
        num2 = Number(parts[1]);
        answer = num1 / num2;

    } else {
        answer = "Invalid input";
    }

    result.textContent = answer;
});
