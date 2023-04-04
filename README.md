# Movie-Recommendation-System

This project is a movie recommendation system that recommends movies based on similarity.  <br /><br />
The data was taken from Kaggle TMDB 5000 Movies Dataset (link provided below)
Link - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv <br /><br />

## Process 
* To begin, I created tags from different columns present in the data. 
* Then, I performed text processing which involved removing stopwords, lowercasing the sentence, and using bag of words. The text was then converted into vectors where only 10,000 words were taken as max_features.
* Using this vector, I found the similarity matrix of each movie with others using cosine_distance. <br /><br />

## Api and Deployement
In the end, I used the Streamlit package to create an API where the user can interact with my model, and later deployed it on Heroku server. Please note that Salesforce (Heroku's parent organization) phased out its free tier plan in November 2022, resulting in my project deployment being no longer accessible. <br /><br />
Link to access website deployed on server - https://nikhils-movie-recommender-sys.herokuapp.com/
