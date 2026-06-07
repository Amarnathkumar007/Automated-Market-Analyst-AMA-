from dotenv import load_dotenv
from api_request import call_api, extract_property_metrics
from gemini import generate_market_narrative
from google import genai
import os
from generate_pdf import generate_pdf_with_jinja
import json

load_dotenv()

with open('agent.json', 'r') as file:
    data = json.load(file)

HOUSE=data["HOUSE"]
STREET=data["STREET"]
PIN_CODE=data["PIN_CODE"]
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key) if api_key else None

api_response=call_api(HOUSE, STREET, PIN_CODE)
market_data=extract_property_metrics(api_response)
print(market_data)
# narrative = generate_market_narrative(market_data, client)



# Map raw API field names → PDF template field names (with safe types)
pdf_market = {
    "city":               str(market_data.get("city") or "N/A"),
    "median_price":       int(market_data.get("property_price") or market_data.get("estimated_value") or 0),
    "days_on_market":     int(market_data.get("days_on_market") or 0),
    "list_to_sale_ratio": float(market_data.get("price_drop_ratio") or 100.0),
}
# print(pdf_market)
# generate_pdf_with_jinja(data, pdf_market, narrative)
generate_pdf_with_jinja(data, pdf_market, "This is just the test to save the tokens")
