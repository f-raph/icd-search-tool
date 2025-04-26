from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load ICD data once
with open('data/icd_data.json', 'r') as f:
    icd_data = json.load(f)

# In-memory patient record
patient_data = {
    "patient_id": "P001",   # (For now, static ID. Later: allow manual input)
    "diagnoses": []
}

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Search endpoint
@app.route('/api/search/', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    results = []

    for disease, entries in icd_data.items():
        if query in disease.lower() or any(query in e["code"] for e in entries):
            results.extend(entries)

    return jsonify({"results": results})

# Add selected diagnosis
@app.route('/api/diagnosis/add/', methods=['POST'])
def add_diagnosis():
    data = request.json
    diagnosis = {
        "icdCode": data.get("icdCode"),
        "diagnosis": data.get("diagnosis")
    }
    patient_data["diagnoses"].append(diagnosis)
    return jsonify({"message": "Diagnosis added successfully"})

# Export patient record
@app.route('/api/patient/export/', methods=['GET'])
def export_patient():
    if not os.path.exists('saved_patients'):
        os.makedirs('saved_patients')

    export_path = f'saved_patients/{patient_data["patient_id"]}_diagnosis.json'
    with open(export_path, 'w') as f:
        json.dump(patient_data, f, indent=4)

    return jsonify({"message": f"Patient data exported to {export_path}"})

if __name__ == '__main__':
    app.run(debug=True)
