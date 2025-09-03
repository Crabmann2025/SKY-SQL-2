from sqlalchemy import create_engine, text

# Queries
QUERY_FLIGHT_BY_ID = """
    SELECT flights.ID as ID,
           flights.ORIGIN_AIRPORT,
           flights.DESTINATION_AIRPORT,
           airlines.AIRLINE,
           flights.DEPARTURE_DELAY as DELAY
    FROM flights
    JOIN airlines ON flights.AIRLINE = airlines.ID
    WHERE flights.ID = :id
"""

QUERY_FLIGHTS_BY_DATE = """
    SELECT flights.ID as ID,
           flights.ORIGIN_AIRPORT,
           flights.DESTINATION_AIRPORT,
           airlines.AIRLINE,
           flights.DEPARTURE_DELAY as DELAY
    FROM flights
    JOIN airlines ON flights.AIRLINE = airlines.ID
    WHERE strftime('%d', flights.DATE) = :day
      AND strftime('%m', flights.DATE) = :month
      AND strftime('%Y', flights.DATE) = :year
"""

QUERY_DELAYED_BY_AIRLINE = """
    SELECT flights.ID as ID,
           flights.ORIGIN_AIRPORT,
           flights.DESTINATION_AIRPORT,
           airlines.AIRLINE,
           flights.DEPARTURE_DELAY as DELAY
    FROM flights
    JOIN airlines ON flights.AIRLINE = airlines.ID
    WHERE airlines.AIRLINE LIKE :airline
      AND flights.DEPARTURE_DELAY >= 20
"""

QUERY_DELAYED_BY_AIRPORT = """
    SELECT flights.ID as ID,
           flights.ORIGIN_AIRPORT,
           flights.DESTINATION_AIRPORT,
           airlines.AIRLINE,
           flights.DEPARTURE_DELAY as DELAY
    FROM flights
    JOIN airlines ON flights.AIRLINE = airlines.ID
    WHERE flights.ORIGIN_AIRPORT = :airport
      AND flights.DEPARTURE_DELAY >= 20
"""

# DB setup
DATABASE_URL = "sqlite:///data/flights.sqlite3"
engine = create_engine(DATABASE_URL)


def execute_query(query, params):
    """
    Execute an SQL query with the params provided in a dictionary,
    and return a list of records (dictionary-like objects).
    """
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), params)
            return result.fetchall()
    except Exception as e:
        print("Query error:", e)
        return []


def get_flight_by_id(flight_id):
    params = {"id": flight_id}
    return execute_query(QUERY_FLIGHT_BY_ID, params)


def get_flights_by_date(day, month, year):
    params = {"day": f"{day:02}", "month": f"{month:02}", "year": str(year)}
    return execute_query(QUERY_FLIGHTS_BY_DATE, params)


def get_delayed_flights_by_airline(airline_name):
    params = {"airline": f"%{airline_name}%"}
    return execute_query(QUERY_DELAYED_BY_AIRLINE, params)


def get_delayed_flights_by_airport(airport_code):
    params = {"airport": airport_code.upper()}
    return execute_query(QUERY_DELAYED_BY_AIRPORT, params)
