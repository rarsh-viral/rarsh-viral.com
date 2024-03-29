import csv
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def myhomepage():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.csv", mode="a") as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer= csv.writer(database, delimiter=",", quotechar="'",quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route("/submit_form", methods=["POST","GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_file(data)
        return render_template("thanku.html")
    else:
        return "something went wrong"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)