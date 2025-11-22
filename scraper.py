import requests
import json

# UPDATED URL: Limit increased to 1000 to get ALL firms
API_URL = "https://propfirmmatch.com/api/trpc/firm.listAll?input=%7B%22json%22%3A%7B%22limit%22%3A1000%7D%7D"

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
        
        # Extract the actual list of firms from the deep JSON structure
        # Structure is usually: result -> data -> json
        try:
            firms_list = data['result']['data']['json']
            print(f"🎉 Success! Downloaded {len(firms_list)} firms.")
            
            # Save ONLY the list (cleaner than saving the whole messy object)
            with open("prop_firms_live.json", "w") as f:
                json.dump(firms_list, f, indent=2)
                
            print("✅ Saved clean list to 'prop_firms_live.json'")
            
        except KeyError:
            print("⚠️ Structure changed? Saving raw data instead.")
            with open("prop_firms_live.json", "w") as f:
                json.dump(data, f, indent=2)

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    fetch_live_data()
