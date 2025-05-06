# Fake Store API Test Suite

This test suite validates the data provided by the Fake Store API (https://fakestoreapi.com/products) to detect errors and anomalies.

## Test Objectives

1. Verify server response code (expected 200)
2. Confirm the presence and validity of product attributes:
   - `title` (name) - must not be empty
   - `price` - must not be negative
   - `rating.rate` - must not exceed 5
3. Generate a list of products containing defects

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

To run all tests:
```bash
pytest test_fake_store_api.py -v
```

To run tests with HTML report:
```bash
pytest test_fake_store_api.py --html=report.html
```

## Test Structure

- `test_response_status_code()`: Verifies the API returns a 200 status code
- `test_product_title_not_empty()`: Checks for empty product titles
- `test_product_price_not_negative()`: Validates product prices are non-negative
- `test_rating_rate_not_exceed_five()`: Ensures ratings don't exceed 5
- `test_generate_defect_report()`: Generates a detailed report of all products with defects

## Output

The test suite will:
1. Run all validation tests
2. Generate a detailed report of any products with defects
3. Create an HTML report (if specified) with test results 