from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)
WEATHER_SERVICE_URL = os.getenv("WEATHER_SERVICE_URL", "http:://weather-service:5000")

@app.route("/")
def get_news():
    try:
        weather_response = requests.get(f"{WEATHER_SERVICE_URL}/weather")
        weather_data = weather_response.json()

        response = {
            "news": "Breaking news!",
            "weather_info": f"Current weather: {weather_data['condition']}, {weather_data['temperature']} °C"
        }
        return jsonify(response)
    except requests.RequestException as e:
        response = {"error": f"Could not fetch weather data {str(e)}"}
        return jsonify(response), 500
    
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5001)
    