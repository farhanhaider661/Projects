import streamlit as st
import pickle as p
import pandas as pd
import requests
movies_dict=p.load(open('movies_dict.pkl','rb'))
similarity=p.load(open('sim.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('Movie Recommender System')
option=st.selectbox('Search Movies',movies['title'].values)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=11f6f3d8bb987ba9dd5b86cc636cb615&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
# e127054336ecf0e64934da50a279ddb7
def recommend(name):
    movie_index=movies[movies['title']==name].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:7]
    recommend_movies=[]
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from API
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies,recommended_movie_posters

if st.button('Get Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5,col6 = st.columns([1,1,1,1,1,1])
    col1, col2, col3 = st.columns(3)
    col4, col5,col6 = st.columns(3)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])