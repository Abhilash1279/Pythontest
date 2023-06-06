from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)
app.debug = True #Enable debug mode

# PUT API to edit a record in the database table
@app.route('/editData/<str:machine>', methods=['PUT'])
def edit_data(record_id):
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

        # Execute an UPDATE query to edit the record in the table
        query = "UPDATE downtime SET machine = %s, category = %s, reason = %s, sub_reason = %s WHERE id = %s;"
        values = (machine, category, reason, sub_reason, machine)
        cursor.execute(query, values)

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        # Return a success message
        return jsonify({"message": f"Record with ID {machine} edited successfully."})

    except psycopg2.Error as e:
        return jsonify({"error": str(e)})


# DELETE API to delete a record from the database table
@app.route('/deleteData/<str:machine>', methods=['DELETE'])
def delete_data(machine):
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute a DELETE query to remove the record from the table
        query = "DELETE FROM downtime WHERE id = %s;"
        values = (machine,)
        cursor.execute(query, values)

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        # Return a success message
        return jsonify({"message": f"Record with ID {machine} deleted successfully."})

    except psycopg2.Error as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    # Run the Flask app on port 8080
    app.run(port=8080)