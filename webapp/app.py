from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

topics = {
    "incident": ["Reporting", "Resolution"],
    "change": ["Planning", "Implementation"],
    "self service": ["Portal Design", "Automation"],
    "knowledge": ["Article Creation", "Review"]
}

subtopics = {
    "Reporting": ["Initial Report", "Follow-up"],
    "Resolution": ["Troubleshooting", "Closure"],
    "Planning": ["Risk Assessment", "Scheduling"],
    "Implementation": ["Execution", "Validation"],
    "Portal Design": ["UI/UX", "Navigation"],
    "Automation": ["Workflow Setup", "Bot Integration"],
    "Article Creation": ["Drafting", "Formatting"],
    "Review": ["Peer Review", "Publishing"]
}

default_hours = 2

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        hours_data = {}
        total_hours = 0
        for topic in topics:
            topic_total = 0
            for sub in topics[topic]:
                for subsub in subtopics[sub]:
                    key = f"{topic}_{sub}_{subsub}"
                    hours = float(request.form.get(key, default_hours))
                    topic_total += hours
            hours_data[topic] = topic_total
            total_hours += topic_total
        return render_template("summary.html", hours_data=hours_data, total_hours=total_hours)
    return render_template("index.html", topics=topics, subtopics=subtopics, default_hours=default_hours)

@app.route("/summary")
def summary():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
