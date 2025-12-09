"use strict";

const num1 = document.getElementById('num1');
const num2 = document.getElementById('num2');
const result = document.getElementById('result');
const operation = document.getElementById('operation');
const button = document.getElementById('start');

button.addEventListener('click', function () {
  const a = Number(num1.value);
  const b = Number(num2.value);
  let answer = '';

  if (operation.value === 'add') {
    answer = a + b;
  } else if (operation.value === 'sub') {
    answer = a - b;
  } else if (operation.value === 'multi') {
    answer = a * b;
  } else if (operation.value === 'div') {
    answer = a / b;
  }

  result.textContent = answer;
});
