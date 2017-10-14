var form = document.getElementById('comment_section');
var storage = window.localStorage;
var area = document.getElementById("comment_area");
form.addEventListener("submit", function(event){

  var comment = form.elements.namedItem("text").value;
  var name = form.elements.namedItem("name").value;

  storage.setItem(name,comment);

  area.innerHTML += comment + "<br>" + "by " + name + "<hr>";
})
