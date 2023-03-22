from flask import Flask, render_template, request, jsonify
from database import load_db, load_hospital_from_db

app = Flask(__name__)


@app.route("/")
def renders():
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
  hospitals = load_db()
  return render_template('bookappt.html', hospitals=hospitals)


@app.route("/bookappt/<id>")
def show_hospital(id):
  hospital = load_hospital_from_db(id)
  if not hospital:
    return "Not Found", 404
  return render_template('hospital.html', hospital=hospital)


@app.route("/kinds")
def kinds():
  return render_template('kinds.html')


@app.route("/results")
def results():
  return render_template('results.html')


@app.route("/contactform", methods=['post'])
def contact():
  data = request.form
  # add_contact_info(data)
  return render_template('contactform.html', data=data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
