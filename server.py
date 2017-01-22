from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

JOBS = [
    'Software Engineer', 'QA Engineer', 'Product Manager']

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/')
def serve_home():
    return render_template("templates/index.html")

@app.route('/application-form')
def application_form():
    return render_template("templates/application-form.html", jobs = JOBS)

@app.route('/application-success', methods=["POST"] )
def application_success():

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    jobtype = request.form.get("jobtype")
    salary = request.form.get("salary")
    
    # salary = request.args.get("salary")   #args or form?
    
    return render_template("templates/application-success.html", success_firstname = firstname,
                                                                success_lastname = lastname,
                                                                success_jobtype = jobtype)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
