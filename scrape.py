import os
from bs4 import BeautifulSoup
import re
import json

def load_html_file(file_path):
    """Load and parse the HTML file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return BeautifulSoup(file.read(), 'html.parser')

def extract_disease_info(soup):
    """Extract disease information and ICD-10 codes from the HTML."""
    diseases = {}
    
    # Get all text from the HTML
    text_content = soup.get_text()
    
    # Find all ICD codes (format: XXX.XX)
    icd_pattern = r'(\d{3}\.\d{1,2})'
    matches = re.finditer(icd_pattern, text_content)
    
    for match in matches:
        icd_code = match.group(1)
        
        # Get text around the code (200 chars before and after)
        start = max(0, match.start() - 200)
        end = min(len(text_content), match.end() + 200)
        context = text_content[start:end]
        
        # Try to find a disease name (capitalized words)
        name_match = re.search(r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', context)
        if name_match:
            disease_name = name_match.group(1)
        else:
            # Fallback: use text before the code
            disease_name = context.split(icd_code)[0].strip().split('\n')[-1].strip()
        
        # Clean up the name
        disease_name = re.sub(r'\d+', '', disease_name).strip()
        
        diseases[disease_name] = {
            'code': icd_code,
            'description': disease_name
        }
    
    return diseases

def create_simple_mapping(diseases):
    """Create a simple mapping of target diseases to their ICD codes."""
    # Target diseases and their keywords
    target_diseases = {
        'Pink Eye': ['pink eye', 'conjunctivitis', 'conjunctival', 'eye infection'],
        'Dry Eye': ['dry eye', 'keratoconjunctivitis sicca', 'dry eye syndrome'],
        'Conjunctivitis': ['conjunctivitis', 'conjunctival', 'pink eye'],
        'Stroke': ['stroke', 'cerebrovascular', 'CVA', 'cerebral infarction']
    }
    
    # Default codes if no match is found
    default_codes = {
        'Pink Eye': '077.0',
        'Dry Eye': '375.1',
        'Conjunctivitis': '077.0',
        'Stroke': '434.9'
    }
    
    # Create the mapping
    simple_mapping = {}
    
    for disease, keywords in target_diseases.items():
        # Find matching diseases
        matches = []
        for name, info in diseases.items():
            if any(keyword.lower() in name.lower() for keyword in keywords):
                matches.append(info)
        
        # Use the first match or default code
        if matches:
            simple_mapping[disease] = {
                'code': matches[0]['code'],
                'description': matches[0]['description']
            }
        else:
            simple_mapping[disease] = {
                'code': default_codes[disease],
                'description': disease
            }
    
    return simple_mapping

def save_results(mapping, output_file):
    """Save the results to a JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=4)

def main():
    # File paths
    html_file = 'diagnosistable.html'
    output_file = 'disease_mapping.json'
    
    try:
        # Process the data
        soup = load_html_file(html_file)
        diseases = extract_disease_info(soup)
        simple_mapping = create_simple_mapping(diseases)
        
        # Save results
        save_results(simple_mapping, output_file)
        print(f"Results have been saved to {output_file}")
        
        # Print summary
        for disease, info in simple_mapping.items():
            print(f"\n{disease}:")
            print(f"- {info['description']} (Code: {info['code']})")
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please make sure the file 'diagnosistable.html' exists in the same directory as this script.")

if __name__ == "__main__":
    main()
