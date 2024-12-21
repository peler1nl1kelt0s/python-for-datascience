from load_csv import load
from matplotlib import pyplot as plt


def main():
    try:
        inc = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        data_life = load("life_expectancy_years.csv")
        inc.set_index("country", inplace=True)
        data_life.set_index("country", inplace=True)
        inc = inc.loc[:, "1900"]
        data_life = data_life.loc[:, "1900"]
        fig, ax = plt.subplots(figsize=(6, 4))
        plt.scatter(x=inc, y=data_life)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        return
    except Exception as msg:
        print(f"Unexpected error! {msg}")


if __name__ == "__main__":
    main()
