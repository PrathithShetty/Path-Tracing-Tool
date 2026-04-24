from flask import Flask, render_template
import requests

app = Flask(__name__)

RYU_URL = "http://127.0.0.1:8080"

def get_path():
    try:
        switches = requests.get(f"{RYU_URL}/stats/switches").json()
        path = []

        for sw in switches:
            flows = requests.get(f"{RYU_URL}/stats/flow/{sw}").json()
            for flow in flows[str(sw)]:
                actions = flow.get('actions', [])
                for act in actions:
                    if "OUTPUT" in act:
                        path.append(f"S{sw} → {act}")

        return path
    except:
        return ["Error fetching path"]

@app.route('/')
def home():
    path = get_path()
    return render_template("index.html", path=path)

if __name__ == '__main__':
    app.run(debug=True)
