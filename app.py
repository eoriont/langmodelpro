from flask import Flask, jsonify, request
import os
from langchain_interpreter import chain_from_str


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/api", methods=["POST"])
def schema_api():
    try:
        req_json = request.json
        schema = req_json.get("schema")
        inputs = req_json.get("langchain_inputs")
        history = req_json.get("history")

        openai_api_key = request.headers.get("openai-api-key")

        lc = chain_from_str(
            schema,
            openai_api_key=openai_api_key,
            history=history,
        )
        return jsonify(lc(inputs))

    except Exception as e:
        print(e.with_traceback())
        return jsonify({"error": e.with_traceback()}), 400


if __name__ == "__main__":
    app.run(debug=True)
