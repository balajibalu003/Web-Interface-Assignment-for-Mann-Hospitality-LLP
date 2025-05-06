import streamlit as st
import pandas as pd
import io
import os


st.set_page_config(page_title="🍽️ ASSIGNMENT ", layout="centered")
st.title("🍽️  ASSIGNMENT")



if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()


uploaded_file = st.file_uploader("Upload your csv file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce').dt.date
        st.session_state.df = df
        st.success(" File uploaded successfully!")
    except Exception as e:
        st.error(f"Error : {e}")


if not st.session_state.df.empty:
    if st.button("Display Data"):
        st.subheader(" Data Preview")
        st.dataframe(st.session_state.df)

    
    st.subheader(" Filter Options")
    unique_dates = sorted(st.session_state.df["Order Date"].dropna().unique())
    unique_restaurants = sorted(st.session_state.df["Restaurant Name"].dropna().unique())

    selected_date = st.selectbox("Select Order Date", unique_dates)
    selected_restaurant = st.selectbox("Select Restaurant", unique_restaurants)

    filtered_df = st.session_state.df[
        (st.session_state.df["Order Date"] == selected_date) &
        (st.session_state.df["Restaurant Name"] == selected_restaurant)
    ]

    st.write(f"Here are  Matching Records: {len(filtered_df)}")
    st.dataframe(filtered_df)

    
    if not filtered_df.empty:
        buffer = io.StringIO()
        filtered_df.to_csv(buffer, index=False)
        st.download_button(
            label=" Download Filtered CSV",
            data=buffer.getvalue(),
            file_name="filtered_GFF_March_2025.csv",
            mime="text/csv"
        )

    
    if st.button(" Delete Filtered Records"):
        before_count = len(st.session_state.df)
        st.session_state.df = st.session_state.df[
            ~((st.session_state.df["Order Date"] == selected_date) &
              (st.session_state.df["Restaurant Name"] == selected_restaurant))
        ]
        after_count = len(st.session_state.df)
        st.success(f" Deleted {before_count - after_count} record(s).")

        st.write("Updated DataFrame:")
        st.dataframe(st.session_state.df)
