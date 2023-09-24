from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_url = "http://api.weatherstack.com/current"
api_key = "55142c28c2d538f1b5f29e4dd0c364b7"
default_location = "Edmonton"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location = request.form.get("location")
        if location:
            params = {
                "access_key": api_key,
                "query": location,
            }
            response = requests.get(api_url, params=params)

            if response.status_code == 200:
                data = response.json()
                temperature = data["current"]["temperature"]
                description = data["current"]["weather_descriptions"][0]

                return render_template("index.html", location=location, temperature=temperature,
                                       description=description)
            else:
                error_message = "Error fetching weather data. Please try again later."
                return render_template("index.html", error_message=error_message)


    return render_template("index.html", location=default_location)



if __name__ == '__main__':
    app.run(debug=True)
