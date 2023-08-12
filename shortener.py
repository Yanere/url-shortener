from flask import Flask, request, redirect, g, render_template
import sqlite3
import random
import string

app = Flask(__name__)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("shortener.db")
        g.db.row_factory = sqlite3.Row
        create_table()
    return g.db

def create_table():
    cursor = g.db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT NOT NULL,
            short_url TEXT NOT NULL
        )
    ''')
    g.db.commit()

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "db"):
        g.db.close()

@app.route("/")
def greetings():
    return render_template("base.html")

@app.route("/shorten", methods=["POST"])
def shortener():
    long_url = request.form.get("long_url")
    if not long_url:
        return "INVALID URL TRY AGAIN"

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT short_url FROM urls WHERE long_url=?", (long_url,))
    result = cursor.fetchone()

    if result:
        short_url = result[0]
    else:
        short_url = generate_short_url()
        cursor.execute("INSERT into urls (long_url, short_url) VALUES (?,?)", (long_url, short_url))
        g.db.commit()

    return render_template("shorturl.html", shortened_url=short_url)

def generate_short_url():
    available_chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(available_chars) for _ in range(6))
    return short_url

@app.route("/<short_url>")
def redirect_to_long(short_url):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT long_url FROM urls WHERE short_url=?", (short_url,))
    result = cursor.fetchone()

    if result:
        long_url = result[0]
        return redirect(long_url)
    else:
        return "Short URL not found :("

if __name__ == "__main__":
    app.run()
