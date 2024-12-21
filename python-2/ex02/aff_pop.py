from load_csv import load
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def main():
    """
    Main function to load, process, and plot population data for Turkey and France.
    """
    try:
        data = load("population_total.csv")
        if data is None:
            raise FileNotFoundError("CSV file not found or could not be loaded.")
        data.set_index("country", inplace=True)
        data = pd.concat([data.loc["Turkey","1800":"2050"], data.loc["Germany","1800":"2050"]], axis=1)
        data["Turkey"] = pd.to_numeric(data["Turkey"].str.replace("M", ""), errors='coerce')
        data["Germany"] = pd.to_numeric(data["Germany"].str.replace("M", ""), errors='coerce')
        fig, ax = plt.subplots(figsize=(8, 6))
        data["Turkey"].plot(ax=ax, label="Turkey")
        data["Germany"].plot(ax=ax, label="Germany")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population (Millions)")
        plt.xticks()
        plt.xticks(ticks=range())
        plt.legend(loc=4)
        plt.savefig("population_total.jpg")
    except FileNotFoundError as msg:
        print(f"Error: {msg}")
    except Exception as msg:
        print(f"Unexpected error! {msg}")

if __name__ == "__main__":
    main()