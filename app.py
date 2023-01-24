#importing the libraries
import streamlit as st
import pickle

#providing the title
st.title("Movie Recommender System")

# we will import movies list as dict from our model code
movies_list = pickle.load(open('movies.pkl','rb'))

#Iterating over the dictionary through values
movies=[]
for i in movies_list.values():
    movies.append(i)
print(movies)

#Importing dataframe & similarity matrix for our recommend button
new_df = pickle.load(open('new_df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]             # will provide index of given movie
    distances = similarity[movie_index]                                 # finding movie vector
    movies_list = sorted(list(enumerate(similarity[movie_index])),
                         reverse=True, key=lambda x: x[1])[ 1:6]        # selecting top 5 movie

    recommended = []                                                    #this will store all 5 recommended movie
    for i in movies_list:
        recommended.append(new_df.iloc[i[0]].title)
    return recommended


#selecting a text box for user input
selected_movie = st.selectbox(
    'Select the movie',movies)

if st.button('Recommend'):
    recommended_movies = recommend(selected_movie)
    for i in recommended_movies:
        st.write(i)

