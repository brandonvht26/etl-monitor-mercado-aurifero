from decouple import config
import requests

def make_gapi_request():
    api_key = config('GOLD_API_KEY')
    symbol = "XAU"
    curr = "USD"
    date = ""

    url = f"https://www.goldapi.io/api/price/{symbol}/{curr}{date}"

    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }

    try: 
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()

        price = result["price"]
        timestamp = result["datetime"]

        print(f"\nPrecio: ${price}\nTiempo: {timestamp}")
        
    except requests.exceptions.RequestException as e:
        print(f"\n[ERRROR] {str(e)}\n")

if __name__ == "__main__":
    make_gapi_requests()