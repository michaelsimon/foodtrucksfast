import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
# Use Pandas to read in the csv file to a dataframe
df = pd.read_csv('https://data.sfgov.org/api/views/rqzj-sfat/rows.csv')
# Select only a few fields in the dataframe and sort them by the Applicant Name A-Z
# Enhancement: allow user to sort on frontend
df2 = df[["Applicant","Address","FoodItems", "Latitude","Longitude","Status"]].sort_values(by=['Applicant'])
# Display only results that have been approved
all_results = df2[df2["Status"].str.contains("APPROVED")]

# Create a route to the homepage
@app.route("/")
def index():
    title = "Welcome"
    return render_template("index.html", title=title)

# Create a route to list all of the results, display using the list template file
@app.route("/list")
def get_list():
    title = "All Your Options"
    return render_template("list.html", title=title, data=all_results)

# Create a route to search for a food trucks by name (applicant), items in the food list, and address. Search is a post request made from the search form in the page header.
@app.route("/search", methods=['POST'])
def search():
    title = "Search"
    if request.method == "POST":
        search_term = request.form["search_term"]
        results = all_results[all_results["Applicant"].str.contains(search_term, case=False) | all_results["FoodItems"].str.contains(search_term, case=False) | all_results["Address"].str.contains(search_term, case=False)]
        return render_template("list.html", title=title, data=results)

# Handle internal system errors
@app.errorhandler(500)
def error():
    title = "Error"
    return render_template("error.html", title=title)