# LinkedIn_company_employee_scrap
Scrap profile data and build a company employee dataset from LinkedIn using Google Dork and Piloter APIs.


# LinkedIn Scraper - Piloterr API

This project demonstrates how to use the [Piloterr API](https://piloterr.com/) to:
- Perform advanced Google searches using dorks
- Extract LinkedIn profile links from search results
- Retrieve detailed profile information
- Build and export a clean JSON dataset

---

## Requirements

- Python 3.7+
- `requests` module
- A valid `x-api-key` from [Piloterr](https://piloterr.com/)

Install dependencies:

```bash
pip install requests
```

---

##  File structure

```
project/
├── main.py                         # Main scraping script (loop + export)
├── credential.py                   # Your API key (variable: x_api_key)
├── output/
│   └── linkedin_profile_dataset.json     # Full dataset
│   └── linkedin_profile_dataset_test.json # One profile (from test)
└── README.md
```

---

##  Usage

### 1. Setup your API key
Create a file named `credential.py`:
```python
x_api_key = "your_api_key"
```

### 2. Run the pipeline
```bash
python main.py
```

This will:
- Scrape search results for `Apple Inc.` profiles
- Fetch profile details
- Export them into `output/linkedin_profile_dataset.json`

### 3. Test a single profile (optional)
```python
from main import test
test()
```

---

## Customization

- Modify `COMPANY` in `main.py` to change the target company.
- Adjust `PAGE_RANGE` to fetch more pages from Google results.
- Tweak the Dork query to target different platforms or filters.

---

## Legal note

This project is for **educational purposes**. Always check the legality and terms of service before scraping any website or using third-party APIs.
