import tweepy
import pandas as pd
import time

# Twitter API credentials (replace with your own)
api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def search_twitter(query, count=100):
    """Search for tweets containing a specific query and return a list of unique usernames."""
    try:
        tweets = api.search_tweets(q=query, count=count)
        usernames = list(set(tweet.user.screen_name for tweet in tweets))
        return usernames
    except Exception as e:
        print(f"Error during search: {e}")
        return []


def get_followers_of_influencer(username, min_followers=500, max_followers=10000, limit=1000):
    """Fetch followers of a given influencer within a specified follower count range."""
    followers = []
    try:
        for follower in tweepy.Cursor(api.get_followers, screen_name=username, count=200).items(limit):
            if min_followers <= follower.followers_count <= max_followers:
                followers.append(follower.screen_name)
        return followers
    except Exception as e:
        print(f"Error fetching followers for {username}: {e}")
        return []


def fetch_influencer_data(username):
    """Fetch follower count, tweet count, and engagement rate for a given username."""
    try:
        user = api.get_user(screen_name=username)
        tweets = api.user_timeline(
            screen_name=username, count=100, tweet_mode="extended")

        # Calculate engagement rate
        total_engagements = sum(tweet.favorite_count +
                                tweet.retweet_count for tweet in tweets)
        avg_engagement_rate = total_engagements / \
            len(tweets) / user.followers_count

        return {
            'Username': username,
            'Followers': user.followers_count,
            'Tweets': user.statuses_count,
            'Engagement Rate': avg_engagement_rate
        }
    except Exception as e:
        print(f"Error fetching data for {username}: {e}")
        return None


def process_influencers(usernames, output_file='influencer_data.csv'):
    """Process a list of usernames and save their data to a CSV file."""
    influencer_data = []

    for i, username in enumerate(usernames):
        data = fetch_influencer_data(username)
        if data:
            influencer_data.append(data)

        # Avoid hitting rate limits
        if (i + 1) % 100 == 0:
            print(
                f"Processed {i + 1} users, sleeping for 15 minutes to avoid rate limit...")
            time.sleep(15 * 60)

    df = pd.DataFrame(influencer_data)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")


hashtags = ['#fitness', '#tech', '#beauty',
            '#microinfluencer', '#nanoinfluencer']
all_usernames = []
for tag in hashtags:
    all_usernames.extend(search_twitter(tag, count=100))

all_usernames = list(set(all_usernames))

process_influencers(all_usernames, output_file='twitter_influencers.csv')
