"use strict";
const trigger = document.querySelector("#trigger");
const img = document.querySelector("#target");
trigger.addEventListener("mouseover", function () {
  img.src = "img/picB.jpg";
});
trigger.addEventListener("mouseout", function () {
  img.src = "img/picA.jpg";
});