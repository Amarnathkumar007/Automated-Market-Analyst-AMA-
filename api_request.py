import requests

def call_api(HOUSE, STREET, PIN_CODE):
    url = "https://api.realestateapi.com/v2/PropertyDetail"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": "AMAR-cf05-8d07-0646-243aba899c2f",
        "x-user-id": "test-user"
    }

    # payload = {
        
    #     "house": "17",
    #     "street": "Topeka Pass",
    #     # "city": "Willingboro", //optional
    #     # "state": "NJ",  //optional
    #     "zip": "08046"
    # }
    payload={
        "house":HOUSE,
        "street":STREET,
        "zip":PIN_CODE
    }
    response = requests.post(
        url,
        headers=headers,
        json=payload
    )
    return response.json()
# print(response.status_code)
# print(response.text)

def extract_property_metrics(payload):
    # Access the main data block
    data_block = payload.get("data", {})
    input_block = payload.get("input", {})
    mls_history = data_block.get("mlsHistory", [])
    
    # Extract the requested metrics
    # City lives in data.propertyInfo.address.city
    property_info = data_block.get("propertyInfo", {})
    city = (
        property_info.get("address", {}).get("city")
        or input_block.get("city")
    )
    metrics = {
        "city": city,
        "address": input_block.get("address"),
        "property_price": data_block.get("mlsListingPrice"),
        "estimated_value": data_block.get("estimatedValue"),
        "days_on_market": data_block.get("mlsDaysOnMarket"),
        "listing_date": data_block.get("mlsListingDate"),
        "current_status": data_block.get("mlsStatus"),
        "months_owned": data_block.get("ownerInfo", {}).get("ownershipLength")
    }
    
    # Calculate list price ratio if history exists
    if len(mls_history) >= 2:
        current_price = mls_history[0].get("price")
        original_price = mls_history[1].get("price")
        if original_price:
            metrics["price_drop_ratio"] = round((current_price / original_price) * 100, 2)
    else:
        metrics["price_drop_ratio"] = 100.0
        
    return metrics

# Example usage with your payload:
# result = extract_property_metrics(your_json_data)
# print(result)
    
    # return market_data
