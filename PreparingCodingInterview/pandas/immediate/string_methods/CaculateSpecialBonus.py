import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame)-> pd.DataFrame:
    employees["has_bonus"] = (employees.employee_id % 2) == 1
    employees["has_bonus"] &= ~(employees.name.str.startswith("M"))
    employees["bonus"] = employees["has_bonus"].astype(int) * employees["salary"]

    return employees[["employee_id", "bonus"]].sort_values(by="employee_id")


if __name__ == "__main__":
    data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
    employees_test = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
        {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})

    print(calculate_special_bonus(employees_test))