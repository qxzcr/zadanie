from flask import Flask, request, render_template
import logging
import datetime
import requests
import os

#Konfiguracja logowania
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Inicjalizacja aplikacji Flask
app = Flask(__name__)

AUTHOR = "Yelyzaveta Zlydnieva"
PORT = os.getenv("PORT", 5000)


COUNTRIES_CITIES = {
    "Polska": ["Warszawa", "Kraków", "Gdańsk", "Wrocław", "Lublin"],
    "Niemcy": ["Berlin", "Monachium", "Hamburg", "Kolonia", "Frankfurt"],
    "Francja": ["Paryż", "Lyon", "Marsylia", "Tuluza", "Nicea"],
    "Włochy": ["Rzym", "Mediolan", "Neapol", "Turyn", "Florencja"]
}

#Logowanie informacji przy starcie aplikacji
startup_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logger.info(f"Data uruchomienia: {startup_time}")
logger.info(f"Autor: {AUTHOR}")
logger.info(f"Port TCP: {PORT}")

#Strona główna aplikacji
@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    selected_country = None
    cities = []

    #Jeśli użytkownik wysłał formularz
    if request.method == "POST":
        selected_country = request.form.get("country")
        city = request.form.get("city")

        #Zaktualizujemy listę miast na podstawie wybranego kraju
        if selected_country in COUNTRIES_CITIES:
            cities = COUNTRIES_CITIES[selected_country]

            #Pobieramy dane pogodowe, jeśli miasto zostało wybrane
            if city and city in cities:
                api_key = "e3752818441fd5ae6c1fb0940dbe8f5d"
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{selected_country}&appid={api_key}&units=metric"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    weather_data = {
                        "city": city,
                        "country": selected_country,
                        "temperature": data["main"]["temp"],
                        "description": data["weather"][0]["description"],
                        "humidity": data["main"]["humidity"]
                    }

    #Jeśli żaden kraj nie jest wybrany, ustawimy pierwszy z listy
    if not selected_country:
        selected_country = list(COUNTRIES_CITIES.keys())[0]
        cities = COUNTRIES_CITIES[selected_country]

    
    return render_template("index.html", countries=COUNTRIES_CITIES.keys(), cities=cities, selected_country=selected_country, weather_data=weather_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))