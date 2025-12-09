"use strict";
const button = document.querySelector("button");
button.addEventListener('click', function(evt){
  alert(evt.currentTarget.tagName + ' was clicked');});