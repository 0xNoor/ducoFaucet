from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("lottery.html")



if __name__ == '__main__':
   app.run(debug=True, host="192.168.0.76", port=4444)