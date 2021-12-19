from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from controller.urlController import UrlController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secretkey'
db = SQLAlchemy(app)

urlController = UrlController()

@app.route("/", methods=['GET', 'POST'])
def index():
    # post method creates a short for a webpage
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        return urlController.addUrl(url)
    return render_template("index.html")

@app.route("/<id>")
def redirect_url(id):
    return urlController.redirectUrl(id)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5010)
    
