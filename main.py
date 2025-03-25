from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import random
import numpy as np
from tensorflow.keras.models import load_model
import pandas as pd
import joblib

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mybank.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    __tablename__ = 'user'  # Explicitly define table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Load the trained model and preprocessors
class ModelLoader:
    def __init__(self):
        self.model = load_model('models/fraud_detection.h5')
        self.encoders = {
            'category': joblib.load('models/category_encoder.pkl'),
            'gender': joblib.load('models/gender_encoder.pkl'),
            'job': joblib.load('models/job_encoder.pkl'),
            'trans_num': joblib.load('models/trans_num_encoder.pkl'),
        }

    def encode_feature(self, feature_name, value):
        return self.encoders[feature_name].transform([value])[0]

    def predict(self, data):
        return self.model.predict(data)

model_loader = ModelLoader()

# Create database tables
with app.app_context():
    db.create_all()
    print("Database tables created successfully")

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already exists. Please use a different one.', 'error')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# Protected routes (require login)
@app.route('/accounts')
def accounts():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))
    return render_template('accounts.html')

@app.route('/transfer')
def transfer():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))
    return render_template('transfer.html')

@app.route('/payments')
def payments():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))
    return render_template('payments.html')

@app.route('/security')
def security():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))
    return render_template('security.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            # Generate random values for certain fields
            transaction_data = {
                'unname': random.randint(1000000000000000, 9999999999999999),
                'trans_date_trans_time': datetime.datetime.now(),
                'cc_num': random.randint(698585855, 8525629555262625),
                'zip_code': random.randint(20000, 80000),

                # Form inputs
                'category': model_loader.encode_feature('category', request.form['category']),
                'amt': float(request.form['amount']),
                'gender': model_loader.encode_feature('gender', request.form['gender']),
                'lat': float(request.form['user_lat']),
                'long': float(request.form['user_long']),
                'job': model_loader.encode_feature('job', request.form['job']),
                'trans_num': model_loader.encode_feature('trans_num', request.form['transaction_number']),
                'merch_lat': float(request.form['merch_lat']),
                'merch_long': float(request.form['merch_long']),
                'city_pop': random.randint(48, 85895),
            }

            # Create DataFrame
            data = pd.DataFrame([list(transaction_data.values())],
                                columns=list(transaction_data.keys()))
            data['trans_date_trans_time'] = data['trans_date_trans_time'].astype(np.int64)

            # Make prediction
            prediction = model_loader.predict(data)

            # Store prediction data in session
            session['prediction_data'] = {
                'prediction': float(prediction[0]),
                'transaction_amount': transaction_data['amt'],
                'merchant_name': request.form['merchant_name']
            }

            return redirect(url_for('result'))

        except Exception as e:
            return render_template('error.html', error=str(e))

    return redirect(url_for('form'))

@app.route('/result')
def result():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))

    data = session.get('prediction_data', {})
    return render_template('result.html', **data)

if __name__ == '__main__':
    app.run(debug=True, port=5800)