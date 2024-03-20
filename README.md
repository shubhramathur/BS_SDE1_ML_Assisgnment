# BS_SDE1_ML_Assisgnment
Data Download and Preprocessing
Data Download
The data used for this project can be downloaded from [link to dataset] and saved in the data/ directory.

Data Preprocessing Steps
Tokenization: Splitting the text into individual words or tokens.
Lowercasing: Converting all words to lowercase to reduce vocabulary size.
Removing Punctuation: Eliminating non-alphanumeric characters.
Stopwords Removal: Removing common words like "the", "a", etc., that do not contribute much to the language model.
Building N-Gram Language Models
The code provides functions to build trigram and bigram language models from the preprocessed training data. Laplace smoothing is implemented to handle unknown words and prevent zero probabilities. The following steps are performed:

Build Trigram Model
Build Bigram Model
Implement Laplace Smoothing
Calculate Probabilities for Sentences
Count and probability matrices are displayed for better understanding of the language models.

Sentence Generation on Flask App
A Flask web application with a simple user interface is developed to accept a starting word from the user. The provided word is used to generate a sentence using both trigram and bigram models. Users can select the model from the UI. The generated sentences are displayed to the user on the web interface.

Evaluation Metrics
The trained models are evaluated using appropriate metrics on test data. Evaluation includes:

Perplexity: Measure of how well the model predicts the test data.
Accuracy: Percentage of correctly generated sentences compared to the test data.
BLEU Score: Measure of the quality of generated sentences compared to reference sentences.
Results from both bigram and trigram models are compared to analyze their performance.

Flask App Setup for Local Image Classification
A guide is provided on setting up a Flask application for local image classification. Steps include:

Install necessary dependencies.
Preprocess images for model input.
Load the trained image classification model.
Implement image classification endpoint in Flask app.
Run the Flask app locally for testing.
Enhancement Scope
Improve Model Performance: Experiment with different smoothing techniques or neural language models like LSTM or Transformer.
Automated Feature Extraction: Explore automated methods for feature extraction, such as using deep learning models like CNNs for text feature extraction.
UI/UX Enhancements: Improve the user interface of the Flask app for better user experience.
Model Deployment: Provide instructions for deploying the trained models and Flask app to cloud platforms like Heroku or AWS for production use.
For detailed implementation and code, please refer to the corresponding directories and files in this repository. Feel free to contribute or provide feedback for further improvements.
