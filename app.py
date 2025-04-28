from flask import Flask, render_template, request, jsonify
import json
import os
from rapidfuzz import process, fuzz

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

    if not query:
        return jsonify({"results": results})

    # Prepare disease name list
    disease_names = list(icd_data.keys())

    # Fuzzy match disease names
    disease_matches = process.extract(query, disease_names, scorer=fuzz.WRatio, limit=10)

    # Add diseases matching fuzzily
    for disease, score, _ in disease_matches:
        if score >= 60:  # Only accept good matches
            results.extend(icd_data[disease])

    # ALSO search in ICD codes exactly (no fuzzy matching on codes)
    for disease, entries in icd_data.items():
        for entry in entries:
            if query in entry["code"].lower():
                results.append(entry)

    return jsonify({"results": results})

# Add selected diagnosis
@app.route('/api/diagnosis/add/', methods=['POST'])
def add_diagnosis():
    data = request.json
    diagnosis = {
        "icdCode": data.get("icdCode"),
        "diagnosis": data.get("diagnosis"),
        "treatmentPlan": data.get("treatmentPlan") 
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
