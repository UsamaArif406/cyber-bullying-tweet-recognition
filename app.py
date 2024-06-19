import streamlit as st
from PIL import Image
import nltk
from Prediction import prediction  # Ensure you import the correct prediction function

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')

# Constants
HEADER_TITLE = "Cyberbullying Tweet Recognition App"
HEADER_SUBTITLE = """
This app predicts the nature of the tweet into 6 Categories:
* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying
"""
IMAGE_PATHS = {
    "age": "Age.png",
    "ethnicity": "Ethnicity.png",
    "gender": "Gender.png",
    "other_cyberbullying": "Other.png",
    "religion": "Religion.png",
    "not_cyberbullying": "not_cyber.png",
    "twitter_logo": "twitter.png"
}

# Load and display logo
def display_logo(image_path, width=150):
    image = Image.open(image_path)
    st.sidebar.image(image, use_column_width=False, width=width)

# Display header
def display_header(title, subtitle):
    st.write(f'''
    # {title}
    {subtitle}
    ***
    ''')

# Display prediction result
def display_prediction_result(prediction_result):
    st.header("Prediction")
    if prediction_result in IMAGE_PATHS:
        st.image(IMAGE_PATHS[prediction_result], width=250)
    else:
        st.write("Unknown category")

# Main function
def main():
    display_header(HEADER_TITLE, HEADER_SUBTITLE)
    display_logo(IMAGE_PATHS["twitter_logo"])

    # Sidebar input
    st.sidebar.header('Enter Tweet ')
    tweet_input = st.sidebar.text_area("Tweet Input", height=200)

    # Process and display prediction
    if st.sidebar.button('Make Prediction'):
        if tweet_input:
            st.write('Making prediction...')
            prediction_result = prediction(tweet_input)
            display_prediction_result(prediction_result)
        else:
            st.write('***No Text Entered!***')

    st.write('***')

# Entry point
if __name__ == "__main__":
    main()
