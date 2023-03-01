from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the request data
    data = request.json
    print('yes')
    print(data)

    # Process the webhook data here
    # ...

    # Return a response
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
