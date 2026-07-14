from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary history list
history_data = []

# ==========================
# HOME PAGE
# ==========================
@app.route('/')
def home():
    return render_template("home.html")


# ==========================
# PREDICTION PAGE
# ==========================
@app.route('/predict')
def predict():
    return render_template("predict.html")


# ==========================
# PREDICT LOAN
# ==========================
@app.route('/result', methods=['POST'])
def result():

    name = request.form.get('name')
    gender = request.form.get('gender')
    age = request.form.get('age')
    income = float(request.form.get('income'))
    loan = float(request.form.get('loan'))
    cibil = int(request.form.get('cibil'))
    education = request.form.get('education')
    employment = request.form.get('employment')
    married = request.form.get('married')
    credit_history = request.form.get('credit_history')
    property_area = request.form.get('property')

    # --------------------------
    # Loan Prediction Logic
    # --------------------------

    if cibil >= 750 and income >= 50000 and credit_history == "1":
        prediction = "Loan Approved ✅"
        color = "success"

    elif cibil >= 650:
        prediction = "Loan Under Review 🟡"
        color = "warning"

    else:
        prediction = "Loan Rejected ❌"
        color = "danger"

    # Save history
    history_data.append({
        "name": name,
        "income": income,
        "loan": loan,
        "cibil": cibil,
        "prediction": prediction
    })

    return render_template(
        "result.html",
        name=name,
        gender=gender,
        age=age,
        income=income,
        loan=loan,
        cibil=cibil,
        prediction=prediction,
        color=color
    )


# ==========================
# HISTORY PAGE
# ==========================
@app.route('/history')
def history():
    return render_template(
        "history.html",
        history=history_data
    )


# ==========================
# RUN APPLICATION
# ==========================
if __name__ == "__main__":
    app.run(debug=True)