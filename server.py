from flask import Flask, request, render_template, jsonify, make_response
from service.translator import english_to_french, french_to_english
import json

app = Flask("Translator")


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/frenchToEnglish', methods=['POST', 'GET'])
def translate_to_english():
  response = make_response(
  jsonify(
    {'result': french_to_english(request.args.to_dict().get('text'))}
  ),
  200
  );

  response.headers["Content-Type"] = "application/json"
  print(response)
  return response


@app.route('/englishToFrench', methods=['POST', 'GET'])
def translate_to_french():
  response = make_response(
    jsonify(
      {"result": english_to_french(request.args.to_dict().get('text'))}
    ),
    200
  )

  response.headers["Content-Type"] = "application/json"
  print(response)
  return response

if __name__ == "__main__":
  app.run(debug=True)
