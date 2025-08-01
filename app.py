from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "segredo_super_secreto"  # troque por algo seguro

# Usuário fixo
USERS = {
    "admin": "12345"  # usuario: senha
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["usuario"]
        password = request.form["senha"]

        if username in USERS and USERS[username] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("index.html", error="Usuário ou senha inválidos!")

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", usuario=session["user"])
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
