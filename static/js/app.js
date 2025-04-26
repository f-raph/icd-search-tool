// Search diseases or codes
async function searchDiseases(query) {
  if (!query) {
    document.getElementById("searchResults").style.display = "none";
    return;
  }

  try {
    const response = await fetch(
      `/api/search/?query=${encodeURIComponent(query)}`
    );
    const data = await response.json();
    displaySearchResults(data.results);
  } catch (error) {
    console.error("Error searching:", error);
  }
}

// Display search results
function displaySearchResults(results) {
  const searchResults = document.getElementById("searchResults");
  searchResults.innerHTML = "";

  if (results.length === 0) {
    searchResults.style.display = "none";
    return;
  }

  results.forEach((result) => {
    const div = document.createElement("div");
    div.className = "search-result-item";
    div.textContent = `${result.description} (${result.code})`;
    div.addEventListener("click", () => selectDiagnosis(result));
    searchResults.appendChild(div);
  });

  searchResults.style.display = "block";
}

// Select a diagnosis
function selectDiagnosis(result) {
  document.getElementById(
    "diagnosis"
  ).value = `${result.description} (${result.code})`;
  document.getElementById("searchResults").style.display = "none";

  // Save selected diagnosis for adding
  document.getElementById("addBtn").dataset.code = result.code;
  document.getElementById("addBtn").dataset.description = result.description;
}

// Add selected diagnosis to patient record
async function addDiagnosis() {
  const icdCode = document.getElementById("addBtn").dataset.code;
  const diagnosis = document.getElementById("addBtn").dataset.description;

  if (!icdCode || !diagnosis) {
    alert("Please select a diagnosis first!");
    return;
  }

  try {
    const response = await fetch("/api/diagnosis/add/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ icdCode, diagnosis }),
    });

    const data = await response.json();
    alert(data.message);
  } catch (error) {
    alert("Error adding diagnosis: " + error.message);
  }
}

// Export patient data
async function exportPatient() {
  try {
    const response = await fetch("/api/patient/export/");
    const data = await response.json();
    alert(data.message);
  } catch (error) {
    alert("Error exporting patient data: " + error.message);
  }
}

// Setup event listeners
function setupEventListeners() {
  const codeInput = document.getElementById("codeInput");
  const addBtn = document.getElementById("addBtn");
  const exportBtn = document.getElementById("exportBtn");

  let searchTimeout;
  codeInput.addEventListener("input", function (e) {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => searchDiseases(e.target.value), 300);
  });

  addBtn.addEventListener("click", addDiagnosis);
  exportBtn.addEventListener("click", exportPatient);
}

// Initialize
setupEventListeners();
