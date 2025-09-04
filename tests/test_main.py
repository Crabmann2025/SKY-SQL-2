# test_main.py
import flights_data


def test_flight_by_id():
    print("\n=== Test: flight_by_id ===")
    # Teste mit einer bekannten ID aus deiner DB
    test_id = 2
    results = flights_data.get_flight_by_id(test_id)
    for r in results:
        print(dict(r))

def test_flights_by_date():
    print("\n=== Test: flights_by_date ===")
    # Teste ein Datum aus deiner DB
    day, month, year = 1, 1, 2015
    results = flights_data.get_flights_by_date(day, month, year)
    for r in results:
        print(dict(r))

def test_delayed_flights_by_airline():
    print("\n=== Test: delayed_flights_by_airline ===")
    # Teste eine bekannte Airline
    airline_name = "Virgin America"
    results = flights_data.get_delayed_flights_by_airline(airline_name)
    for r in results:
        print(dict(r))

def test_delayed_flights_by_airport():
    print("\n=== Test: delayed_flights_by_airport ===")
    # Teste einen Flughafen
    airport_code = "LAX"
    results = flights_data.get_delayed_flights_by_airport(airport_code)
    for r in results:
        print(dict(r))

if __name__ == "__main__":
    test_flight_by_id()
    test_flights_by_date()
    test_delayed_flights_by_airline()
    test_delayed_flights_by_airport()
