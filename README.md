# SKY-SQL-2

SKY-SQL-2 is a Python-based flight reporting tool that allows you to query flight data, visualize delays, and export results to CSV files. It is designed to work with a local SQLite database and provides both terminal-based interaction and data visualization.

---

## Features

- Query flights by ID or date
- List delayed flights by airline or origin airport
- Export query results to CSV files
- Visualize flight delays:
  - Percentage of delayed flights per airline
  - Percentage of delayed flights per hour
  - Heatmap of delayed flights per route
  - (Optional) Map of delayed flights per route
- Modular code structure:
  - `main.py` – user interface and menu
  - `flights_data.py` – database access layer
  - `flight_plots.py` – plotting functions
  - `data/` – SQLite database and exported CSV files

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SKY-SQL-2.git
   cd SKY-SQL-2

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate

3. Install required packages:
   ```bash
   pip install -r requirements.txt

---

## Usage

- Run the main program:
    ```bash
     python main.py


## Menu Options

1. Show flight by ID – Enter a flight ID to see details.
2. Show flights by date – Enter a date in DD/MM/YYYY format.
3. Delayed flights by airline – Enter airline name (partial match allowed).
4. Delayed flights by origin airport – Enter a 3-letter IATA airport code.
5. Plot delayed flights per airline – Creates a bar chart and saves to data/.
6. Plot delayed flights per hour – Creates a bar chart and saves to data/.
7. Heatmap of delayed flights per route – Creates a heatmap and saves to data/.
8. Exit – Quit the program.

After queries, you can choose to export results to a CSV file, which will be saved in the data/ folder.


## Testing

- Run the unit tests:
    ```bash
    pytest tests/


