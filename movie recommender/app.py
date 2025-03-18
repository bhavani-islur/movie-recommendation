import streamlit as st
import pickle
import pandas as pd

# Custom CSS to set the background color to black and text color to bright white
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stApp {
        background-color: black;
    }
    .css-1d391kg, .css-18e3th9 {
        background-color: black;
    }
    .recommendation {
        color: #ffffff;  /* Bright white color */
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('🎬 Movie Recommender System')
selected_movie_name = st.selectbox('Choose a movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.markdown("<h3 style='color:white;'>Recommended Movies:</h3>", unsafe_allow_html=True)
    for i in recommendations:
        st.markdown(f"<p class='recommendation'>{i}</p>", unsafe_allow_html=True)
