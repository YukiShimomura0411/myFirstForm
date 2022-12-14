from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("start.html")

@app.route('/procForm', methods=['POST'])
def processPost():
    a = request.form['msg2']
    b = request.form['msg3']
    a = int(a)
    b = int(b)
    c = a+b
    return render_template("result.html", message = c)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)