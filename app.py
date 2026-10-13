from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def registration():
    return render_template('registration.html')

@app.route('/success', methods=['POST'])
def success():
    student_id = request.form.get('student_id', '')
    student_name = request.form.get('student_name', '')
    student_email = request.form.get('student_email', '')
    phone_number = request.form.get('phone_number', '')
    year = request.form.get('year', '')

    return render_template(
        'success.html',
        student_id=student_id,
        student_name=student_name,
        student_email=student_email,
        phone_number=phone_number,
        year=year
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)