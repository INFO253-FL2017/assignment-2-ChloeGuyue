# LEARNINGS Muxuan
1. What is the function of the following technologies in your assignment:
* HTML: HTML is an agreed-upon markup language. I used it to organize the content of my web pages.
* CSS: I used CSS to format the HTML pages that I've written.
* JavaScript: I used JavaScript to add functions to the HTML so that it can interact with users in response to their actions.
* Python: I used Python script to power the whole application.
* Flask: Flask is a python framework for web development. I used it to facilitate the web development process; it makes develop web pages much easier and more convenient.
* HTTP: HTTP is a protocol for hypertext to transfer between servers and clients. The function of HTTP in my assignment is to ensure the transfer of requests/response between my server and user requests.
* GET and POST requests: GET: a request method, with which users can request for data from server.  POST: another request method, with which users can both request and post data from/to the server.
---
2. How does HTML, CSS, and JavaScript work together in the browser for this assignment?
* HTML is the foundation of the webpage; CSS conveniently format all the HTML pages to make them look better; JavaScript makes my HTML pages dynamic by dynamically accessing some data and show it on the web pages and it also implemented some small functions.
---
3. How does Python and Flak work together in the server for this assignment?
* Python is the overall language we adopted to power the server. Flask is a python module, which facilitates the process of making dynamic website, e.g. rendering the HTML pages to the browser with a simple imported method.
---
4. List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request?
* "GET / HTTP/1.1" 200 - successfully returns the main page(0.0.0.0;5000)
* "GET /static/css/style.css HTTP/1.1" 200 - successfully loads the CSS file
* "GET /static/js/script.js HTTP/1.1" 200 - successfully loads the JS file
* "GET /static/css/1.jpg HTTP/1.1" 200 - successfully loads the background picture
* "GET /about HTTP/1.1" 200 - successfully returns the about page
* "GET /contact HTTP/1.1" 200 - successfully returns the contactus page
* "POST /contact HTTP/1.1" 200 - successfully sends the email
* "GET /blog/* HTTP/1.1" 200 - successfully returns the blogs page
* "GET /static/css/style2.css HTTP/1.1" 200 - successfully loads the CSS file
* "GET /static/js/script2.js HTTP/1.1" 200 - successfully loads the JS file
* "GET /static/css/2.jpg HTTP/1.1" 200 - successfully loads the background picture
