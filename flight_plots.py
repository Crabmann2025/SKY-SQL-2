import flights_data
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Nicht-interaktives Backend, damit Tkinter nicht benötigt wird
matplotlib.use('Agg')

# Ordner für gespeicherte Plots
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

def delayed_percentage_per_airline():
    """Bar chart: percentage of delayed flights per airline"""
    results = flights_data.get_all_flights()
    df = pd.DataFrame(results)

    df['DELAYED'] = df['DELAY'] >= 20
    grouped = df.groupby('AIRLINE')['DELAYED'].mean().sort_values(ascending=False) * 100

    plt.figure(figsize=(12,6))
    sns.barplot(x=grouped.index, y=grouped.values, palette="viridis")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Percentage of Delayed Flights (%)")
    plt.title("Percentage of Delayed Flights per Airline")
    plt.tight_layout()
    filename = os.path.join(DATA_FOLDER, "delayed_per_airline.png")
    plt.savefig(filename)
    plt.close()
    print(f"Plot saved to {filename}")

def delayed_percentage_per_hour():
    """Bar chart: percentage of delayed flights per hour of the day"""
    results = flights_data.get_all_flights()
    df = pd.DataFrame(results)

    # Stunden simulieren aus ID, falls keine reale Stunde vorhanden
    df['HOUR'] = df['ID'] % 24
    df['DELAYED'] = df['DELAY'] >= 20

    grouped = df.groupby('HOUR')['DELAYED'].mean() * 100

    plt.figure(figsize=(10,5))
    sns.barplot(x=grouped.index, y=grouped.values, palette="coolwarm")
    plt.xlabel("Hour of Day")
    plt.ylabel("Percentage of Delayed Flights (%)")
    plt.title("Percentage of Delayed Flights per Hour")
    plt.tight_layout()
    filename = os.path.join(DATA_FOLDER, "delayed_per_hour.png")
    plt.savefig(filename)
    plt.close()
    print(f"Plot saved to {filename}")

def delayed_heatmap_routes():
    """Heatmap: percentage of delayed flights per route (Origin -> Destination)"""
    results = flights_data.get_all_flights()
    df = pd.DataFrame(results)

    df['DELAYED'] = df['DELAY'] >= 20
    pivot = df.pivot_table(index='ORIGIN_AIRPORT', columns='DESTINATION_AIRPORT',
                           values='DELAYED', aggfunc='mean') * 100

    plt.figure(figsize=(12,10))
    sns.heatmap(pivot, cmap="Reds", linewidths=0.5, annot=False)
    plt.title("Percentage of Delayed Flights per Route (Origin -> Destination)")
    plt.ylabel("Origin Airport")
    plt.xlabel("Destination Airport")
    plt.tight_layout()
    filename = os.path.join(DATA_FOLDER, "delayed_routes_heatmap.png")
    plt.savefig(filename)
    plt.close()
    print(f"Heatmap saved to {filename}")
