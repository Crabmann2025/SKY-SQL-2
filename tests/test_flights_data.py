# test_flights_data.py
import flights_data


def test_get_flight_by_id():
    print("\n=== Test: get_flight_by_id ===")
    test_id = 2  # Beispiel-ID aus deiner DB
    results = flights_data.get_flight_by_id(test_id)
    for r in results:
        print(dict(r))

def test_get_flights_by_date():
    print("\n=== Test: get_flights_by_date ===")
    day, month, year = 1, 1, 2015  # Beispiel-Datum aus deiner DB
    results = flights_data.get_flights_by_date(day, month, year)
    for r in results:
        print(dict(r))

def test_get_delayed_flights_by_airline():
    print("\n=== Test: get_delayed_flights_by_airline ===")
    airline_name = "Virgin America"  # Beispiel-Airline
    results = flights_data.get_delayed_flights_by_airline(airline_name)
    for r in results:
        print(dict(r))

def test_get_delayed_flights_by_airport():
    print("\n=== Test: get_delayed_flights_by_airport ===")
    airport_code = "LAX"  # Beispiel-Airport
    results = flights_data.get_delayed_flights_by_airport(airport_code)
    for r in results:
        print(dict(r))

if __name__ == "__main__":
    test_get_flight_by_id()
    test_get_flights_by_date()
    test_get_delayed_flights_by_airline()
    test_get_delayed_flights_by_airport()
