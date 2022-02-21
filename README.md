# Food Trucks Fast

Food Trucks Fast is a web application that displays the location of Food Trucks in San Francisco using publicly available data. It was developed in Python using Flask and Pandas on the backend with Bootstrap framework on the frontend.

Users can currently display a listing of food trucks (with approved permits) along with its address, the foods served and a link to a map. Users can also search for a specific food truck.

A hosted version of this application is available at [https://foodtrucks.michaelsimon.co](https://foodtrucks.michaelsimon.co)

## Installation

- Ensure you can have python3 installed. You can verify this by running `python3 --version` from a command line. To download and install python visit [https://www.python.org/downloads/](https://www.python.org/downloads/).

- Ensure you have pip installed. This is typically included with python. Validate by running `python3 -m pip --version` from a command line.

- Clone this repository by running 

- Using a command line terminal, `cd` to the location of the clone.

- Run `python3 -m pip install -r requirements.txt` to install the additional packages required (including flask, pandas, and gunicon).

- Run `gunicorn app:app` to start a local webserver and access the application at `http://127.0.0.1:8000` (or port 8001)

## Usage

- Upon launching the application, click the "View all food trucks" button to view all available food trucks.

- Search for a food truck in the top right corner of the navigation bar.

- Click the "Map it" button on any listing to view a Google Map of the food truck location.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)