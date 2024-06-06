# import flast module
from flask import Flask, render_template,redirect, url_for, request, json, current_app as app
import os, random


# instance of flask application
app = Flask(__name__)

app.secret_key = "sdfasdgestrhtrryjyj54er65thgs6dhdhDsdgfsg4fsg5fs5g15fd1g5f"

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))



# home route that returns below text when root url is accessed
@app.route("/", methods=["GET"])
def home():
	return render_template('home.html')



@app.route("/about", methods=["GET"])
def about():
	json_url = os.path.join(SITE_ROOT, "static/data", "user_info.json")
	data = json.load(open(json_url))
	return render_template('about.html', info=data)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name  = request.form.get('name')
        email = request.form.get('email')
        occupation = request.form.get('occupation')
        department = request.form.get('department')
        status   = request.form.get('status')
        position = request.form.get('position')
        
        print("----------------")
        print("name =", name)
        print("email =", email)
        print("occupation =", occupation)
        print("status =", status)
        print("position =", position)
        print("department =", department)
        print("----------------")

        new_user = {
            "id": random.randint(0, 100),
            "name": name,
            "email": email,
            "occupation": occupation,
            "department": department,
            "status": status,
            "position": position
        }
        
        # Append new user data to user_info.json
        json_url = os.path.join(SITE_ROOT, "static/data", "user_info.json")
        with open(json_url, "r") as file:
            data = json.load(file)
        
        data.append(new_user)
        
        with open(json_url, "w") as file:
            json.dump(data, file, indent=4)
        
        return redirect(url_for('about'))
    
    return render_template('create.html')



if __name__ == '__main__': 
    app.run(debug = True)

