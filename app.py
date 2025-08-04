from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load("naive_bayes_spam.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        message = request.form["message"]
        prediction = model.predict([message])[0]
        result = "Spam" if prediction == 1 else "Ham (Not Spam)"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
