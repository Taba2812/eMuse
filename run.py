from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo # type: ignore

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://earlgibe:mCUVEYOmjdBeifOg@earlgibe.mmluw.mongodb.net/eMuse?retryWrites=true&w=majority"

mongo = PyMongo(app)
db = mongo.db
collection = db.songs

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/<int:year>')
def year_page(year):
    years = list(range(2010, 2026))
    return render_template("years.html", years=years, selected_year=year)

@app.route('/api/<int:year>', methods=['GET'])
def list_songs_by_year(year):
    try:
        songs = collection.find({"Year": year}, {"_id": 0, "Song": 1, "Album": 1, "Length": 1, "Tempo": 1, "Key": 1, "Energy": 1})
        return jsonify(songs)
    except:
        return "", 500

@app.route('/api/songs', methods=['GET'])
def list_songs():
    try:
        # songs = collection.find()
        songs = collection.find({"Year": 2010}, {"_id": 0, "Song": 1, "Album": 1, "Length": 1, "Tempo": 1, "Key": 1, "Energy": 1})
        return jsonify(songs)
    except:
        return "", 500

if __name__ == '__main__':
    app.run(debug=True)

# flask --app run.py --debug run