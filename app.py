from flask import Flask, render_template, request, jsonify
import google.generativeai as genai


app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyAPenmXNkIyr32H-YDy_oV3hqp3Yy9FB6M")
model = genai.GenerativeModel("gemini-1.5-pro")


@app.route("/")
def index():
    return render_template("index.html")  # Load the webpage

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = model.generate_content(user_message)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
