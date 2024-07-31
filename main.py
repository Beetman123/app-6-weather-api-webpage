from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,  # structure that shows the
            "date": date,
            "temperature": temperature}
    #return render_template("about.html")


"""
@app.route("/api/v1/<word>")
def about(word):
    caps = word.upper()
    return {"definition": caps,  # structure that shows the data
            "word": word}
    #return render_template("about.html")
"""

app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # specify port if using multiple flask apps at once
