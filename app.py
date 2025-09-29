from flask import Flask, render_template, request
import json


app = Flask(__name__)

projects_list: list[dict] = []


def main() -> None:
    app.run(debug=True)


@app.route("/")
def index():
    return render_template("index.jinja")

@app.route("/projects")
def projects():
    projects_list = get_json("static/json/projects.json")
    icons_list = get_json("static/json/icons.json")
    
    return render_template("projects.jinja", projects_list=projects_list, icons=icons_list)

def get_json(json_file) -> list[dict]:
    with open(json_file) as projects_json:
        return json.load(projects_json)


if __name__ == '__main__':
    main()