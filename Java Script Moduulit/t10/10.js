"use strict";

const form = document.querySelector("#source");
const target = document.querySelector("#target");

form.addEventListener("submit", function (evt) {
  evt.preventDefault();

  const first = document.querySelector('input[name="firstname"]').value;
  const last = document.querySelector('input[name="lastname"]').value;

  target.textContent = `Your name is ${first} ${last}`;
});
