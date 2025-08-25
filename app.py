from flask import Flask, render_template, request


app = Flask(__name__)


def main() -> None:
    app.run(debug=True)


@app.route("/")
def index():
    return render_template("index.jinja")

@app.route("/projects")
def projects():
    return render_template("projects.jinja")


if __name__ == '__main__':
    main()