import requests
import json

# I reconstructed this from your screenshot
API_URL = "https://propfirmmatch.com/api/trpc/firm.listAll?input=%7B%22json%22%3A%7B%22limit%22%3A100%7D%7D"

def fetch_live_data():
    print(f"Targeting URL: {API_URL}")
    print("Fetching live data...")

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://propfirmmatch.com/",
    }

    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status() # Stop if error
        
        data = response.json()
        
        # Based on tRPC structure, the data is likely nested deep.
        # We save the whole thing so you can inspect it.
        with open("prop_firms_live.json", "w") as f:
            json.dump(data, f, indent=2)
            
        print("✅ Success! Data saved to 'prop_firms_live.json'")
        
        # Quick check to see if we got firms
        try:
            # Typically tRPC data is in result -> data -> json -> ...
            firms = data['result']['data']['json']
            print(f"🎉 Found {len(firms)} firms in the download.")
        except:
            print("Data saved, but the structure was different than expected. Check the JSON file manually.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    fetch_live_data()
