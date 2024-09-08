import pandas as pd


def convert_to_json(excel_file):
    df = pd.read_excel(excel_file)
    data = df.to_json(orient='records')
    return data


def convert_to_csv(excel_file):
    df = pd.read_excel(excel_file)
    data = df.to_csv(index=False)
    return data
