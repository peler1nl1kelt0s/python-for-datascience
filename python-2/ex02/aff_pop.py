from load_csv import load
from matplotlib import pyplot as plt
import pandas as pd


def main():
    """
    Main function to load, process, and plot population
    data for Turkey and France.
    """
    try:
        data = load("population_total.csv")
        if data is None:
            raise FileNotFoundError("CSV file not found \
                                    or could not be loaded.")
        data.set_index("country", inplace=True)
        data = pd.concat([data.loc["Turkey", "1800":"2050"],
                          data.loc["Germany", "1800":"2050"]], axis=1)
        data.index = data.index.astype(int)
        data["Turkey"] = pd.to_numeric(data["Turkey"].str.replace("M", ""),
                                       errors='coerce')
        data["Germany"] = pd.to_numeric(data["Germany"].str.replace("M", ""),
                                        errors='coerce')
        data["Turkey"] = data["Turkey"] * 1000000
        data["Germany"] = data["Germany"] * 1000000
        fig, ax = plt.subplots(figsize=(8, 6))
        data["Turkey"].plot(ax=ax, label="Turkey")
        data["Germany"].plot(ax=ax, label="Germany")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.yticks([20000000, 40000000, 60000000, 80000000, 100000000],
                   ["20M", "40M", "60M", "80M", "100M"])
        plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040],
                   ["1800", "1840", "1880", "1920", "1960", "2000", "2040"])
        plt.legend(loc=4)
        plt.show()
    except FileNotFoundError as msg:
        print(f"Error: {msg}")
    except Exception as msg:
        print(f"Unexpected error! {msg}")


if __name__ == "__main__":
    main()
