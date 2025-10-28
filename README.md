# 🔧 Backtest Automation for Machine Diagnostics

This project automates the **AI backtesting process** for machine condition diagnostics.  
It fetches **pre-test** and **post-test** data from a remote API, compares diagnostic results, and generates a **multi-level Excel report** with visual validation highlights.

---

## Features

- Fetch machine diagnostic data from a remote API (`Seenous` / `MachWise`)
- Compare **pre** and **post backtest** results
- Automatically generate a **multi-level Excel file** with:
  - AI and human validation comparison
  - Fault mode intensity and probability
  - Visual color coding for failed validations
  - Grouped machine rows with dashed separators
- Local JSON caching for debugging and offline analysis

---

## Project Structure

```
project/
│
├── backtest_automation.py     # Main script (contains all functions)
├── requirements.txt           # Python dependencies
├── data/
│
└── output/
    └── backtest_report.xlsx   # Generated Excel report
```

---

## Installation

### 1️Clone the repository
```bash
git clone https://github.com/yourusername/backtest-automation.git
cd backtest-automation
```

### 2️Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Run the full automation:

```python
from backtest_automation import BackTestAuto

BackTestAuto(
    company_id="YOUR_COMPANY_ID",
    company_domain_before_backtest="before_domain",
    company_domain_after_backtest="after_domain",
    output_path="/path/to/output/report.xlsx"
)
```

This will:
1. Fetch pre/post diagnostic data via API  
2. Generate a detailed Excel file with AI vs. Human validation results  
3. Apply full formatting (color coding, merged cells, summaries)

---

## Example Excel Output

The generated Excel report contains:
- **AI Model Predictions**  
- **Human Validation Results**  
- **Intensity Changes (Δ Probability)**  
- **Validation Status (% True)**  
- **Machine-Level Grouping**  

---

## Functions Overview

| Function | Description |
|-----------|--------------|
| `GetMachineInformation` | Fetch machine point information from API |
| `GetCompanyData` | Retrieve diagnostic data for a specific company |
| `_extract_chart_key` | Extracts normalized chart identifiers |
| `_generate_base_rows` | Builds baseline “Healthy” rows for all machine parts |
| `_update_with_records` | Updates baseline rows with real pre/post diagnostic data |
| `_create_dataframe` | Builds a structured DataFrame with multi-level headers |
| `_format_excel` | Styles and formats the Excel output (colors, borders, widths) |
| `build_excel_multilevel` | Core pipeline to generate the final Excel |
| `BackTestAuto` | Master function to run the full backtest automation |

---

## Requirements

```
openpyxl>=3.1.0
pandas>=2.0.0
numpy>=1.24.0
requests>=2.31.0
machwise>=1.0.0
```

---


## Notes

- API keys used in the script (`api-key`) should be secured in environment variables for production use.  
- File paths in the code (like `Desktop/CeeNous/...`) should be updated to your local directory.

---

