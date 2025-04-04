# 🚨 Financial Fraud Detection Using Machine Learning 🚨

## 📖 Project Overview
This project is focused on detecting financial fraud using machine learning models. It offers a complete pipeline starting from data collection and model training to deployment through a Flask web application. The objective is to enable users to input transaction data and receive fraud detection predictions in real-time. The machine learning models are trained in Google Colab and deployed locally using Flask.

---

## 📂 Workflow

### 1. 📅 Dataset Acquisition
- Download the dataset from the following link:
  - [Download CSV](https://drive.google.com/file/d/1k3b2yPQ800ot5djpDNKKGm7IXLwfcTFo/view?usp=drive_link)

### 2. 📚 Model Training (Google Colab)
- Open the `fraud.ipynb` file in Google Colab.
- Upload the CSV dataset.
- Execute each cell in the notebook to clean the data, train the machine learning models, and evaluate performance.

### 3. 🔄 Model Exporting
- Once the models are trained, export and save them as `.h5` (Keras/TensorFlow) or `.joblib` (Scikit-learn).
- Download these files and place them in the `models/` directory inside your local project folder.

### 4. 📝 Project Setup (Local Environment)
- Clone the repository:
  ```bash
  git clone https://github.com/NukaNarendra/FinancialFraudDetectionUsingML
  cd FinancialFraudDetectionUsingML
  ```
- Ensure Python 3.10 or below is installed.

### 5. 📚 Install Required Dependencies
Install the necessary Python libraries using pip:
```bash
pip install flask flask_sqlalchemy werkzeug numpy tensorflow pandas joblib
```

### 6. 🌐 Run the Flask Application
Start the application with:
```bash
python main.py
```
Visit `http://127.0.0.1:5000/` on your browser to access the web interface.

---

## 🛠️ Tech Stack & Tools
- **Programming Language**: Python
- **ML Libraries**: TensorFlow, Scikit-learn, Pandas, NumPy, Joblib
- **Web Framework**: Flask
- **Notebook**: Google Colab
- **Deployment**: Localhost via Flask

---

## 📊 Key Features & Results
- ✅ Trains machine learning models to identify fraudulent financial transactions.
- ✅ Flask web interface for interactive prediction and user input.
- ✅ Real-time fraud detection and result display.
- ✅ Easy-to-use modular structure with pre-trained model integration.

---

## 📁 Folder Structure
```
📂 FinancialFraudDetectionUsingML
├── 📁 instance
├── 📁 static
├── 📁 templates
├── 📁 models             # Folder to store trained model files
├── 📄 README.md
├── 📓 fraud.ipynb        # Google Colab notebook
└── 🐍 main.py            # Flask application
```

---

## 🔒 Prerequisites
- Python 3.10 or lower
- Google Colab for model training
- Flask & Flask_SQLAlchemy
- TensorFlow, Pandas, NumPy, Joblib

---

## 👥 Contribution
Contributions are highly welcome! Feel free to raise issues, suggest improvements, or submit pull requests to enhance the functionality and performance.

---

## 👤 Author
**Nuka Narendra**

---

## 📈 Future Enhancements
- 🔔 Add real-time alerts for detected frauds via email/SMS.
- 🤖 Integrate advanced deep learning models like LSTM or Autoencoders.
- 🔄 Extend deployment to cloud platforms like Heroku or AWS.


