from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("tutorial.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pandas.read_csv("")
    temperature = df.station(date)
    return {"station": station,  # structure that shows the
            "date": date,
            "temperature": temperature}
    #return render_template("about.html")


app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
