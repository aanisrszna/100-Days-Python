from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# Function to fetch all cafes
def get_cafes():
    conn = sqlite3.connect("cafes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cafe")
    cafes = cursor.fetchall()
    conn.close()
    return cafes


# Function to add a new cafe
def add_cafe(name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price):
    conn = sqlite3.connect("cafes.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cafe (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price))
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        map_url = request.form["map_url"]
        img_url = request.form["img_url"]
        location = request.form["location"]
        has_sockets = bool(request.form.get("has_sockets"))
        has_toilet = bool(request.form.get("has_toilet"))
        has_wifi = bool(request.form.get("has_wifi"))
        can_take_calls = bool(request.form.get("can_take_calls"))
        seats = request.form["seats"]
        coffee_price = request.form["coffee_price"]

        add_cafe(name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats,
                 coffee_price)
        return redirect(url_for("home"))

    cafes = get_cafes()
    return render_template("index.html", cafes=cafes)


@app.route("/delete/<int:cafe_id>")
def delete(cafe_id):
    delete_cafe(cafe_id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
