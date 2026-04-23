import json
import response_utils
import product_data


def handler(event, context):
    try:
        product_id = event.get('pathParameters', {}).get('id')

        if not product_id:
            return response_utils.create_response(400, {"error": "Product ID required"})

        product = product_data.get_product(product_id)
        if not product:
            return response_utils.create_response(404, {"error": "Product not found"})

        return response_utils.create_response(200, product)

    except json.JSONDecodeError:
        return response_utils.create_response(400, {"error": "Invalid JSON"})
    except Exception as e:
        print(f"Error: {str(e)}")
        return response_utils.create_response(500, {"error": "Internal server error"})
