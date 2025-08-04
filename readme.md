# Naive Bayes SMS Spam Classifier

This project is an SMS spam classifier built using a Naive Bayes model. It uses a dataset of SMS messages to train a model that can predict whether a message is spam or not. The project includes a Flask web app for user interaction.

## Project Structure

- `app.py` — Flask web application for spam prediction
- `model.ipynb` — Jupyter notebook for data analysis and model training
- `naive_bayes_spam.pkl` — Saved trained model
- `spam.csv` — Dataset of SMS messages
- `requirements.txt` — Python dependencies
- `static/style.css` — CSS for the web app
- `templates/index.html` — HTML template for the web app

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Train the model (optional):**
   - Open `model.ipynb` and run all cells to retrain and save the model as `naive_bayes_spam.pkl`.

4. **Run the web app:**
   ```
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Usage

- Enter an SMS message in the web app to check if it is spam or not.

## License

This project is for educational purposes.