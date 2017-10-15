"""
webserver.py

File that is the central location of code for your webserver.
"""

import requests
import os
from flask import Flask, request,render_template


# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def main_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/index')
def home_page():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("aboutus.html")

@app.route('/contact',methods=['GET'])
def show_contact_page():
    return render_template("contactus.html",notifications=[])

@app.route('/contact',methods=['POST'])
def send_email():
    name = request.form.get("Name")
    subject = request.form.get("Subject")
    message = request.form.get("Message")
    email = request.form.get("Email")
    notifications = []
    a = []
    missing_value = ''
    if name and subject and message:
        content = "Name: " + name + "\n" + "Email: " + email + "\n" + "Subject: " + subject + "\n" + "Message: " + message + "\n"

        data = {
            'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
            'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
            'subject': "You just was sent a message",
            'text': content,
        }
        auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

        r = requests.post(
            'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
            auth=auth,
            data=data)
        if r.status_code == requests.codes.ok:
            notifications.append("Hi "+name+", Your email was sent!!!")
        else:
            notifications.append("You email was not sent. Please try again later")
    else:
        if not name:
            a += ["\"Name\""]
        if not email:
            a += ["\"Email\""]
        if not subject:
            a += ["\"Subject\""]
        if not message:
            a += ["\"Message\""]
        for elem in a:
            missing_value += elem + '  '
        notifications.append(missing_value + "Missing. You email was not sent. Please try again later")

    return render_template("contactus.html", notifications=notifications)

@app.route('/blog/8-experiments-in-motivation')
def blog_one():
    return render_template("/blog/8 Experiments in Motivation.html")

@app.route('/blog/a-mindful-shift-of-focus')
def blog_two():
    return render_template("/blog/A Mindful Shift of Focus.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def blog_three():
    return render_template("/blog/How to Develop an Awesome Sense of Direction.html")

@app.route('/blog/training-to-be-a-good-writer')
def blog_four():
    return render_template("/blog/Training to Be a Good Writer.html")

@app.route('/blog/what-productivity-systems-wont-solve')
def blog_five():
    return render_template("/blog/What Productivity Systems Won't Solve.html")
