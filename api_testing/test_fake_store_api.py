import pytest
import requests
from typing import List, Dict, Any

BASE_URL = "https://fakestoreapi.com/products"

def get_products() -> List[Dict[str, Any]]:
    """Fetch products from the API."""
    response = requests.get(BASE_URL)
    return response.json()

def test_response_status_code():
    """Test that the API returns a 200 status code."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_product_title_not_empty():
    """Test that all products have non-empty titles."""
    products = get_products()
    products_with_empty_titles = [
        product for product in products 
        if not product.get('title') or product['title'].strip() == ''
    ]
    assert len(products_with_empty_titles) == 0, \
        f"Found {len(products_with_empty_titles)} products with empty titles"

def test_product_price_not_negative():
    """Test that all products have non-negative prices."""
    products = get_products()
    products_with_negative_prices = [
        product for product in products 
        if product.get('price', 0) < 0
    ]
    assert len(products_with_negative_prices) == 0, \
        f"Found {len(products_with_negative_prices)} products with negative prices"

def test_rating_rate_not_exceed_five():
    """Test that all product ratings do not exceed 5."""
    products = get_products()
    products_with_invalid_ratings = [
        product for product in products 
        if product.get('rating', {}).get('rate', 0) > 5
    ]
    assert len(products_with_invalid_ratings) == 0, \
        f"Found {len(products_with_invalid_ratings)} products with ratings exceeding 5"

def test_generate_defect_report():
    """Generate a report of all products with defects."""
    products = get_products()
    defects = []
    
    for product in products:
        product_defects = []
        
        # Check title
        if not product.get('title') or product['title'].strip() == '':
            product_defects.append("Empty title")
            
        # Check price
        if product.get('price', 0) < 0:
            product_defects.append("Negative price")
            
        # Check rating
        if product.get('rating', {}).get('rate', 0) > 5:
            product_defects.append("Rating exceeds 5")
            
        if product_defects:
            defects.append({
                'id': product.get('id'),
                'title': product.get('title'),
                'defects': product_defects
            })
    
    # Print the defect report
    if defects:
        print("\nProducts with defects:")
        for defect in defects:
            print(f"\nProduct ID: {defect['id']}")
            print(f"Title: {defect['title']}")
            print("Defects:", ", ".join(defect['defects']))
    
    return defects 