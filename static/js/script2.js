var form = document.getElementById('comment_section');
var storage = window.localStorage;
var area = document.getElementById("comment_area");
form.addEventListener("submit", function(event){

  var comment = form.elements.namedItem("text").value;
  var name = form.elements.namedItem("name").value;

  storage.setItem(name,comment);

  area.innerHTML += comment + "<br>" + "by " + name + "<hr>";
})



var weatherContainer = document.getElementById("weather_div");
function requestWeather(){
  var ourRequest = new XMLHttpRequest();
  ourRequest.open('GET','http://api.openweathermap.org/data/2.5/weather?id=5327684&APPID=bc9af5272ea0f9b4df3aabb8eaeddf10&units=metric');

  ourRequest.onload = function(){
    var ourData = JSON.parse(ourRequest.responseText);
    var htmlString = "<p>" + "Current Temperature: "+ourData.main.temp+"&nbsp;"+"Celcius"+"</p>"+
    "<p>"+"Min:"+"&nbsp;"+ourData.main.temp_min+"&nbsp;Celcius;&nbsp;&nbsp;Max:&nbsp;"+ourData.main.temp_max+"&nbsp;Celcius</p>"+
    "<p>"+ourData.weather[0].main+":&nbsp;"+ourData.weather[0].description+"</p>";
    weatherContainer.insertAdjacentHTML('beforeend',htmlString);
  }

  ourRequest.send();
};

requestWeather();
