import unittest
import flights_data

class TestFlightsData(unittest.TestCase):

    def test_get_flight_by_id(self):
        results = flights_data.get_flight_by_id(2)
        self.assertTrue(len(results) > 0)
        self.assertIsInstance(results[0], dict)
        self.assertIn('ID', results[0])

    def test_get_flights_by_date(self):
        results = flights_data.get_flights_by_date(1,1,2015)
        self.assertTrue(len(results) > 0)

    def test_get_delayed_flights_by_airline(self):
        results = flights_data.get_delayed_flights_by_airline("Virgin America")
        self.assertTrue(all(r['DELAY'] >= 20 for r in results))

    def test_get_delayed_flights_by_airport(self):
        results = flights_data.get_delayed_flights_by_airport("LAX")
        self.assertTrue(all(r['DELAY'] >= 20 for r in results))

if __name__ == '__main__':
    unittest.main()

