from load_csv import load
from matplotlib import pyplot as plt

def main():
    data = load("population_total.csv")
    data.set_index("country", inplace=True)
    turkey_data = data.loc["Turkey", "1800":"2050"]
    france_data = data.loc["France", "1800":"2050"]

    print(turkey_data.describe())
    # plt.plot(turkey_data)
    # plt.plot(france_data)

    # print(turkey_data)
    # print()
    # plt.legend()
    # plt.xlabel("Year")
    # plt.ylabel("Population")
    # plt.show()

if __name__ == "__main__":
    main()