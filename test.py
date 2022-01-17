from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello World!"

if __name__ == "__main__" and "get_ipython" not in locals():  # ne pas exécuter dans un notebook
    app.run()

