import pandas as pd
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "Welcome"

@app.route("/list")
def get_list():
    df = pd.read_csv('https://data.sfgov.org/api/views/rqzj-sfat/rows.csv')
    df2 = df[["Applicant","Address","FoodItems", "Latitude","Longitude","Status"]]
    return df2[df2["Status"].str.contains("APPROVED")].to_html()