
    
    


# Backup code if above doesn't work, code below is hardcoded to irvine, above should take location input
"""
import requests
import json

url = "https://api.yelp.com/v3/businesses/natural_language_search"

payload = {
    "messages": [{"content": "study spots and cafes"}],
    "location": "Irvine",
    "timezone": "America/New_York"
}

# Authorization header with API key
header = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer " + "6jsrkDuonkZm550GADNb_xr3zEfpQzbn8cpYbBe6UEznghFZkt-Rfgmjx0Qmuy7K3fuuHrbdC82xNNZZTmiaXHSrpjr94ymQh27vNmwuB_uYVd1VADZmdnu2FrAmZ3Yx"
}

# Send a POST request with JSON payload and headers
response = requests.post(url, json=payload, headers=header)

# Check for errors
if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
else:
    # Parse and filter the JSON response
    data = response.json()
    businesses = data.get("businesses", [])

    # Extract only name, address, and image_url for each business
    recommendations = [
        {
            "name": business.get("name"),
            "address": ", ".join(business["location"].get("display_address", [])),
            "image_url": business.get("photos")
        }
        for business in businesses
    ]

    # Print formatted JSON output of the recommendations
    print(json.dumps(recommendations, indent=4))

#except requests.exceptions.RequestException as e:
#return jsonify({"error": str(e)}), 500


url = "https://api.yelp.com/v3/businesses/natural_language_search"

payload = {
    "messages": [{"content": "study spots and cafes"}],
    "location": "Irvine",
    "timezone": "America/New_York"
}

# Import os to use os.getenv
header = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer " + "6jsrkDuonkZm550GADNb_xr3zEfpQzbn8cpYbBe6UEznghFZkt-Rfgmjx0Qmuy7K3fuuHrbdC82xNNZZTmiaXHSrpjr94ymQh27vNmwuB_uYVd1VADZmdnu2FrAmZ3Yx"
}

response = requests.post(url, json=payload, headers=header)

# Convert to JSON object
data = response.json()

# Print formatted JSON data
print(json.dumps(data, indent=4))

#print(response.text)


# Send a request to the Yelp API
try:
    response = requests.post(url, json=payload, headers=header)
    response.raise_for_status()
    return jsonify(response.json())  # Return Yelp API response as JSON
except requests.exceptions.RequestException as e:
    return jsonify({"error": str(e)}), 500"""