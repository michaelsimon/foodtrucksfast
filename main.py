import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

df = pd.read_csv('https://data.sfgov.org/api/views/rqzj-sfat/rows.csv')
df2 = df[["Applicant","Address","FoodItems", "Latitude","Longitude","Status"]].sort_values(by=['Applicant'])
all_results = df2[df2["Status"].str.contains("APPROVED")]

@app.route("/")
def index():
    title = "Welcome"
    return render_template("index.html", title=title)


@app.route("/list")
def get_list():
    title = "All Your Options"
    return render_template("list.html", title=title, data=all_results)

@app.route("/search", methods=['POST'])
def search():
    title = "Search"
    if request.method == "POST":
        search_term = request.form["search_term"]
        results = all_results[all_results["Applicant"].str.contains(search_term, case=False) | all_results["FoodItems"].str.contains(search_term, case=False) | all_results["Address"].str.contains(search_term, case=False)]
        return render_template("list.html", title=title, data=results)

@app.errorhandler(500)
def error():
    title = "Error"
    return render_template("error.html", title=title)