import unittest
import os
import flight_plots

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")

class TestFlightPlots(unittest.TestCase):

    def test_delayed_percentage_per_airline(self):
        flight_plots.delayed_percentage_per_airline()
        self.assertTrue(os.path.exists(os.path.join(DATA_FOLDER, "delayed_per_airline.png")))

    def test_delayed_percentage_per_hour(self):
        flight_plots.delayed_percentage_per_hour()
        self.assertTrue(os.path.exists(os.path.join(DATA_FOLDER, "delayed_per_hour.png")))

    def test_delayed_heatmap_routes(self):
        flight_plots.delayed_heatmap_routes()
        self.assertTrue(os.path.exists(os.path.join(DATA_FOLDER, "delayed_routes_heatmap.png")))

if __name__ == '__main__':
    unittest.main()
