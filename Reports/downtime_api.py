from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

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

@app.route('/getDowntimeReason', methods=['GET'])
def get_downtime_details():
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
        cursor.execute("SELECT  * FROM public.downtime_reason;")
        
        # Fetch all the rows returned by the query
        rows = cursor.fetchall()
        
        # Create a list to store machine details
        downtime_reasons = []
        
        # Iterate over the rows and add machine details to the list

        for row in rows:
            dt_id = row[0]
            dt_reason = row[1]
            # created_at = row[2]
            # updated_at = row[3]
            # updated_by = row[4]
            
            downtime_reasons.append({
                "dt_id": dt_id,
                "dt_reason": dt_reason,
                # "created_at": created_at,
                # "updated_at": updated_at,
                # "updated_by": updated_by
            })
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
        
        # Return the downtime details as a JSON response
        return jsonify(downtime_reasons)
    
    except psycopg2.Error as e:
        return jsonify({"error": str(e)})

#GET api for downtime sub reason
@app.route('/getDowntimeSubReason', methods=['GET'])
def get_downtime_sub_reason_details():
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
        cursor.execute("SELECT  * FROM public.downtime_sub_reason;")
        
        # Fetch all the rows returned by the query
        rows = cursor.fetchall()
        
        # Create a list to store machine details
        downtime_sub_reasons = []
        
        # Iterate over the rows and add machine details to the list

        for row in rows:
            sub_id = row[0]
            sub_reason = row[1]
            # created_at = row[2]
            # updated_at = row[3]
            # updated_by = row[4]
            
            downtime_sub_reasons.append({
                "sub_id": sub_id,
                "sub_reason": sub_reason,
                # "created_at": created_at,
                # "updated_at": updated_at,
                # "updated_by": updated_by
            })
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
        
        # Return the downtime details as a JSON response  
        return jsonify(downtime_sub_reasons)

    except psycopg2.Error as e:
        return jsonify({"error": str(e)})

@app.route('/getCategories', methods=['GET'])
def get_categories_details():
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
        cursor.execute("SELECT * FROM public.categories;")
        
        # Fetch all the rows returned by the query
        rows = cursor.fetchall()
        
        # Create a list to store machine details
        categories = []
        
        # Iterate over the rows and add machine details to the list

        for row in rows:
            cat_id = row[0]
            category = row[1]
            categories.append({
                "cat_id": cat_id,
                "category": category,
            })
        
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
        
        # Return the downtime details as a JSON response
        return jsonify(categories)
    
    except psycopg2.Error as e:
        return jsonify({"error": str(e)})    

# GET API to retrieve data from the database table
@app.route('/getData', methods=['GET'])
def get_data():
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

        # Execute a SELECT query to fetch data from the table
        query = "SELECT * FROM downtime;"
        cursor.execute(query)

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Create a list to store the retrieved data
        data_list = []

        # Iterate over the rows and add the data to the list
        for row in rows:
            # The table columns are machine, category, reason, and sub_reason
            machine = row[0]
            category = row[1]
            reason = row[2]
            sub_reason = row[3]

            # Create a dictionary representing the row data
            data = {
                "machine": machine,
                "category": category,
                "reason": reason,
                "sub_reason": sub_reason
            }

            # Add the data to the list
            data_list.append(data)

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        # Return the retrieved data as a JSON response
        return jsonify(data_list)

    except psycopg2.Error as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    # Run the Flask app on port 8080
    app.run(port=8080)

