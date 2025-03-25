# 🚨 Financial Fraud Detection Using ML 🚨

## 📖 Overview
This project focuses on detecting financial fraud by training machine learning models and deploying them using a Flask web application.  
It follows a structured workflow that involves downloading the dataset, training the model in Google Colab, saving models locally, and running the Flask app in your local environment.

---

## 📂 Workflow
✅ **Download the dataset** using the given link:  
🔗 [Download CSV](https://drive.google.com/file/d/1Sk9C5EDnNYXA7-fhmH841ap9RiRJxV2-/view?usp=drive_link)

✅ **Run the Jupyter notebook**:
- 🗒️ Open `fraud.ipynb` in **Google Colab**.
- 📥 Load the downloaded CSV file and execute all cells to train the model.

✅ **Save trained models**:
- 💾 After training, download and save the models (`.h5` or `.joblib` files) into the `models` folder in your local project directory.

✅ **Clone the repository**:
```bash
git clone <repository_url>
cd FinancialFraudDetectionUsingML
```

✅ **Place the saved models** in the `models` folder inside your cloned repository.

✅ **Install required dependencies**:
```bash
pip install flask flask_sqlalchemy werkzeug numpy tensorflow pandas joblib
```
> ⚠ **Make sure you are using Python 3.10 or below for the best performance.**

✅ **Run the Flask application**:
```bash
python main.py
```
- 🌐 The Flask server will start running on your localhost.

---

## 🛠️ Setup and Installation

### 🔎 Prerequisites
- ✅ Python 3.10 or below
- ✅ Google Colab
- ✅ Flask
- ✅ Flask_SQLAlchemy
- ✅ Werkzeug
- ✅ Numpy
- ✅ TensorFlow
- ✅ Pandas
- ✅ Joblib

### ⚙️ Installation
Clone the repository:
```bash
git clone <repository_url>
cd FinancialFraudDetectionUsingML
```
Install the necessary Python libraries:
```bash
pip install flask flask_sqlalchemy werkzeug numpy tensorflow pandas joblib
```

---

## 🚀 Usage

### 1️⃣ Run the Jupyter Notebook (`fraud.ipynb`)
- 📖 Open in Google Colab.
- 📂 Download the CSV file.
- 🤖 Train the models.
- 💾 Save models in `.h5` or `.joblib` formats.

### 2️⃣ Place Trained Models
- 📥 Save the trained model files inside the `models` directory in your local project.

### 3️⃣ Run the Flask App
```bash
python main.py
```
- 🌍 Open the browser and access the app via `localhost`.

---

## 📊 Results
The project will:
- ✅ Allow detection of fraudulent transactions through the Flask web interface.
- ✅ Use trained machine learning models for prediction.
- ✅ Display results dynamically from user input.

---

## 📁 Folder Structure
```
📂 FinancialFraudDetectionUsingML  
 ├── 📁 instance  
 ├── 📁 static  
 ├── 📁 templates  
 ├── 📁 models  
 ├── 📄 README.md  
 ├── 📓 fraud.ipynb  
 └── 🐍 main.py  
```

---

## 🤝 Contributing
Contributions are welcome! ✨  
Feel free to open issues or submit pull requests to enhance the project.

---

## 📜 License
This project is for educational and learning purposes only.

---

## 👤 Author
Developed by **Nuka Narendra** 💡

