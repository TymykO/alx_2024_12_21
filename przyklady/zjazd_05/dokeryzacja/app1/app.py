from flask import Flask, jsonify
import random


app = Flask(__name__)

@app.route("/weather")
def get_weather():
    weather_conditions = ["Sunny", "Rainy", "Clody", "Windy"]
    temperature = random.randint(-10, 40)

    return jsonify(
        {
            "condition": random.choice(weather_conditions),
            "temperature": temperature
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)