import os
import requests
API_KEY = os.getenv("GOOGLE_CSE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")

class GoogleSearchTool:
    def __init__(self, api_key=None, cse_id=None):
        self.api_key = api_key or os.getenv("GOOGLE_CSE_API_KEY")
        self.cse_id = cse_id or os.getenv("GOOGLE_CSE_ID")
        if not self.api_key or not self.cse_id:
            print("⚠️ Google Search Tool disabled (missing API key/CSE ID).")

    def search(self, query: str, num: int = 3):
        if not self.api_key or not self.cse_id:
            return ["--- SEARCH TOOL DISABLED (Missing API Key / CSE ID) ---"]

        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.api_key,
            "cx": self.cse_id,
            "q": query,
            "num": num
        }

        try:
            r = requests.get(url, params=params, timeout=10)
            r.raise_for_status()
            data = r.json()
            items = data.get("items", [])
            
            results = []
            for it in items:
                title = it.get("title", "")
                snippet = it.get("snippet", "")
                # Short summary: limit to ~50 words
                words = snippet.split()
                if len(words) > 50:
                    snippet = " ".join(words[:50]) + "..."
                results.append(f"{title}: {snippet}")
            return results
        except Exception as e:
            return [f"Error fetching search results: {e}"]
