import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("titanic.csv")

# Copy dataset
data = df.copy()

# Drop kolom tidak relevan
data = data.drop(
    columns=[
        "PassengerId",
        "Name",
        "Ticket",
        "Cabin"
    ]
)

# Handle missing value
data["Age"] = data["Age"].fillna(
    data["Age"].median()
)

data["Embarked"] = data["Embarked"].fillna(
    data["Embarked"].mode()[0]
)

# Encoding
le = LabelEncoder()

data["Sex"] = le.fit_transform(
    data["Sex"]
)

data["Embarked"] = le.fit_transform(
    data["Embarked"]
)

# Save hasil preprocessing
data.to_csv(
    "titanic_preprocessing.csv",
    index=False
)

print("Preprocessing selesai")
print("Shape:", data.shape)