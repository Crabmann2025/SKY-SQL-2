import flights_data
from datetime import datetime
import sqlalchemy

IATA_LENGTH = 3

def delayed_flights_by_airline():
    airline_input = input("Enter airline name: ")
    results = flights_data.get_delayed_flights_by_airline(airline_input)
    print_results(results)

def delayed_flights_by_airport():
    valid = False
    while not valid:
        airport_input = input("Enter origin airport IATA code: ")
        if airport_input.isalpha() and len(airport_input) == IATA_LENGTH:
            valid = True
    results = flights_data.get_delayed_flights_by_airport(airport_input)
    print_results(results)

def flight_by_id():
    valid = False
    while not valid:
        try:
            id_input = int(input("Enter flight ID: "))
        except Exception:
            print("Try again...")
        else:
            valid = True
    results = flights_data.get_flight_by_id(id_input)
    print_results(results)

def flights_by_date():
    valid = False
    while not valid:
        try:
            date_input = input("Enter date in DD/MM/YYYY format: ")
            date = datetime.strptime(date_input, '%d/%m/%Y')
        except ValueError as e:
            print("Try again...", e)
        else:
            valid = True
    results = flights_data.get_flights_by_date(date.day, date.month, date.year)
    print_results(results)

def print_results(results):
    print(f"Got {len(results)} results.")
    for result in results:
        result = result._mapping
        try:
            delay = int(result['DELAY']) if result['DELAY'] else 0
            origin = result['ORIGIN_AIRPORT']
            dest = result['DESTINATION_AIRPORT']
            airline = result['AIRLINE']
        except (ValueError, sqlalchemy.exc.SQLAlchemyError) as e:
            print("Error showing results: ", e)
            return

        if delay and delay > 0:
            print(f"{result['ID']}. {origin} -> {dest} by {airline}, Delay: {delay} Minutes")
        else:
            print(f"{result['ID']}. {origin} -> {dest} by {airline}")

def show_menu_and_get_input():
    print("Menu:")
    for key, value in FUNCTIONS.items():
        print(f"{key}. {value[1]}")

    while True:
        try:
            choice = int(input())
            if choice in FUNCTIONS:
                return FUNCTIONS[choice][0]
        except ValueError:
            pass
        print("Try again...")

FUNCTIONS = {
    1: (flight_by_id, "Show flight by ID"),
    2: (flights_by_date, "Show flights by date"),
    3: (delayed_flights_by_airline, "Delayed flights by airline"),
    4: (delayed_flights_by_airport, "Delayed flights by origin airport"),
    5: (quit, "Exit")
}

def main():
    while True:
        choice_func = show_menu_and_get_input()
        choice_func()

if __name__ == "__main__":
    main()
