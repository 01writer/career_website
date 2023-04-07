from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Gurugram, India',
  'salary': 'Rs.12,00,000'
}, {
  'id': 2,
  'title': 'Font End Developer',
  'location': 'Pune, India',
  'salary': ''
}, {
  'id': 3,
  'title': 'Full Stack',
  'location': 'London, United Kingdom',
  'salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Webbullz')

@app.route('/api')
def list_job():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
