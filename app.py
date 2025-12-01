from flask import Flask, render_template, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

movies = [
    "Legenda Senja", "Malam di Jakarta", "Pahlawan Kota", "Cinta dan Kopi",
    "Petualangan Nusantara", "Terowongan Waktu", "Operasi Rahasia", "Komedi Kampus",
    "Hantu di Gedung Tua", "Romansa Musim Hujan"
]
halls = [f"Studio {i}" for i in range(1, 6)]

def generate_ticket(name, movie):
    show_time = datetime.now() + timedelta(days=random.randint(1,7))
    seat = f"{chr(random.randint(65,70))}{random.randint(1,15)}"
    ticket_id = f"TKT{random.randint(1000,9999)}"
    return {
        "ticket_id": ticket_id,
        "name": name,
        "movie": movie,
        "hall": random.choice(halls),
        "seat": seat,
        "show_time": show_time.strftime("%Y-%m-%d %H:%M"),
        "price": random.choice([35000,45000,50000,60000])
    }

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/pesan", methods=["POST"])
def pesan():
    name = request.form["name"]
    movie = request.form["movie"]
    ticket = generate_ticket(name, movie)
    return render_template("tiket.html", ticket=ticket)

if __name__ == "__main__":
    app.run(debug=True)
