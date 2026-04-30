import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    col_name = f'getNthHighestSalary({N})'

    sorted_salaries = employee['Salary'].sort_values(ascending=False).drop_duplicates()

    return pd.DataFrame({
        col_name: [None if sorted_salaries.size < N or N <= 0 else sorted_salaries.iloc[N-1]]
    })

if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id': 'Int64', 'Salary': 'Int64'})

    print(nth_highest_salary(employee, 2))