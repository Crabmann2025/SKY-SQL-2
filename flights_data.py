import sqlite3
import os

# Absoluter Pfad zur Datenbank im Unterordner "data"
DB_FILE = os.path.join(os.path.dirname(__file__), "data", "flights.sqlite3")


def execute_query(query, params=None):
    """
    Führt eine SQL-Abfrage auf der SQLite-Datenbank aus.
    Gibt die Ergebnisse als Liste von Row-Objekten zurück.
    """
    global conn
    results = []
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row  # Zugriff per Spaltenname
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
    return results


def get_flight_by_id(flight_id):
    query = """
        SELECT f.ID, f.ORIGIN_AIRPORT, f.DESTINATION_AIRPORT,
               a.AIRLINE, f.DEPARTURE_DELAY AS DELAY
        FROM flights f
        JOIN airlines a ON f.AIRLINE = a.ID
        WHERE f.ID = :flight_id
    """
    return execute_query(query, {"flight_id": flight_id})


def get_flights_by_date(day, month, year):
    query = """
        SELECT f.ID, f.ORIGIN_AIRPORT, f.DESTINATION_AIRPORT,
               a.AIRLINE, f.DEPARTURE_DELAY AS DELAY
        FROM flights f
        JOIN airlines a ON f.AIRLINE = a.ID
        WHERE f.YEAR = :year
          AND f.MONTH = :month
          AND f.DAY = :day
    """
    return execute_query(query, {"year": year, "month": month, "day": day})


def get_delayed_flights_by_airline(airline_name):
    query = """
        SELECT f.ID, f.ORIGIN_AIRPORT, f.DESTINATION_AIRPORT,
               a.AIRLINE, f.DEPARTURE_DELAY AS DELAY
        FROM flights f
        JOIN airlines a ON f.AIRLINE = a.ID
        WHERE a.AIRLINE LIKE :airline
          AND f.DEPARTURE_DELAY >= 20
    """
    # % für LIKE-Matching hinzufügen
    return execute_query(query, {"airline": f"%{airline_name}%"})


def get_delayed_flights_by_airport(airport_code):
    query = """
        SELECT f.ID, f.ORIGIN_AIRPORT, f.DESTINATION_AIRPORT,
               a.AIRLINE, f.DEPARTURE_DELAY AS DELAY
        FROM flights f
        JOIN airlines a ON f.AIRLINE = a.ID
        WHERE f.ORIGIN_AIRPORT = :airport
          AND f.DEPARTURE_DELAY >= 20
    """
    return execute_query(query, {"airport": airport_code.upper()})
