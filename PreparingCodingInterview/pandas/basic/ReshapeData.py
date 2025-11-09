import pandas as pd
import numpy as np

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=["product"],
                   value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
                   var_name = "quarter", value_name="sales")


if __name__ == "__main__":
    df = pd.DataFrame(np.array([["Umbrella", 417, 224, 379, 611],
                                 ["SleepingBag", 800, 936, 93, 875]])
                      , columns = ["product", "quarter_1", "quarter_2", "quarter_3", "quarter_4"])

    print(df)
    print(meltTable(df))