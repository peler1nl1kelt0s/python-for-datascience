from matplotlib import pyplot as plt
from load_csv import load

def main():
    try:
        data = load("life_expectancy_years.csv")
        data.set_index("country",inplace=True)
        turkey_data = data.loc["Turkey"]
        turkey_data.plot()
        plt.title("Turkey Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.legend()
        plt.show()
    except FileNotFoundError as msg:
        return
    except Exception as msg:
        print(f"Unexpected error! {msg}")


if __name__ == "__main__":
    main()