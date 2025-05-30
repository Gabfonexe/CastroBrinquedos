from flask import redirect, render_template, request, session, url_for
from flask_admin import AdminIndexView
from flask_admin.base import expose
import os

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

def register_admin_routes(app):
    @app.route("/login/admin", methods=["GET", "POST"])
    def login_admin():
        if request.method == "POST":
            password = request.form.get("password")
            if password == ADMIN_PASSWORD:
                session["admin_authenticated"] = True
                session["admin_password_filled"] = password
                return redirect(url_for("admin.index"))
        return render_template("login.html")

    @app.route("/logout", methods=["GET", "POST"])
    def logout():
        session.pop("admin_authenticated", None)
        session.pop("admin_password_filled", None)
        return redirect(url_for("login_admin"))

class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not session.get("admin_authenticated"):
            return redirect(url_for("login_admin"))
        return super().index()
