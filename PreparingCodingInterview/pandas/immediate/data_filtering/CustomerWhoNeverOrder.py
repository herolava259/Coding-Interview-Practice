import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = customers.merge(orders, how="left", left_on="id", right_on="customerId")
    never_buy_customers = merged_df[merged_df["customerId"].isna()]

    return never_buy_customers[['name']].rename(columns={"name": "Customers"})


if __name__ == "__main__":
    data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
    df_customer = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[1, 3], [2, 1]]
    df_order = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})

    print(find_customers(df_customer, df_order))
