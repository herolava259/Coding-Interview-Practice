
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(department, how="inner", left_on = "departmentId", right_on="id")

    satisfy_df = merged_df.loc[merged_df.groupby("departmentId")["salary"].transform("max") == merged_df["salary"]]

    return satisfy_df.rename(columns={"name_x": "Employee", "name_y": "Department", "salary": "Salary"})[["Department", "Employee", "Salary"]]