import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_country_df = world.loc[(world["area"] >= 3000000) | (world["population"] >= 25000000), ["name", "population", "area"]]

    return big_country_df




if __name__ == "__main__":
    data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000],
            ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000],
            ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
    df = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype(
        {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'})

    print(big_countries(df))