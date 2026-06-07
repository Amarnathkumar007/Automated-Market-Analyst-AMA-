import os
from google import genai
import api_request

def generate_market_narrative(market_data, client=None):
    
    # Structure the prompt clearly with the live data values
    prompt = (
        f"You are an expert real estate agent. Analyze these property statistics for the area of {market_data.get('city', 'N/A')}:\n"
        f"- Address: {market_data.get('address', 'N/A')}\n"
        f"- Property Price: ${market_data.get('property_price', 0):,}\n"
        f"- Estimated Value: ${market_data.get('estimated_value', 0):,}\n"
        f"- Days on Market: {market_data.get('days_on_market', 'N/A')} days\n"
        f"- Listing Date: {market_data.get('listing_date', 'N/A')}\n"
        f"- Current Status: {market_data.get('current_status', 'N/A')}\n"
        f"- Months Owned: {market_data.get('months_owned', 'N/A')} months\n"
        f"- Price Drop Ratio: {market_data.get('price_drop_ratio', 'N/A')}%\n\n"
        f"Write a professional, concise 3-sentence summary advising local homeowners "
        f"whether it is a good time to sell based on these exact metrics."
    )
    
    if not client:
        print("\n--- NO API KEY FOUND ---")
        print("Here is the prompt that WOULD be sent to Gemini:\n")
        print(prompt)
        print("---------------------------\n")
        return "[Mocked LLM Response: This is a great time to sell based on the estimated value of your property!]"
    
    # 1. Set the system instruction and choose the model
    system_prompt = "You are a professional real estate market analyst co-branded with Snaphomz."
    
    # 2. Configure temperature and token limits
    config = genai.types.GenerateContentConfig(
        max_output_tokens=3000,
        temperature=0.7,
        system_instruction=system_prompt
    )
    
    # 3. Execute the API call using the client
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=config
    )
    
    # 4. Return the processed text
    # print(response)
    return response.text.strip()