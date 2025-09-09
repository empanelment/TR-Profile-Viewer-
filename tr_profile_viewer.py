import streamlit as st
import pandas as pd

# Load and clean Excel
@st.cache_data
def load_data(file_path):
    df = pd.read_excel(file_path)

    # Clean column names: strip spaces, lower-case
    df.columns = df.columns.str.strip().str.lower()

    # Flexible column mapping
    column_mapping = {
        "name of member": "name",
        "mrn no.": "mrn",
        "mobile no.": "mobile",
        "email id": "email",
        "final decision of board": "final_decision_of_board"
    }
    df = df.rename(columns=column_mapping)

    return df

# ✅ Pass your file path
file_path = r"C:\Users\ICAI\Desktop\TR Profile Viewer\Streamlit test.xlsx"
df = load_data(file_path)

# ----------------- Streamlit App -----------------
st.set_page_config(page_title="T.R. Profile Viewer", layout="centered")

st.title("📘 T.R. Profile Viewer")

search_input = st.text_input("🔎 Search by Name, MRN, Mobile, or Email")

# Dropdown filter
if "final_decision_of_board" in df.columns:
    filter_option = st.selectbox(
        "Filter by Final Decision of Board",
        options=["All"] + df["final_decision_of_board"].dropna().unique().tolist()
    )
else:
    filter_option = "All"

# Apply search
if search_input:
    search_input = search_input.lower()
    results = df[
        df.apply(lambda row: row.astype(str).str.lower().str.contains(search_input).any(), axis=1)
    ]
else:
    results = df.copy()

# Apply decision filter
if filter_option != "All" and "final_decision_of_board" in df.columns:
    results = results[results["final_decision_of_board"] == filter_option]

# Show profile
if not results.empty:
    for _, row in results.iterrows():
        st.subheader(f"👤 {row.get('name', 'Unknown')}")
        st.write(f"**MRN:** {row.get('mrn', 'N/A')}")
        st.write(f"**Mobile:** {row.get('mobile', 'N/A')}")
        st.write(f"**Email:** {row.get('email', 'N/A')}")
        st.write(f"**Final Decision of Board:** {row.get('final_decision_of_board', 'N/A')}")
        st.markdown("---")
else:
    st.warning("No matching records found.")
