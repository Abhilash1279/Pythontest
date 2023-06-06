from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)
app.debug = True  # Enable debug mode

# POST API to store data in a new database table
@app.route('/storeData', methods=['POST'])
def store_data():
    try:
        # Retrieve the JSON data from the request
        data = request.json

        # Extract the necessary fields from the JSON data
        machine = data.get('machine')
        category = data.get('category')
        reason = data.get('reason')
        sub_reason = data.get('sub_reason')

        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute an INSERT query to store the data in a new table
        query = "INSERT INTO downtime (machine, category, reason, sub_reason) VALUES (%s, %s, %s, %s);"
        values = (machine, category, reason, sub_reason)
        cursor.execute(query, values)

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        # Return a success message
        return jsonify({"message": "Data stored successfully."})

    except psycopg2.Error as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    # Run the Flask app on port 8080
    app.run(port=8080)