import streamlit as st

# Title
st.markdown("<h1 style='text-align: center; color: black;'>Prashanna Cyclone Tracker</h1>", unsafe_allow_html=True)

# Description
st.write("Real-time tracking of cyclones around India and Southeast Asia, with NIT Rourkela marked in the map.")

# Embed Windy.com iframe for real-time weather tracking
windy_embed_code = """
<iframe width="650" height="450" src="https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=default&metricTemp=default&metricWind=default&zoom=5&overlay=wind&product=ecmwf&level=surface&lat=16.51&lon=85.825&detailLat=20.271&detailLon=85.833&detail=true" frameborder="0"></iframe>
"""

# Display the iframe with Windy.com cyclone tracking
st.components.v1.html(windy_embed_code, height=600)

