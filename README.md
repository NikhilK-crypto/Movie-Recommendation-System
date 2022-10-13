# Movie-Recommendation-System

This is a movie recommendation system where it while recommend movies based on tags similarity. 
The data is taken from kaggle TMDB 5000 Movies Dataset 
Link - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv 
In this project, first i created tags from different columns present in the data. After that i did text processing like removing stopwords then lower the sentence and then using bag of words i converted the text into vectors where we only took 10000 words as max_features. Using this vector, i found the similarity matrix of each movie with other using cosine_distance. 
At the end the used stramlit app to create api where use can interact with our model and later deployed it on heroku server
Link to access website deployed on server - https://nikhils-movie-recommender-sys.herokuapp.com/
