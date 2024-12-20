from flask import Flask
import python-1
>>>>>>> 071e34ddf0b7699e565c236f8702d5ec408e09f3

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
