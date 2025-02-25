import os
import psycopg2
import pandas as pd
import pyautogui

def save_as_screenshot(file_name):
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

        # Convert to Pandas DataFrame for display
        df = pd.DataFrame(records, columns=["Product Name", "Category", "Quantity", "Price", "Location"])
        
        

        # Take a screenshot and save it
        file_path = os.path.abspath(file_name)
        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)

        return file_path  

    except Exception as e:
        print("Error:", e)
        return None
