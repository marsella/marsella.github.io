from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/art')
def art():
  return render_template('art.html')

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0',port=80)

