import pandas as pd
import ISLP

college = ISLP.load_data("College")

college.columns = college.columns.str.replace('.', '_', regex=False)
college['Acceptance_Rate'] = ((college['Accept'] / college['Apps']) * 100).round(1)
college.sort_values(by=['Private', 'Apps'], ascending=[True, True], inplace=True)
print(college)



college['Elite'] = pd.cut(college['Top10perc'], bins=[0, 50, 100], labels=['Nicht-Elite', 'Elite'])
print(college[['Top10perc', 'Elite']])

print(college.describe())



by_private = (college.groupby("Private", observed=True)[["Acceptance_Rate", "Room_Board", "Books", "PhD", "Grad_Rate"]].mean().round(2))
print("\n=== Means grouped by Private ===")
print(by_private)

by_private_elite = (college.groupby(["Private", "Elite"], observed=True)[["Acceptance_Rate", "Room_Board", "Books", "PhD", "Grad_Rate"]].mean().round(2))
print("\n=== Means grouped by Private and Elite ===")
print(by_private_elite)
