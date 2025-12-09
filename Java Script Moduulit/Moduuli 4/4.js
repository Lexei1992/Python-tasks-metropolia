"use strict";

var form = document.querySelector("#searchForm");
var input = document.querySelector("#query");
var results = document.querySelector("#results");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  var value = input.value.trim();
  if (!value) {
    return;
  }

  fetch("https://api.tvmaze.com/search/shows?q=" + value)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      results.innerHTML = "";

      data.forEach(function (item) {
        var show = item.show;

        var article = document.createElement("article");

        var h2 = document.createElement("h2");
        h2.textContent = show.name;
        article.appendChild(h2);

        var a = document.createElement("a");
        a.href = show.url;
        a.target = "_blank";
        a.textContent = "Details";
        article.appendChild(a);

        var img = document.createElement("img");
        img.alt = show.name;
        img.src =
          show.image && show.image.medium
            ? show.image.medium
            : "https://placehold.co/210x295?text=Not%20Found";

        article.appendChild(img);

        var summary = document.createElement("div");
        summary.innerHTML = show.summary;
        article.appendChild(summary);

        results.appendChild(article);
      });
    })
    .catch(function (err) {
      console.error(err);
    });
});
