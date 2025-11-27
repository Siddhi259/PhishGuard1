# PhishGuard1

🔒🌐 Phishing Website Detection System

📘 Introduction

Phishing attacks are one of the most common cybersecurity threats, tricking users into revealing sensitive information. This project aims to build a Machine Learning–powered Phishing Website Detection System that predicts whether a website is legitimate or phishing based on URL and webpage features.
Using Python and ML algorithms, the project analyzes patterns commonly found in phishing URLs to ensure safer browsing and awareness in the cyber world.

📁 Project Structure
📦 Phishing-Website-Detector
│
├── 📄 Phishing URL.csv              → Dataset used for training/testing
├── 📂 src/
        │     ├── feature_extraction.py → Extracts URL features
        │     ├── model_training.py     → ML model training script
        │     ├── predict.py            → URL prediction script
│
├── 📂 web_app/
         │     ├── app.py                → Flask web application
         │     ├── templates/            → HTML templates for UI
         │     ├── static/               → CSS & JS files
│
├── 📄 requirements.txt         → Dependencies
├── 📄 README.md                → Project documentation
├── 📄 LICENSE                  → License info

⭐ Features

🔍 Real-time URL analysis
🧠 Machine Learning–based classification
📊 Feature extraction from URL and domain properties
🌐 Simple Flask web interface for predictions
📁 Clean and modular code structure
⚡ Fast, lightweight & beginner-friendly
🛠️ Technologies Used
🐍 Python
📦 Pandas / NumPy
🤖 Scikit-Learn (ML Models)
🔗 Regex for URL parsing
🌐 Flask (Web App)
📝 Jupyter Notebook (Model experiments)

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/yourusername/phishing-website-detector.git
cd phishing-website-detector

2️⃣ Install Required Packages
pip install -r requirements.txt

3️⃣ Train the Model
python src/model_training.py

4️⃣ Run the Web App
cd web_app
python app.py


Visit: http://127.0.0.1:5000/
 🚀

📄 License

This project is licensed under the MIT License — feel free to use, modify, and distribute it responsibly.

💡 Inspiration

This project was inspired by the growing number of cyber attacks and the need for simple tools that help people stay safe online.
The idea came from observing how phishing websites cleverly mimic legitimate ones, motivating the creation of a system that detects such patterns automatically using Machine Learning.
