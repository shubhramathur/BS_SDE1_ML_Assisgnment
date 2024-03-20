from flask import Flask, request, jsonify
from your_module import calculate_sentence_probability

app = Flask(__name__)

# Load your bigram and trigram models here
# Make sure you have the models available in your application

@app.route('/')
def home():
    return 'Welcome to the Language Model API!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    sentence = data['sentence']

    # Calculate probability for bigram model
    bigram_probability = calculate_sentence_probability(sentence, bigram_model)

    # Calculate probability for trigram model
    trigram_probability = calculate_sentence_probability(sentence, trigram_model)

    # Return the results
    return jsonify({
        'bigram_probability': bigram_probability,
        'trigram_probability': trigram_probability
    })

if __name__ == '__main__':
    app.run(debug=True)
