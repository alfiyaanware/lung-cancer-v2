from flask import Flask, render_template

app = Flask(__name__)


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
  return render_template('bookappt.html')


@app.route("/kinds")
def kinds():
  return render_template('kinds.html')


@app.route("/results")
def results():
  return render_template('results.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
