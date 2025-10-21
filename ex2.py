import pandas as pd
import ISLP

college = ISLP.load_data("College")

college.columns = college.columns.str.replace('.', '_', regex=False)
college['Acceptance_Rate'] = ((college['Accept'] / college['Apps']) * 100).round(1)
college.sort_values(by=['Private', 'Apps'], ascending=[True, True], inplace=True)
print(college)
