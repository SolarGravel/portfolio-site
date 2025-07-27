from flask import Flask, render_template


app = Flask(__name__)


def main() -> None:
    app.run(debug=True)


@app.route("/")
def index():
    return render_template("index.jinja")


if __name__ == '__main__':
    main()