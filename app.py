from flask import Flask
from flask_cors import CORS
from functions.getTicket import get_data_from_database
from dotenv import load_dotenv

load_dotenv()

app =Flask(__name__)
CORS(app)

@app.route('/api/downloads-tickets', method=['GET'])
def display_tickets():
    data = get_data_from_database()

    print(data)

    return str(data), 200



if __name__ == '__main__':
    app.run(debug=True)
