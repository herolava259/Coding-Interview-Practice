import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered_animals = animals[animals["weight"] > 100]
    sorted_animals = filtered_animals.sort_values(by="weight", ascending = False)

    return sorted_animals[["name"]]


if __name__ == "__main__":
    df = pd.DataFrame(data = {"name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
                              "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
                              "age": [98, 50, 6, 45, 100, 26],
                              "weight": [464, 41, 328, 463, 50, 349]})
    print(df)
    print(findHeavyAnimals(df))
