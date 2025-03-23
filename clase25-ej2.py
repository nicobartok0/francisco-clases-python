from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nombre = None
    if request.method == "POST":
        nombre = request.form.get("nombre")  
    return render_template("index2.html", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)
