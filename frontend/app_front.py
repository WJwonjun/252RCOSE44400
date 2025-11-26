from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# URL of the backend container inside Docker network
BACKEND_URL = "http://backend:5001"


@app.route("/", methods=["GET"])
def index():
    """
    TODO:
    - Send a GET request to BACKEND_URL + "/api/message"
    - Extract the message from the JSON response
    - Render index.html and pass the message as "current_message"
    """
    response = requests.get(f"{BACKEND_URL}/api/message")
    data = response.json()
    stored_message = data.get("message", "")
    
    # Parse timestamp from message
    timestamp = ""
    if "(updated at" in stored_message:
        # Extract timestamp from "message (updated at YYYY-MM-DD HH:MM:SS)"
        start = stored_message.rfind("(updated at ")
        end = stored_message.rfind(")")
        if start != -1 and end != -1:
            timestamp = stored_message[start + 12:end]
            stored_message = stored_message[:start].strip()

    return render_template("index.html", current_message=stored_message, timestamp=timestamp)

@app.route("/update", methods=["POST"])
def update():
    """
    TODO:
    - Get the value from the form field named "new_message"
    - Send a POST request to BACKEND_URL + "/api/message"
      with JSON body { "message": new_message }
    - Redirect back to "/"
    """
    new_message = request.form.get("new_message", "")
    requests.post(
        f"{BACKEND_URL}/api/message",
        json={"message": new_message}
    )
    return redirect("/")


# v2 TODO:
# - Change page title (in HTML)
# - Parse timestamp from backend message
# - Show "Last updated at: <timestamp>" in the template


if __name__ == "__main__":
    # Do not change the host or port
    app.run(host="0.0.0.0", port=5000)

