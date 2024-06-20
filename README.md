# Cyberbullying Tweet Recognition App

This is a web application designed to predict the nature of tweets, classifying them into six categories:

- Age
- Ethnicity
- Gender
- Religion
- Other Cyberbullying
- Not Cyberbullying

The app is built using Streamlit and employs natural language processing (NLP) techniques to analyze the content of tweets and predict the type of cyberbullying, if any.

## Features

- **User-Friendly Interface**: Simple and intuitive interface for users to input tweets and get predictions.
- **Multiple Categories**: Predicts whether the tweet falls into one of the five cyberbullying categories or if it's not cyberbullying.
- **Visual Feedback**: Provides visual feedback based on the prediction.

## How to Run the App

### Prerequisites

Ensure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/cyberbullying-tweet-recognition-app.git
    cd cyberbullying-tweet-recognition-app
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download necessary NLTK data:

    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('punkt')
    nltk.download('omw-1.4')
    ```

### Running the App

To start the Streamlit app, run the following command in your terminal:

```bash
streamlit run app.py
