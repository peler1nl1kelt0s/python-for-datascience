from matplotlib import pyplot as plt
from load_csv import load


def main():
    """
    Main function gets the csv file with load function where load_csv.py.
    And plot the given data like basic.
    """
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            raise FileNotFoundError()
        data.set_index("country", inplace=True)
        turkey_data = data.loc["Turkey"]
        turkey_data.index = turkey_data.index.astype(int)
        turkey_data.plot()
        plt.title("Turkey Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.yticks([30, 40, 50, 60, 70, 80, 90],
                   ["30", "40", "50", "60", "70", "80", "90"])
        plt.legend()
        plt.show()
    except FileNotFoundError:
        return
    except Exception as msg:
        print(f"Unexpected error! {msg}")


if __name__ == "__main__":
    main()
