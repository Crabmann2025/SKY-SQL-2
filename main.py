import flights_data
from datetime import datetime
import sqlalchemy
import os
import csv

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
        delay = int(result['DELAY']) if result['DELAY'] else 0
        origin = result['ORIGIN_AIRPORT']
        dest = result['DESTINATION_AIRPORT']
        airline = result['AIRLINE']

        if delay and delay > 0:
            print(f"{result['ID']}. {origin} -> {dest} by {airline}, Delay: {delay} Minutes")
        else:
            print(f"{result['ID']}. {origin} -> {dest} by {airline}")

    # CSV export
    export = input("\nDo you want to export these results to a CSV file? (y/n): ").strip().lower()
    if export == 'y':
        # Ensure 'data' folder exists
        data_folder = os.path.join(os.path.dirname(__file__), "data")
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        filename_input = input("Enter the filename (without extension, e.g., flights): ").strip()
        filename = os.path.join(data_folder, f"{filename_input}.csv")

        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['ID', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'AIRLINE', 'DELAY']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for result in results:
                    writer.writerow({
                        'ID': result['ID'],
                        'ORIGIN_AIRPORT': result['ORIGIN_AIRPORT'],
                        'DESTINATION_AIRPORT': result['DESTINATION_AIRPORT'],
                        'AIRLINE': result['AIRLINE'],
                        'DELAY': result['DELAY'] if result['DELAY'] else 0
                    })
            print(f"Data successfully saved to {filename}!")
        except Exception as e:
            print("Error saving CSV file:", e)

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
