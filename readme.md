# 📩 Naive Bayes SMS Spam Classifier

This project is an **SMS Spam Classifier** built using a **Naive Bayes** machine learning model. It uses a dataset of SMS messages to train and predict whether a message is **Spam** or **Not Spam**. The project includes a **Flask web app** for user interaction.

## 🚀 Features
- 📧 Naive Bayes model for spam detection
- 🧹 Data preprocessing for text messages
- 🌐 Flask web interface for real-time predictions
- ☁️ Deployment-ready for Render, Heroku, or AWS

## 📂 Project Structure
```
naive-bayes-sms-classifier/
│── app.py                  # Flask web application
│── model.ipynb              # Jupyter notebook for training
│── naive_bayes_spam.pkl     # Saved trained model
│── spam.csv                 # Dataset of SMS messages
│── requirements.txt         # Python dependencies
│── static/
│     └── style.css          # Styling for the app
│── templates/
│     └── index.html         # HTML template
│── README.md                # Project documentation
```

## ⚡ Setup
1. **Clone the repository** and navigate to the project directory:
   ```bash
   git clone https://github.com/your-username/naive-bayes-sms-classifier.git
   cd naive-bayes-sms-classifier
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Train the model (optional):**
   - Open `model.ipynb` and run all cells to retrain and save the model as `naive_bayes_spam.pkl`.
4. **Run the web app:**
   ```bash
   python app.py
   ```
   Access it at → `http://127.0.0.1:5000/`

## 🧑‍💻 Usage
- Enter an SMS message in the web app
- Click **Predict** to see if it’s **Spam** or **Not Spam**

## 🖼️ App Preview

<img width="1361" height="625" alt="Screenshot 2025-08-05 150554" src="https://github.com/user-attachments/assets/49122695-4d2e-4d75-91da-0f97ae75dee9" />
