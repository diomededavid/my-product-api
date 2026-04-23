# In-memory product catalog (replace with DynamoDB in production)
products = {
    "prod_123": {"id": "prod_123", "name": "Wireless Headphones", "price": 199.99},
    "prod_456": {"id": "prod_456", "name": "USB-C Cable", "price": 12.99}
}

def get_product(product_id):
    return products.get(product_id)

def get_all_products():
    return list(products.values())

def get_products_by_category(category):
    # Simplified example - actual implementation would filter by category
    return list(products.values())
