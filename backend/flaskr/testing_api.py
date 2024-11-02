
    
    


# Backup code if above doesn't work, code below is hardcoded to irvine, above should take location input
"""
import os
import requests



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

print(response.text)
"""