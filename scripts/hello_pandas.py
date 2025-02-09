import pandas as pd

data = pd.read_excel(
    '../data/iris/iris dataset.xlsx',  # location on disk, relative to this file
    header=None,  # this dataset has no headers, so we'll add them manuall;y
)

data.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']

print(data.describe())

# Display the maximum petal length for each species
max_petal_length_by_species = data.groupby('Species')['Petal Length'].max()
print("\nMaximum Petal Length by Species:")
print(max_petal_length_by_species)