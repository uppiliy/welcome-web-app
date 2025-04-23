from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        version = "1.0.5"
        return render_template_string("<h1>Welcome to new Version: {{ version }}, {{ name }}</h1>", version=version, name=name)
    return '''
        <form method="post">
            Enter your name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
