from load_csv import load
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def custom_format(x, _):
    if x < 1000:
        return f"{int(x)}"
    else:
        return f"{int(x/1000)}K"


def main():
    data_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data_life = load("life_expectancy_years.csv")
    
    data_income.set_index("country", inplace=True)
    data_life.set_index("country", inplace=True)

    # data_income.fillna(0, inplace=True)
    # data_life.fillna(0, inplace=True)

    data_income = data_income.loc[:,"1900"]
    data_life = data_life.loc[:,"1900"]
    fig, ax = plt.subplots(figsize=(6, 4))


    plt.scatter(x=data_income,y=data_life)    
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    # plt.tight_layout()
    plt.savefig("life-vs-gross.jpg")
if __name__ == "__main__":
    main()