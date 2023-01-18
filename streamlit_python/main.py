import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = './data/Motor_Vehicle_Collisions_-_Crashes.csv'

st.title("Motor Vehicle Collisions in NYC")
st.markdown("This application is a Streamlit dashboard that can be used"
            "to analyze motor vehicle collision in NYC 🗽"
            )

@st.cache(persist=True)
def load_data(nrows) :
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowcase = lambda x : str(x).lower()
    data.rename(lowcase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time' : 'date/time'}, inplace=True)
    return data

data = load_data(100000)

st.header("Where are the most people injured in NYC ")
injured_people = st.slider("Number of persons injured in vehicle collisions",0,19)
st.map(data.query("injured_people >= @injured_people")[["latitude", "longitude"]].dropna(how="any"))


if st.checkbox("Show Raw Data", False) :
    st.subheader('Raw Data')
    st.write(data)