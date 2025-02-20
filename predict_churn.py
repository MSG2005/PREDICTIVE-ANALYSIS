import pandas as pd

# Load the dataset
file_path = "Bank_Churn.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
df.info()

