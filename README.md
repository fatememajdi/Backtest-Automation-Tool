# Backtest Automation Tool

This script is designed to **compare diagnostic results before and after a Backtest** in industrial monitoring systems.  
The output is an Excel file with multi-level columns showing detailed validation status between the two datasets.

---

## Project Structure

```
.
├── backtest_auto.py          # Main code including data fetching and Excel generation
├── requirements.txt          # Python dependencies (if needed)
└── README.md                 # Project documentation
```

---

## How It Works

### 1. Fetching Data

The `GetCompanyData` function retrieves raw diagnostic data from the server using the API:

```python
GetCompanyData(company_id, domain, company_domain)
```

The output contains diagnostic information for each machine over different time periods.

---

### 2. Comparing Pre- and Post-Backtest Data

The main function `build_excel_multilevel` compares pre-test (`pre_json`) and post-test (`post_json`) data.  
The comparison is performed in three areas:

| Comparison | Description |
|------------|------------|
| **Failure Validation** | Checks whether the failure diagnosis matches before and after Backtest |
| **Human Evaluation Validation** | Checks if the probability difference is within ±15% |
| **Worst Signal Validation** | Checks signal similarity based on key parts of the ChartPlot filename |

If **Failure Validation** is `False`, the other validations are automatically set to `False`.

---

### 3. Extracting ChartPlot Keys

The `_extract_chart_key` function extracts key components from a ChartPlot filename:

```
01EPU01310300-13-M-1-H-(2025-09-29 10-30-00)-healthy-1760946281359.gz
```

Output: `M-1-H`  
Only these key parts are used for comparison, ignoring timestamps or unique IDs.

---

### 4. Generating the Excel File

The data is saved in an Excel file with **multi-level columns (MultiIndex)**:

| Machine | Failure Mode | Part | Point/Spare | Date | Prediction | Failure Validation | Failure Description | Human Eval Validation | Human Eval Description | Worst Signal Validation | Worst Signal Description |
|----------|---------------|------|--------------|------|-------------|--------------------|---------------------|-----------------------|------------------------|--------------------------|---------------------------|

The file is saved to the `output_path` provided to the function.

---

##  How to Run

```python
from backtest_auto import BackTestAuto

BackTestAuto(
    company_id="123",
    company_domain_before_backtest="before_domain",
    company_domain_after_backtest="after_domain",
    output_path="/path/to/output.xlsx",
    domain="20.108.64.195"
)
```

---

##  Dependencies

Make sure to install the following Python packages:

```bash
pip install requests pandas numpy openpyxl
```

---

##  Main Functions

| Function | Purpose |
|----------|---------|
| `GetCompanyData` | Fetches diagnostic data from the server |
| `_normalize` | Cleans strings by trimming spaces and replacing None with empty string |
| `_extract_chart_key` | Extracts key parts (e.g., M-1-H or PUMP-4-H) from ChartPlot filenames |
| `find_post_entry` | Finds corresponding post-test record |
| `build_excel_multilevel` | Generates the Excel report comparing pre- and post-test data |
| `BackTestAuto` | Runs the full process: fetch → compare → Excel |

---

##  Notes

- If the server response is invalid JSON, `GetCompanyData` returns `None`.  
- If pre-test or post-test data is missing, the report will not be generated.  
- Probability values that are not numeric are replaced with `NaN`.  
- Probability differences above 15% cause Human Validation to be `False`.

---

##  Example Output

| Machine | Failure Mode | Part | Point | Date | Prediction | Failure (Validation) | Human Eval (Validation) | Worst Signal (Validation) |
|----------|---------------|------|--------|------|-------------|----------------------|-------------------------|---------------------------|
| 01EPU01310300-13 | Bearing Failure | Pump | 3 | 2025-09-29 | Faulty |  True |  True |  True |
| 01EPU01310300-06 | Bearing Failure | Pump | 4 | 2025-09-29 | Faulty |  False |  False |  False |

---

