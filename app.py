import streamlit as st
from dotenv import load_dotenv

st.set_page_config(layout="wide")

st.title("🧪 Environment Test App")

try:
    # This is the line that was failing before
    find_dotenv_result = load_dotenv()

    st.success("✅ `python-dotenv` library was successfully loaded!")
    st.info(f"The `load_dotenv()` function returned: `{find_dotenv_result}`")
    st.write("This confirms the environment and requirements are now working correctly.")
    st.balloons()

except ImportError:
    st.error("❌ Still getting a `ModuleNotFoundError`. The deployment environment is stuck. Contact Streamlit support.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

