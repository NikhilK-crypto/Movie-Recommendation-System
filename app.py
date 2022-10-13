import streamlit as st
import pandas as pd
import numpy as np
import pickle

similarity_vec = pickle.load(open('similarity_vec','rb'))
movies = pd.read_csv('Movies_with_Tags.csv')

def similarity_of_movies(movie_name):
    movie_name = movie_name.lower()
    index = movies.loc[movies['original_title']==movie_name].index[0]
    
    movie_indexes = np.arange(0, similarity_vec[index].shape[0],
                         dtype='int').reshape(-1, 1)
    
    stack = np.hstack((similarity_vec[index].reshape(-1, 1),movie_indexes))
    
    sorted_stack = stack[stack[:,0].argsort()][::-1]
    
    similar_movies_index = sorted_stack[1:6][:,1]
    
    similar_movies = movies.loc[similar_movies_index,'original_title']
    return similar_movies


st.title("Movie Recommendation System")

movie_name = st.selectbox(
    'Which number do you like best?',
     list(movies['original_title'].values))

'you selected: ', movie_name

if st.button('Recommend Similar Movies'):
    recommendations = similarity_of_movies(movie_name)
    for i in recommendations:
        st.write(i)
