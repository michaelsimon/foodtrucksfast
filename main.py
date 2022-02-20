import pandas as pd
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def index():
    title = "Home"
    return render_template("index.html", title=title)


@app.route("/list")
def get_list():
    title = "Food Truck List"
    df = pd.read_csv('https://data.sfgov.org/api/views/rqzj-sfat/rows.csv')
    df2 = df[["Applicant","Address","FoodItems", "Latitude","Longitude","Status"]]
    # df2[df2["Status"].str.contains("APPROVED")].to_html()
    return render_template("list.html", title=title, data=df2[df2["Status"].str.contains("APPROVED")])
