"use strict";

var button = document.querySelector("button");

button.addEventListener("click", function () {
  fetch("https://api.chucknorris.io/jokes/random")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data.value);
    })
    .catch(function (err) {
      console.error(err);
    });
});
