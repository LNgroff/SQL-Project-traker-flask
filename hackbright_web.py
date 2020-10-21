"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")


@app.route("/add-student-form")
def add_student_form():
    """Show form for searching for a student"""

    return render_template("add_student_form.html")


@app.route("/student-add", methods=['POST'])
def get_new_student():
    """Add new student and information."""

    github = request.form.get('github')
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    hackbright.make_new_student(fname, lname, github)

    print("hello")

    return render_template("student_added.html", github=github)

    









if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")



