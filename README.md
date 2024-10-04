# base64-encoding-decoding-using-flask-in-python
Author - BHUMIKA
<br>


Project: Base64 Encoder and Decoder API Using Flask

Introduction
<br>

This project is a Flask-based API that allows users to encode or decode data in Base64 format. It accepts input either as a string or a number, processes the input to either encode it to Base64 or decode it from Base64, and then returns the corresponding result.
<br>
Base64 encoding is commonly used to encode binary data, especially when transmitting over media that are designed to handle textual data. This project provides a simple API to handle Base64 encoding and decoding operations through HTTP requests, and it has been tested using Postman, a popular API development and testing tool.


Features
<br>
1. Encode Input: Converts user-provided input (number or string) into Base64 format.
2. Decode Input: Decodes Base64-encoded strings back into their original format.
3. Flask Framework: The API is built using Flask, a lightweight and flexible Python web framework.
4. Postman Integration: The API can be easily tested and interacted with using Postman.
5. User-Friendly API: The API takes JSON input and returns JSON output for easy integration with various applications.

How It Works
<br>

Encoding: The API accepts a number or string from the user, encodes it into Base64 format, and returns the encoded result.
<br>
Decoding: If the user provides a Base64-encoded string, the API decodes it back into its original form and returns the decoded result.


Postman Usage
<br>

Postman is used to test the API by sending HTTP requests and receiving responses. Users can perform the following actions:

1. Send a POST request with input to encode into Base64.
2. Send a POST request with Base64 input to decode it back to its original form.

