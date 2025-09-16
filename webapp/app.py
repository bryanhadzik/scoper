
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

topics = {
    "incident": ["reporting", "resolution"],
    "change": ["planning", "implementation"],
    "self service": ["portal", "automation"],
    "knowledge": ["articles", "training"]
}

sub_subtopics = {
    "reporting": ["initial report", "follow-up"],
    "resolution": ["diagnosis", "fix"],
    "planning": ["risk assessment", "schedule"],
    "implementation": ["deployment", "review"],
    "portal": ["design", "access"],
    "automation": ["workflow", "integration"],
    "articles": ["creation", "review"],
    "training": ["sessions", "materials"]
}

@app.route("/")
def index():
    return render_template("index.html", topics=topics, sub_subtopics=sub_subtopics)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
