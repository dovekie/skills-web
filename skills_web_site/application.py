from flask import Flask, request, render_template, redirect, flash
import os

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("application-form.html")
	
@app.route("/application", methods=['GET','POST'])
def show_form():
	given_name_input = request.form.get("given-name")
	surname_input = request.form.get("surname")
	salary_input = request.form.get("salary")
	job_input = request.form.get("job")
	
	output_text = "Dear %s %s, thank you for applying with the new web order. You have asked for %s to be our %s. Your request will be considered in the order in which it was received." %(given_name_input, surname_input, salary_input, job_input)
	
	return render_template("form_ack.html", submission_text=output_text)
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)