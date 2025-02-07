import requests

def search_google(query, api_key, cx):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cx,
        'q': query
    }
    response = requests.get(url, params=params)
    return response.json()

def search_facebook(query, access_token):
    url = f"https://graph.facebook.com/v14.0/search"
    params = {
        'access_token': access_token,
        'q': query,
        'type': 'page'
    }
    response = requests.get(url, params=params)
    return response.json()

def search_twitter(query, bearer_token):
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {
        'Authorization': f'Bearer {bearer_token}',
    }
    params = {
        'query': query,
        'max_results': 10,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def main():
    google_api_key = 'YOUR_GOOGLE_API_KEY'
    google_cx = 'YOUR_GOOGLE_CX'
    facebook_access_token = 'YOUR_FACEBOOK_ACCESS_TOKEN'
    twitter_bearer_token = 'YOUR_TWITTER_BEARER_TOKEN'
    
    query = input("Enter search query: ")
    
    google_results = search_google(query, google_api_key, google_cx)
    print("Google Results:", google_results)
    
    facebook_results = search_facebook(query, facebook_access_token)
    print("Facebook Results:", facebook_results)
    
    twitter_results = search_twitter(query, twitter_bearer_token)
    print("Twitter/X Results:", twitter_results)

if __name__ == "__main__":
    main()
  
