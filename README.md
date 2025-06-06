# google-play-bank-reviews
## Methodology

### 1. Data Collection
I used the `google-play-scraper` Python package to collect recent app reviews from the Google Play Store for:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

Each review includes the following metadata:
- Review content
- Rating (1 to 5 stars)
- Date
- Bank name
- Source (Google Play Store)

I targeted 400–700 reviews per bank to ensure data quality after cleaning.

### 2. Preprocessing
Raw reviews were cleaned using a custom Python script to:
- Remove duplicate reviews
- Drop reviews missing essential fields (`review`, `rating`, or `date`)
- Save cleaned reviews to `bank_reviews_clean.csv`

This ensures the dataset is ready for downstream NLP analysis and visualization.
