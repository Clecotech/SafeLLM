# SafeLLM API 🚀
This is a Flask-based API that processes user queries, ensuring they are non-toxic and appropriate. It uses pre-trained NLP models for query classification, toxicity detection, and query rewriting.

## Features ✨
- 🛡️ Detects and blocks toxic or inappropriate content.
- 🧠 Classifies query intents and restricts certain types of queries.
- ✍️ Rewrites queries for better clarity.
- 🤖 Generates responses to rewritten queries.

## Tech Stack 🛠️
- Flask: Backend framework for the API.
- Transformers Library: For text classification and query rewriting.
- Detoxify: For toxicity detection in text.

## Endpoints 🔗
### /query (Method: POST)
Processes user queries by:

1. Checking for toxicity.
2. Classifying intent.
3. Rewriting queries for clarity.
4. Generating a response.


### **Request Body (JSON):**  📤
```json
{
  "query": "Your input query here"
}
```

### **Response:** 📥
🚫 If query contains toxicity:
```json
{
  "query": "Query contains inappropriate content."
}
```
  **Status Code: 403**

  ### **Response:**  
☣️ If query is restricted:
```json
{
  "query": "Restricted query detected."
}
```
  **Status Code: 403**

  ### **Response:**  
✅ If query is valid:
```json
{
  "query": "LLM Response to: Your clarified query"
}
```
  **Status Code: 200**

## Installation 🛠️
### Prerequisites
- Python 3.8 or later
- pip package manager

## Setup ⚡
1. Clone the repository:
```
   git clone git@github.com:Clecotech/SafeLLM.git
   cd SafeLLM
```
2. Install dependencies:
  ```
    pip install -r requirements.txt
```

3. Run the application:
   ```
   python app.py
   ```
4. The app will run on http://localhost:5001 🌐

## Environment Configuration 🌱
You can set up a virtual environment for this project:
```
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
pip install -r requirements.txt  
```

## Example Request 📡
### cURL:
```
curl -X POST http://localhost:5001/query \
-H "Content-Type: application/json" \
-d '{"query": "Explain the process of natural language processing."}'
```

