import streamlit as st
import pandas as pd

st.set_page_config(page_title="College Search", layout="wide")
st.title("🏫 Search College by District and Name")

# Load and clean Excel
file_path = "col_con.xlsx"
try:
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip().str.lower()  # Clean headers
except Exception as e:
    st.error(f"Error loading Excel file: {e}")
    st.stop()

# Check if required columns exist
if "district name" not in df.columns or "college name" not in df.columns:
    st.error("Excel must contain columns 'District' and 'College Name' (case-insensitive).")
    st.write("Found columns:", df.columns.tolist())  # Help user debug
    st.stop()

# Search form
with st.form("search_form"):
    col1, col2 = st.columns(2)
    district_input = col1.text_input("District Name")
    college_input = col2.text_input("College Name")
    submitted = st.form_submit_button("Search")

# Search logic
if submitted:
    filtered_df = df.copy()

    if district_input.strip():
        filtered_df = filtered_df[filtered_df["district name"].astype(str).str.contains(district_input.strip(), case=False, na=False)]

    if college_input.strip():
        filtered_df = filtered_df[filtered_df["college name"].astype(str).str.contains(college_input.strip(), case=False, na=False)]

    if not filtered_df.empty:
        st.success(f"✅ Found {len(filtered_df)} matching record(s):")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("❌ No matching records found.")
