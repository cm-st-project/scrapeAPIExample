import pandas as pd
import requests

payload = {
    'api_key': 'YOUR_API_KEY',
    'query': 'bitcoin',
    'num': '3',
    'time_period': '1D'
}

response = requests.get('https://api.scraperapi.com/structured/twitter/search', params=payload)

print(response.text)

twitter_data = []
data = response.json()
all_tweets = data['organic_results']
for tweet in all_tweets:
    print(tweet["snippet"])
    print(tweet["link"])
    twitter_data.append(
        {'title': tweet['title'], 'time': tweet["tags"], 'Tweet': tweet["snippet"], 'URL': tweet["link"]})

df = pd.DataFrame(twitter_data)
print(df.head())
