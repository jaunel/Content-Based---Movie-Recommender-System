# Content-Based---Movie-Recommender-System

Recommender System - Based upon some similarity we will get recommended. like youtube videos, e-commerce recommendation
There are three types of recommender system

    1. Content Based - Based upon the content we get recommended like similar songs recommended on GAANA.com while listening songs
    2. Collaborative filtering - Based upon similar personalities we get recommended. eg two person rated any movie quite similarly. so our algo will treat these two person similarly. And one user will get recommended based upon anothers watchlist.
    3. Hybrid based - Both technique is used jointly as per their convenience.
    
Feature Selection
    Budget - nobody recommends movie based upon budget
    Genres - we recommend movies based upon genre link scifi, thriller, comedy
    Homepage - doesnt required
    Id - will require for web development 
    keyword - tags..required
    original_lan - highly imbanced towards english so will drop it
    original_title - we will use title, original may be in regional language also
    overview - content depends upon overview, so highly required
    popularity - numeric value so dont use
    production_companies - recommendation doesnt based upon production_companies, so dropping
    production_countries - doesnt required
    release_date - generation wise, it required but since numeric so dropping it
    revenue - indirect indicator, but wont recommend based upon
    runtime- doesnt required
    spoken_lang - doesnt required
    tagling - have kept overview so omitting
    title - will keep it
    vote_average - numeric will remove it
    vote_count - again numeric wont use here
    movie_id - will use id so no movie_id
    cast - based upon cast we recommend like srk
    crew - we recommend particular director movie so keep it

    
