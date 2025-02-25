import os
import json
import psycopg2

def save_to_json(file_name):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="3062",
            database="agrimesh"
        )
        cursor = conn.cursor()

        # Fetch data
        query = "SELECT productname, category, quantity, price, location FROM produce"
        cursor.execute(query)
        records = cursor.fetchall()
        
        # Close connection
        cursor.close()
        conn.close()

        # Convert data to JSON format
        data_list = []
        headers = ["productname", "category", "quantity", "price", "location"]
        
        for row in records:
            data_list.append(dict(zip(headers, row)))

        # Save JSON file
        file_path = os.path.abspath(file_name)
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4, ensure_ascii=False)

        return file_path  

    except Exception as e:
        print("Error:", e)
        return None
