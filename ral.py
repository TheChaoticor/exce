import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Excel Search", layout="wide")
st.title("🔍 Search in College Contacts")

# Load Excel file
file_path = "col_con.xlsx"
try:
    df = pd.read_excel(file_path)
except Exception as e:
    st.error(f"Error loading Excel file: {e}")
    st.stop()

st.markdown("Enter values in any field below to search (leave others blank).")

# Search form
with st.form("search_form"):
    col1, col2 = st.columns(2)
    district_input = col1.text_input("District")
    college_input = col2.text_input("College Name")
    submitted = st.form_submit_button("Search")
# Filtering
if submitted:
    filtered_df = df.copy()
    for col, val in search_inputs.items():
        if val.strip():
            filtered_df = filtered_df[filtered_df[col].astype(str).str.contains(val.strip(), case=False, na=False)]

    if not filtered_df.empty:
        st.success(f"Found {len(filtered_df)} matching record(s):")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("No matching records found.")
