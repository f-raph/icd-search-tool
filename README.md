# ICD Search Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightblue.svg)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-purple.svg)](https://getbootstrap.com/)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](#)

The **ICD Search Tool** is a lightweight web application that allows healthcare professionals to quickly search for diseases and corresponding ICD codes using intelligent fuzzy search. Doctors can select a diagnosis, create a treatment plan, save it to a patient record, and export the patient's data for further processing (e.g., pharmacy, insurance, or EHR systems).
**Link**: https://icd-search-tool-hqq8.onrender.com/

---

## 🚀 Features

- 🔍 **Fuzzy Search** for disease names (handles typos like "pnik" → "pink eye")
- 📋 **Direct ICD Code Search** (enter part of ICD code, e.g., "372.05")
- 📝 **Treatment Plan Input** for each selected diagnosis
- 💾 **Save Diagnoses** to patient record
- 📤 **Export Patient Data** as a JSON file
- ⚡ **Responsive UI** with Bootstrap 5 styling
- 🌐 **Built with** Python (Flask) + HTML/CSS/JavaScript

---

## 📂 Project Structure

```
icd-search-tool/
│
├── static/
│   ├── css/
│   │   └── style.css          # Custom styling
│   └── js/
│       └── app.js             # Frontend logic (search, save, export)
│
├── templates/
│   └── index.html             # Main web page
│
├── data/
│   └── icd_data.json          # Disease names and ICD codes
│
├── saved_patients/            # Exported patient data (auto-created)
│
├── app.py                     # Flask backend server
├── README.md                  # Project description (this file)
├── requirements.txt           # Python dependencies
└── .gitignore                 # Ignored files (optional)
```

---

## 🛠️ How to Run Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/icd-search-tool.git
   cd icd-search-tool
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # OR
   source venv/bin/activate # macOS/Linux
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**:

   ```bash
   python app.py
   ```

5. **Open your browser** and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🧠 Tech Stack

- **Frontend**: HTML5, CSS3 (Bootstrap 5), JavaScript
- **Backend**: Python 3 (Flask)
- **Search Engine**: RapidFuzz for fuzzy matching
- **Database**: JSON file (local ICD database)

---

## 📈 Future Improvements

- 🔒 Add user authentication (doctors login before accessing)
- 🗂️ Support multiple patients and records
- 🌍 Multi-language support for disease names
- 📑 PDF export option for patient records
- 💬 Auto-complete suggestions based on common searches

---

## 🤝 Contributing

Contributions are welcome!  
If you find a bug or have a feature request:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Open a Pull Request

---

## 📝 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 📣 Acknowledgements

- [RapidFuzz](https://github.com/maxbachmann/RapidFuzz) for fuzzy search capabilities
- [Bootstrap](https://getbootstrap.com/) for responsive UI components

---
