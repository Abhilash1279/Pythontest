from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)
app.debug = True #Enable debug mode

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

if __name__ == '__main__':
     # Run the Flask app on port 8080
     app.run(port=8080)