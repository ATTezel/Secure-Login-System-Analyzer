# 🔐 Secure Login System Analyzer

A simple web tool to analyze whether a website has implemented secure login practices. This tool checks:

- ✅ HTTPS support and SSL certificate validity  
- 🍪 Secure and HttpOnly cookie flags  
- 📦 HTTP Strict Transport Security (HSTS) header

---

## 📸 Demo

![UI Screenshot](https://your-screenshot-link-here)  
*Replace with your own screenshot of the running app*

---

## 🚀 Features

- SSL/TLS Certificate Validation
- HTTPS Support Detection
- Secure Cookie Flag Detection
- HttpOnly Cookie Flag Detection
- HSTS Header Presence Check

---

## 🧠 Technologies Used

- Python 3.13+
- Flask
- HTML + CSS
- Requests
- SSL, Socket

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/secure-login-analyzer.git
cd secure-login-analyzer
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
▶️ Usage
bash
Copy
Edit
python app.py
Then open your browser and visit:
http://127.0.0.1:5000/

Paste a URL to analyze (e.g. https://example.com) and hit Analyze.

📂 Project Structure
pgsql
Copy
Edit
secure-login-analyzer/
│
├── analysis/
│   ├── https_checker.py
│   ├── cookie_checker.py
│   └── hsts_checker.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
✅ Example Output
yaml
Copy
Edit
URL: https://example.com

🔐 HTTPS Supported: True
📜 Certificate Valid: True
🍪 Cookies Found: True
    - secure flag: ✅
    - HttpOnly flag: ✅
📦 HSTS Enabled: True
🤖 To-Do
Add JavaScript-based live analysis

Add CSP (Content-Security-Policy) header checks

Export reports to PDF

Multi-URL batch scan

📄 License
MIT License – feel free to use, modify, and contribute!

🙌 Contributing
Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

