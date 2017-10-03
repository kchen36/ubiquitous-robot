from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def root():
    return render_template("form.html")

@app.route("/request", methods = ["POST","GET"])
def requests():
    return render_template("request.html",
                           name = request.form['name'],
                           method = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
