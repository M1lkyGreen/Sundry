import pandas as pd
from textblob import TextBlob

# Load the data
file_path = r'C:\Users\27234\Desktop\AI\BIGDATA\淘宝商品评论.csv'
df = pd.read_csv(file_path,encoding='gbk')

# The review column is named '评论内容'
reviews_column = '评论内容'

# Function to analyze sentiment
def analyze_sentiment(review):
    analysis = TextBlob(str(review))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# Apply sentiment analysis
if reviews_column in df.columns:
    df['sentiment'] = df[reviews_column].apply(analyze_sentiment)
    result = df['sentiment'].value_counts(normalize=True)
    # Determine overall sentiment
    total_reviews = len(df)
    positive_reviews = result.get('positive', 0) * total_reviews
    negative_reviews = result.get('negative', 0) * total_reviews
    overall_sentiment = ('positive' if positive_reviews > negative_reviews else
                         'negative' if negative_reviews > positive_reviews else
                         'neutral')
else:
    raise Exception(f'Column "{reviews_column}" does not exist in the provided data.')

# The final output would be a tuple of the overall sentiment and the sentiment distribution
print(overall_sentiment)