from app import app
import pandas as pd

# Use Pandas to read in the csv file to a dataframe
df = pd.read_csv('https://data.sfgov.org/api/views/rqzj-sfat/rows.csv')
# Select only a few fields in the dataframe and sort them by the Applicant Name A-Z
# Enhancement: allow user to sort on frontend
df2 = df[["Applicant","Address","FoodItems", "Latitude","Longitude","Status"]].sort_values(by=['Applicant'])
# Display only results that have been approved
all_results = df2[df2["Status"].str.contains("APPROVED")]