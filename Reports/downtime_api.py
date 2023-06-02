from flask import Flask, jsonify
import psycopg2

# app = Flask(__name__)
# app.debug = True #Enable debug mode

# @app.route('/getDowntimeReason', methods=['GET'])
# def get_downtime_details():
#     try:
#         # Establish a connection to the PostgreSQL database
#         conn = psycopg2.connect(
#             host="localhost",
#             database="postgres",
#             user="postgres",
#             password="postgres"
#         )
        
#         # Create a cursor object to interact with the database
#         cursor = conn.cursor()
        
#         # Execute the SQL query
#         cursor.execute("SELECT dt_id, downtime_reason FROM public.downtime_reason;")
        
#         # Fetch all the rows returned by the query
#         rows = cursor.fetchall()
        
#         # Create a list to store machine details
#         downtime_reason = []
        
#         # Iterate over the rows and add machine details to the list
#         downtime_reasons = []  # Create an empty list to store downtime reasons

#         for row in rows:
#             dt_id = row[0]
#             dt_reason = row[1]
#             downtime_reasons.append({
#                 "dt_id": dt_id,
#                 "dt_reason": dt_reason
#              })
        
#         # Close the cursor and the database connection
#         cursor.close()
#         conn.close()
        
#         # Return the downtime details as a JSON response
#         return jsonify(downtime_reason)
    
#     except psycopg2.Error as e:
#         return jsonify({"error": str(e)})

@app.route('/getMachine', methods=['GET'])
def get_machine_details():
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
        
        # Execute the SQL query
        cursor.execute("SELECT machine_id, machine_name FROM public.machine;")
        
        # Fetch all the rows returned by the query
        rows = cursor.fetchall()
        
        # Create a list to store machine details
        machines = []
        
        # Iterate over the rows and add machine details to the list
        for row in rows:
            machine_id = row[0]
            machine_name = row[1]
            # Add more variables as per your machine details table structure
            machines.append({
                "Machine ID": machine_id,
                "Machine Name": machine_name
            })
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
        
        # Return the machine details as a JSON response
        return jsonify(machines)
    
    except psycopg2.Error as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    # Run the Flask app on port 8080
    app.run(port=8080)

