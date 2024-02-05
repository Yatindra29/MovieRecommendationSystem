import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=a814d3f02423ded61ccf6654ec6a9418&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_overview(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=a814d3f02423ded61ccf6654ec6a9418&language=en-US'.format(
            movie_id))
    data = response.json()
    return data['overview']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_overview=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_overview.append(fetch_overview(movie_id))
    return recommended_movies, recommended_movies_posters,recommended_movies_overview


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Your Movie Pal 🎬')
st.image('director.jpg', caption='“Oh how Shakespeare would have loved cinema!”')
selected_movie_name = st.selectbox(
    'Which movie did you watch recently that you liked?',
    movies['title'].values)

if st.button('What should I watch now?'):
    st.image('Cook.jpg', caption='Let us cook up the recommendations!')
    names, posters, overviews = recommend(selected_movie_name)
    st.header('You would love these!')
    tab1, tab2, tab3, tab4, tab5 = st.tabs([names[0],names[1],names[2],names[3],names[4]])

    with tab1:
        poster,name=st.columns(2)
        with poster:
            st.image(posters[0])
        with name:
            st.header(names[0])
            st.markdown(overviews[0])


    with tab2:
        poster, name = st.columns(2)
        with poster:
            st.image(posters[1])
        with name:
            st.header(names[1])
            st.markdown(overviews[1])

    with tab3:
        poster, name = st.columns(2)
        with poster:
            st.image(posters[2])
        with name:
            st.header(names[2])
            st.markdown(overviews[2])

    with tab4:
        poster, name = st.columns(2)
        with poster:
            st.image(posters[3])
        with name:
            st.header(names[3])
            st.markdown(overviews[3])

    with tab5:
        poster, name = st.columns(2)
        with poster:
            st.image(posters[4])
        with name:
            st.header(names[4])
            st.markdown(overviews[4])
