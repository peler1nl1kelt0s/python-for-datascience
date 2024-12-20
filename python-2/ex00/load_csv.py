import pandas as pd

def load(path: str) -> pd.DataFrame:
    """
    This function gets the csv path and 
    convert to dataframe with pandas.
    After that print shape of data and
    return the data values.
    """
    if (isinstance(path,str) == False):
        return None
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions",data.shape)
        return data
    except FileNotFoundError as msg:
        print("Csv file not found!")
    except Exception as msg:
        print(Exception.__name__ + ": " + msg)
