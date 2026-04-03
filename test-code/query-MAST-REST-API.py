import requests

url = "https://mast.stsci.edu/api/v0/invoke"

params = {
    "service": "Mast.Caom.Filtered",
    "params": {
        "obs_collection": ["Kepler"],
        "target_name": "Kepler-10"
    },
    "format": "json"
}

r = requests.post(url, json=params)
data = r.json()

print(data)