from google_play_scraper import Sort, reviews
import pandas as pd
from datetime import datetime
import time

# Dictionary of bank names and their app IDs
bank_apps = {
    "CBE": ("com.combanketh.mobilebanking", 600),
    "BOA": ("com.boa.boaMobileBanking", 600),
    "Dashen": ("com.dashen.dashensuperapp", 440)
}


def fetch_reviews(app_id, bank_name, num_reviews=600):
    print(f"Fetching reviews for {bank_name}...")
    all_reviews = []
    count = 0
    next_token = None

    while count < num_reviews:
        review_batch, next_token = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=200,  # max per request
            continuation_token=next_token
        )

        for r in review_batch:
            all_reviews.append({
                'review': r['content'],
                'rating': r['score'],
                'date': r['at'].strftime('%Y-%m-%d'),
                'bank': bank_name,
                'source': 'Google Play Store'
            })

        count = len(all_reviews)
        print(f"{count} reviews collected...")
        if not next_token:
            break
        time.sleep(1)

    return all_reviews[:num_reviews]

all_data = []
for bank, (app_id, review_target) in bank_apps.items():
    bank_reviews = fetch_reviews(app_id, bank, num_reviews=review_target)
    all_data.extend(bank_reviews)

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Clean data
df.drop_duplicates(subset='review', inplace=True)
df.dropna(subset=['review', 'rating'], inplace=True)
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Save to CSV
df.to_csv("bank_reviews.csv", index=False)
print("\n✅ Reviews saved to 'bank_reviews.csv'")
