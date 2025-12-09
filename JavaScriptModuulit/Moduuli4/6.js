"use strict";

var form = document.querySelector("form");
var input = document.querySelector("#query");
var results = document.querySelector("#results");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  var value = input.value.trim();
  if (!value) return;

  fetch("https://api.chucknorris.io/jokes/search?query=" + value)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      results.innerHTML = ""; // clear old results

      data.result.forEach(function (item) {
        var article = document.createElement("article");
        var p = document.createElement("p");

        p.textContent = item.value; // the joke text
        article.appendChild(p);

        results.appendChild(article);
      });
    })
    .catch(function (err) {
      console.error(err);
    });
});
