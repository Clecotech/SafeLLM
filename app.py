from flask import Flask, request, jsonify
from transformers import pipeline
from detoxify import Detoxify

app = Flask(__name__)

rewrite_model = pipeline("text2text-generation", model="pszemraj/grammar-synthesis-small")  
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english") 

def is_toxic(query):
    result = Detoxify('original').predict(query)
    return result['toxicity'] > 0.5

def classify_intent(query):
    result = classifier(query)
    return result[0]['label'] 

def rewrite_query(query):
    rewritten = rewrite_model(f"Clarify this: {query}", max_length=50, num_return_sequences=1)
    return rewritten[0]['generated_text']

@app.route('/query', methods=['POST'])
def process_query():
    data = request.json
    query = data.get('query')

    if is_toxic(query):
        return jsonify({"error": "Query contains inappropriate content."}), 403

    intent = classify_intent(query)
    if intent == 'LABEL_1':  
        return jsonify({"error": "Restricted query detected."}), 403

    safe_query = rewrite_query(query)

    response = f"LLM Response to: {safe_query}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5001)