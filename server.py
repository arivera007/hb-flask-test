from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


app = Flask(__name__)

JOBS = [
    'Software Engineer', 'QA Engineer', 'Product Manager']

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

@app.route('/')
def serve_home():
    return render_template("index.html")
    # return "templates/index.html"

@app.route('/application-form')
def application_form():
    return render_template("application-form.html", jobs = JOBS)

@app.route('/application-success', methods=["POST"] )
def application_success():

    # firstname = request.args.get("firstname")
    # lastname = request.args.get("lastname")
    # jobtype = request.args.get("jobtype")
    # salary = request.args.get("salary")
    
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    jobtype = request.form.get("jobtype")
    salary = request.form.get("salary")
    
    # salary = request.args.get("salary")   #args or form?
    
    return render_template("application-response.html", success_firstname = firstname,
                                                                success_lastname = lastname,
                                                                success_jobtype = jobtype,
                                                                success_salary = salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
