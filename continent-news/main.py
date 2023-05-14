import datetime
import config
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=config.NEWS_API_KEY)

date = datetime.datetime.utcnow().date()

NUM_ARTICLES_TO_GET = 15 # Change based on num articles you wanna get

# Define the sources for each continent
sources = ['al-jazeera-english', 'bbc-news', 'associated-press', 'reuters', 'cnn', 'abc-news-au', 'the-guardian-au']

# Fetch top articles for each continent
top_articles = []

for source in sources:
    top_headlines = newsapi.get_top_headlines(
        sources=source,
        language='en',
        page_size=20,
        page=1
    )
    
    articles = top_headlines['articles']

    today = datetime.datetime.today()

    
    # Filter out sports or celebrity-related articles
    filtered_articles = [article for article in articles if 'sports' not in article['title'].lower() and 'entertainment' not in article['title'].lower() and \
(datetime.date(int(article['publishedAt'].split("-")[0]), int(article['publishedAt'].split("-")[1]), int(article['publishedAt'].split("-")[2].split("T")[0])) > (datetime.datetime.today() - datetime.timedelta(days=2)).date())]

    
    
    # Sort articles based on published time
    sorted_articles = sorted(filtered_articles, key=lambda x: x['publishedAt'], reverse=True)
    
    top_articles.extend(sorted_articles)

top_articles = sorted(top_articles, key=lambda x: x['publishedAt'], reverse=True)[:NUM_ARTICLES_TO_GET]

file = open("continent-news/headlines.txt", "w")

# Print the results
for article in top_articles:
    file.writelines(article['title'] + "\n")
    file.writelines(article['publishedAt'] + "\n")
    file.writelines(article['description'] + "\n")
    file.writelines(article['source']['name'] + "\n")
    file.writelines(str(article['content']) + "\n")
    file.writelines(article['title'] + "\n")
    file.writelines("---" + "\n") 
print("finished process")