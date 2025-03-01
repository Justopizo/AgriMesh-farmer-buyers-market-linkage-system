import os
import csv
import psycopg2

def save_to_csv(file_name):
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
        query = ("SELECT productname, buyername, price FROM vieworders")
        cursor.execute(query)
        records = cursor.fetchall()
        
        cursor.close()
        conn.close()

        # Save data to CSV
        file_path = os.path.abspath(file_name)
        headers = ["Product Name", "Buyer Name", "Price"]

        with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)  
            writer.writerows(records)  

        
        return file_path  

    except Exception as e:
        print("Error:", e)
        return None
