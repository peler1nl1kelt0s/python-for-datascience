from matplotlib import pyplot as plt
from load_csv import load

def main():
    data = load("life_expectancy_years.csv")
    data.set_index("country", inplace=True)
    data = data.loc["Turkey"]
    data.plot()
    plt.title("Turkey Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()