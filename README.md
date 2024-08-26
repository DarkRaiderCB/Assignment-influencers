# Twitter Influencer Data Collection

This project is designed to collect data on Micro and Nano influencers on Twitter. It searches for influencers based on specific hashtags, retrieves followers of known influencers, and processes the collected data to calculate metrics like follower count, tweet count, and engagement rate. The final data is saved to a CSV file.

## Features

- **Hashtag Search:** Searches for tweets containing specified hashtags and extracts the usernames of the users who posted them.
- **Follower Extraction:** Fetches followers of known influencers within a specified follower count range.
- **Influencer Data Collection:** Gathers follower count, tweet count, and engagement rate for each influencer.
- **Rate Limit Handling:** Automatically pauses the script to avoid hitting Twitter API rate limits.
- **Data Export:** Saves the processed influencer data to a CSV file.

## Prerequisites

- **Python 3.x**
- **Twitter Developer Account**: Obtain API keys from [Twitter Developer](https://developer.twitter.com/).
- **Libraries**: Install the required Python libraries using pip:
  ```bash
  pip install tweepy pandas
  ```

## Setup

```
git clone https://github.com/yourusername/twitter-influencer-data.git
cd twitter-influencer-data
```

```
api_key = 'YOUR_API_KEY'
api_key_secret = 'YOUR_API_KEY_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
```

Run script

```
python influencer_data.py
```


## Thankyou!
