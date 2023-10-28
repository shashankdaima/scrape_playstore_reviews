import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from models.reviews import Review


# Create an input field for Play Store URLs
st.title("Play Store Review Analysis")
st.write("Enter Play Store URLs (separate with a newline):")
urls = st.text_area("Enter URLs", "")
urls = urls.split("\n")

# Display URLs as chips/capsules

# Button to trigger review analysis
if st.button("Find Review Analysis"):
    st.write("Entered URLs:")
    for url in urls:
        st.text(url)
    print(urls)
    pass

# Run the app
if __name__ == "__main__":
    st.set_option('deprecation.showPyplotGlobalUse', False)
