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
├── main.py                           # Main scraping script (loop + export)
├── credential.example.py             # Example credentials file
├── credential.py                     # Your actual API key (not tracked)
├── output/
│   └── linkedin_profile_dataset.json        # Full dataset
│   └── linkedin_profile_dataset_test.json   # One profile (from test run)
└── README.md
```

---

##  Usage

### 1. Setup your API key
Copy the example credentials file:

```bash
cp credential.example.py credential.py
```
Edit `credential.py` and paste your API key:
```python
x_api_key = "paste your api key here"
```
### 2. Choose your target company and set result limits

#### Target company 
We have "Apple In." as default company in the project.
Feel free to change your target by editing in `main.py` 

```python
COMPANY = "Apple Inc."  
```

#### Limit Google results

Google Search can return several results and pages.
To control scraping depth and speed, adjust the following:


```python
PAGE_RANGE = 2     # set the number of google page result Scrape
LIMIT = 20         # set maximum link to get in one page
```

### 3. Run the pipeline
```bash
python main.py
```

This will:
- Scrape search results for `Apple Inc.` profiles
- Fetch profile details
- Export them into `output/linkedin_profile_dataset.json`

### 4. Test a single profile (optional)
```python
from main import test
test()
```

---

## Customization

- Tweak the Dork query to target different company or specify roles to search for.

---

## Legal note

This project is for **educational purposes**. Always check the legality and terms of service before scraping any website or using third-party APIs.
