import unittest
import flights_data
import main
import os
from unittest.mock import patch

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")

class TestMain(unittest.TestCase):

    def test_get_flight_by_id(self):
        results = flights_data.get_flight_by_id(2)
        self.assertTrue(len(results) > 0)
        row_dict = dict(results[0])
        self.assertIn('ID', row_dict)
        self.assertIn('AIRLINE', row_dict)

    def test_get_flights_by_date(self):
        results = flights_data.get_flights_by_date(1,1,2015)
        self.assertTrue(len(results) > 0)

    def test_get_delayed_flights_by_airline(self):
        results = flights_data.get_delayed_flights_by_airline("Virgin America")
        self.assertTrue(all(r['DELAY'] >= 20 for r in results))

    def test_get_delayed_flights_by_airport(self):
        results = flights_data.get_delayed_flights_by_airport("LAX")
        self.assertTrue(all(r['DELAY'] >= 20 for r in results))

    def test_csv_export_function(self):
        results = flights_data.get_flight_by_id(2)
        filename = os.path.join(DATA_FOLDER, "test_export.csv")
        if os.path.exists(filename):
            os.remove(filename)
        # Mock input für CSV-Export: "n" = nicht speichern
        with patch('builtins.input', side_effect=['n']):
            main.print_results(results)
        # Prüfen, dass die Funktion ausführbar ist
        self.assertTrue(callable(main.print_results))

if __name__ == '__main__':
    unittest.main()
