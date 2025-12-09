"use strict";

var form = document.querySelector("form");
var input = document.querySelector("#query");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  var value = input.value.trim();
  if (!value) return;

  fetch("https://api.tvmaze.com/search/shows?q=" + value)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
    })
    .catch(function (err) {
      console.error(err);
    });
});
