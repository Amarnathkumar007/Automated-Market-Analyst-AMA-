# SnapHomz Market Intelligence Platform 🏡📈

An automated, end-to-end real estate reporting pipeline designed to empower agents with hyperlocal market data. SnapHomz seamlessly integrates live property metrics, Generative AI narratives, and branded PDF generation into a single, cohesive workflow.

## 🌟 Overview

Real estate agents need to provide constant value to their clients, but manually pulling data, writing market analyses, and designing branded reports takes hours. 

**SnapHomz** solves this by automating the entire process:
1. Pulls live property and market data.
2. Leverages an LLM to write a personalized, insightful market narrative.
3. Generates a beautifully styled, co-branded PDF report with the agent's headshot and contact information.
4. *Ready in under 90 seconds.*

---

## 🛠️ Architecture & Step-by-Step Workflow

This project is built using a modular, service-oriented architecture in Python.

### 1. Data Ingestion (`api_request.py`)
The system queries the **RealEstateAPI** (`PropertyDetail` endpoint) using a specific property address and zip code. It parses the complex JSON response to extract only the most critical, actionable metrics:
* Median Home Price / Estimated Value
* Average Days on Market
* List-to-Sale Price Ratio

### 2. Generative AI Narrative (`gemini.py`)
Using the **Google GenAI SDK** (`gemini-2.5-flash`), the extracted metrics are fed into a finely-tuned prompt. The AI acts as a seasoned real estate analyst, synthesizing the raw numbers into a fluent, professional narrative that explains *what the data means* for prospective buyers and sellers in that specific zip code.

### 3. Data Aggregation (`app.py`)
The main orchestrator script. It reads the agent's branding profile (name, contact info, base64 encoded logos/headshots) from `agent.json`, aggregates the API market data, and calls the PDF generation module.

### 4. Template Rendering & PDF Generation (`generate_pdf.py`)
Using **Jinja2**, the system injects the agent profile, market metrics, and AI narrative into a custom HTML/CSS template. Finally, **xhtml2pdf** converts this responsive HTML directly into a premium, styled PDF document—complete with navy accent bars, circular profile pictures, and color-coded data tables.

---

## 🚀 How to Run Locally

Follow these steps to set up the environment and generate your first SnapReport.

### Prerequisites
* Python 3.8+
* A valid Google Gemini API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/snaphomz.git
   cd snaphomz
   ```

2. **Create and activate a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install requests google-genai xhtml2pdf jinja2 python-dotenv
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Configure Agent Profile**
   Ensure `agent.json` is populated with the target address, agent details, and base64-encoded images for the logo and profile picture.

### Execution

Run the main orchestrator script:
```bash
python app.py
```

**Output:**
* The script will print the AI-generated narrative to the console.
* A beautifully formatted PDF file (e.g., `SnapReport_90210.pdf`) will be instantly generated and saved in the project root.

---

## 💡 Future Enhancements
* **CRON Scheduling:** Implement automated monthly execution to batch-generate and email reports to an agent's CRM mailing list.
* **Expanded Metrics:** Integrate a broader Market Trends API to include "Months of Inventory" and "New Listings" at the zip-code level.
* **Dynamic Charting:** Add Python `matplotlib` or `plotly` to generate visual graphs of price trends and embed them dynamically into the HTML template before PDF conversion.

---
*Developed for modern real estate professionals.*
