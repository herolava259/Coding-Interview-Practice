import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    conditions_msk = patients['conditions'].str.contains(r'(^| )DIAB1')

    return patients.loc[conditions_msk, ['patient_id', 'patient_name', 'conditions']]


if __name__ == '__main__':
    data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'],
            [5, 'Alain', 'DIAB201']]
    patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype(
        {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})

    print(find_patients(patients))