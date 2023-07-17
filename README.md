# LangModelPro

### Run locally with docker

```
docker-compose up --build
```

### Run locally with python

Run App:
```
python app.py
```

### Example in js:

> Make sure to first run the docker container, then run the following in NodeJS due to CORS

```js
// Your API Key and other data
let openaiApiKey = "your openai api key";
let langchainInputs = "What are some good potential names for my company?";
let history = "Human: My company bakes cakes out of rainbows.\nAI: Very cool! What can I help you with?";
let schema =  {
  "name": "Conversation Buffer Memory Chain",
  "description": "A chain for building a simple chatbot.",
  "template_version": "0.0.5",
  "chain": {
    "type": "ConversationChain",
    "llm": {
      "type": "openai",
      "args": {
        "temperature": 0.7
      }
    },
    "memory": {
      "type": "ConversationBufferMemory"
    }
  }
}


// The data to send in the body of the request
let data = {
    langchain_inputs: langchainInputs,
    history: history,
    schema: JSON.stringify(schema)
};

// Options for the fetch function
let options = {
    method: 'POST',
    headers: {
        'openai-api-key': openaiApiKey,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
};

// Send the request
fetch('http://localhost:8000/api', options)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.log('There was an error!', error));
```
