import streamlit as st
import pandas as pd

# App title
st.set_page_config(page_title="Self Improvement Dataset Viewer", layout="wide")
st.title("📈 Self Improvement Dataset Viewer")

@st.cache_data
def load_data(file_path: str):
    try:
        data = pd.read_csv(file_path)
        return data, None
    except FileNotFoundError:
        return None, "⚠️ Dataset not found. Please upload or place `self_improvement.csv` in the project folder."
    except Exception as e:
        return None, f"⚠️ Something went wrong while loading the dataset: {str(e)}"

# Load dataset
df, error = load_data("self_improvement.csv")

if error:
    st.warning(error)
    uploaded_file = st.file_uploader("Or upload your self_improvement.csv file here", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("✅ File uploaded successfully!")
        except Exception as e:
            st.error(f"Could not read uploaded file: {str(e)}")
else:
    st.success("✅ Dataset loaded successfully!")

# Show data if available
if df is not None:
    st.subheader("🔍 Preview of Data")
    st.dataframe(df.head())

    st.subheader("📊 Basic Statistics")
    st.write(df.describe())
