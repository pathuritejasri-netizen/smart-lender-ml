# 💙 Smart Lender – Loan Eligibility Prediction System

An AI-powered Machine Learning web application designed to predict loan eligibility based on applicant information. Built using **Python**, **Flask**, **Scikit-learn**, and **XGBoost**, the system helps financial institutions make faster, data-driven lending decisions.

## 📌 Features

- 🏦 **Loan Eligibility Prediction:** Predicts whether a loan application is likely to be approved.
- 🤖 **Multiple ML Models:** Implements Decision Tree, Random Forest, K-Nearest Neighbors (KNN), and XGBoost classifiers.
- 📊 **Data Visualization:** Interactive analysis using Matplotlib and Seaborn.
- 🧹 **Data Preprocessing:** Handles missing values, feature encoding, and data cleaning.
- ⚡ **Real-Time Predictions:** Flask-based web interface for instant loan eligibility checks.
- 📱 **Responsive User Interface:** Simple and user-friendly design accessible across devices.
- 🔒 **Secure Model Integration:** Uses a trained and serialized ML model for reliable predictions.
- 🛡️ **Error Handling:** Validates user input and prevents application failures.

---

# 🏗️ Project Architecture

```
User
   ↓
Flask Web Interface
   ↓
Python Backend (Preprocessing & Prediction)
   ↓
Trained XGBoost Model
   ↓
Loan Eligibility Result
```

---

# 📂 Project Structure

```
Smart_Lender/
│
├── dataset/                 # Loan dataset
├── models/                  # Trained ML model (.pkl)
├── static/                  # CSS, Images
├── templates/               # HTML templates
├── app.py                   # Flask application
├── train_model.py           # Model training script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.9+ | Core Programming Language |
| Flask | Web Application Framework |
| NumPy | Numerical Computing |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning Models |
| XGBoost | Final Prediction Model |
| Matplotlib | Data Visualization |
| Seaborn | Exploratory Data Analysis |
| Git & GitHub | Version Control |

---

# 🚀 Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Lender.git
cd Smart-Lender
```

### Create and Activate Virtual Environment

**Windows**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model (Optional)

```bash
python train_model.py
```

---

# ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 📊 Model Performance

| Model | Test Accuracy |
|--------|--------------|
| Decision Tree | Good |
| Random Forest | Better |
| K-Nearest Neighbors (KNN) | Moderate |
| ⭐ XGBoost | **81.1% (Best Model)** |

---

# 🌟 Future Enhancements

- 📈 Credit Score Integration
- 🌐 Cloud Deployment (IBM Cloud/AWS/Azure)
- 📱 Mobile-Friendly Interface
- 🔔 Loan Recommendation System
- 📊 Admin Dashboard for Loan Analytics
- 🤖 Explainable AI (Feature Importance & SHAP)

---

# 👨‍💻 Team

**Pathuri Tejasri** *(Team Lead)*
pathuritejasri@gmail.com
GitHub: 

**Hima Bindu Mareedu**
bindu.mareedu2004@gmail.com

**Raghava Garlapati**
raghavagarlapati379@gmail.com

**Haneef Jani Shaik**
skhaneef023@gmail.com

**Triveni Thumarada**
trivenithumarada@gmail.com

---

# 📜 License

This project was developed for educational purposes as part of the AI/ML and Machine Learning learning track.
