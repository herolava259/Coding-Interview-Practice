import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y"), ["product_id"]]

if __name__ == "__main__":
    data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
    df = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype(
        {'product_id': 'int64', 'low_fats': 'category', 'recyclable': 'category'})

    print(find_products(df))