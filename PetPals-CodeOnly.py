import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = "https://data.longbeach.gov/api/explore/v2.1/catalog/datasets/animal-shelter-intakes-and-outcomes/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%2C"
df = pd.read_csv(url)

# Handle missing values by filling with the most frequent value
df.fillna(df.mode().iloc[0], inplace=True)

# Keep a copy of the original DataFrame for visualization
df_viz = df.copy()

# Encode categorical variables using OrdinalEncoder
categorical_features = ['Animal Type', 'Sex', 'Primary Color', 'Secondary Color', 'Intake Condition', 'Intake Type', 'Outcome Type']
encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
df[categorical_features] = encoder.fit_transform(df[categorical_features].astype(str))

# Create new features
df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')
df['Intake Date'] = pd.to_datetime(df['Intake Date'], errors='coerce')
df['Age at Intake'] = (df['Intake Date'] - df['DOB']).dt.days / 365.25

# Fill missing Age at Intake values with the mean age
df['Age at Intake'].fillna(df['Age at Intake'].mean(), inplace=True)

# Create new features for the visualization DataFrame
df_viz['DOB'] = pd.to_datetime(df_viz['DOB'], errors='coerce')
df_viz['Intake Date'] = pd.to_datetime(df_viz['Intake Date'], errors='coerce')
df_viz['Age at Intake'] = (df_viz['Intake Date'] - df_viz['DOB']).dt.days / 365.25
df_viz['Age at Intake'].fillna(df_viz['Age at Intake'].mean(), inplace=True)

# Distribution of animal types
sns.countplot(data=df_viz, x='Animal Type')
plt.title('Distribution of Animal Types')
plt.xticks(rotation=90)
plt.show()

# Distribution of intake conditions
sns.countplot(data=df_viz, x='Intake Condition')
plt.title('Distribution of Intake Conditions')
plt.xticks(rotation=90)
plt.show()

# Relationship between age at intake and outcome type
sns.boxplot(data=df_viz, x='Outcome Type', y='Age at Intake')
plt.title('Age at Intake vs Outcome Type')
plt.xticks(rotation=90)
plt.show()

# Define features and target
features = ['Animal Type', 'Sex', 'Primary Color', 'Secondary Color', 'Intake Condition', 'Intake Type', 'Age at Intake']
target = 'Outcome Type'

X = df[features]
y = df[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a logistic regression model on the scaled data
model = LogisticRegression(max_iter=5000)
model.fit(X_train_scaled, y_train)

# Make predictions on the scaled test data
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy}')
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()