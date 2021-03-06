from app import app
from flask import Flask, render_template, request
from app import df
@app.route("/")
def index():
    title = "Welcome"
    return render_template("index.html", title=title)

# Create a route to list all of the results, display using the list template file
@app.route("/list")
def get_list():
    title = "All Your Options"
    return render_template("list.html", title=title, data=df.all_results)

# Create a route to search for a food trucks by name (applicant), items in the food list, and address. Search is a post request made from the search form in the page header.
@app.route("/search", methods=['POST'])
def search():
    title = "Search"
    if request.method == "POST":
        search_term = request.form["search_term"]
        results = df.all_results[df.all_results["Applicant"].str.contains(search_term, case=False) | df.all_results["FoodItems"].str.contains(search_term, case=False) | df.all_results["Address"].str.contains(search_term, case=False)]
        return render_template("list.html", title=title, data=results)

# Handle internal system errors
@app.errorhandler(500)
def error():
    title = "Error"
    return render_template("error.html", title=title)