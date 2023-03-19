from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_db():

  with engine.connect() as conn:
    result = conn.execute(text("select * from hospitals"))

    result_dicts = []
    for row in result.all():
      result_dicts.append(row._mapping)

  return result_dicts


@app.route("/")
def renders():
  return render_template('home.html')


@app.route("/home")
def home():
  return render_template('home.html')


@app.route('/about')
def about():
  return render_template("about.html")


@app.route("/treat")
def treat():
  return render_template('treat.html')


@app.route("/predict")
def predict():
  return render_template('predict.html')


@app.route("/bookappt")
def bookappt():
  jobs = load_db()
  return render_template('bookappt.html', jobs=jobs)


@app.route("/kinds")
def kinds():
  return render_template('kinds.html')


@app.route("/results")
def results():
  return render_template('results.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
