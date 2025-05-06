import streamlit as st
import pandas as pd
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error: {e}")

if not st.session_state.df.empty:
    if st.button("Display Data"):
        st.subheader("Data Preview")
        st.dataframe(st.session_state.df)

    st.subheader("Filter Options")
    unique_dates = sorted(st.session_state.df["Order Date"].dropna().unique())
    unique_restaurants = sorted(st.session_state.df["Restaurant Name"].dropna().unique())

    selected_date = st.selectbox("Select Order Date", unique_dates)
    selected_restaurant = st.selectbox("Select Restaurant", unique_restaurants)

    filtered_df = st.session_state.df[
        (st.session_state.df["Order Date"] == selected_date) &
        (st.session_state.df["Restaurant Name"] == selected_restaurant)
    ]

    st.write(f"Here are matching records: {len(filtered_df)}")
    st.dataframe(filtered_df)

    if not filtered_df.empty:
        buffer = io.StringIO()
        filtered_df.to_csv(buffer, index=False)
        st.download_button(
            label="Download Filtered CSV",
            data=buffer.getvalue(),
            file_name="filtered_GFF_March_2025.csv",
            mime="text/csv"
        )

    if st.button("Delete Filtered Records"):
        before_count = len(st.session_state.df)
        st.session_state.df = st.session_state.df[
            ~((st.session_state.df["Order Date"] == selected_date) &
              (st.session_state.df["Restaurant Name"] == selected_restaurant))
        ]
        after_count = len(st.session_state.df)
        st.success(f"Deleted {before_count - after_count} record(s).")

        st.write("Updated DataFrame:")
        st.dataframe(st.session_state.df)

    if st.button("Send Email Notification"):
        recipient_email = st.text_input("Enter recipient's email")
        if recipient_email:
            summary_df = filtered_df.groupby("Order Date").agg(
                total_orders=("Order ID", "count"),
                total_amount=("Amount", "sum")
            ).reset_index()

            summary_text = summary_df.to_string(index=False)

            sender_email = "balajiyalburgi003@gmail.com"
            sender_password = "sljl nfeq oawu erha" #ITS MY PERSONEL PASSWORD, PLEASE CHANGE IT TO YOURS

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = "Date-wise Summary Report"

            msg.attach(MIMEText(summary_text, 'plain'))

            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.send_message(msg)
                st.success("Email sent successfully!")
            except Exception as e:
                st.error(f"Error sending email: {e}")
        else:
            st.warning("Please enter a valid email address.")
