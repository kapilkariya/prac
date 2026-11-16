# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("Churn_Modelling.csv")

# Preprocessing
data = data.dropna()

# Select input and output
x = data[["RowNumber", "CustomerId", "Surname", "Exited"]]
y = data["Exited"]

# Convert text into numbers
x=pd.get_dummies(x)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Neural Network
nn = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=500, random_state=42)
nn.fit(X_train, y_train)    
p = nn.predict(X_test)

# Check accuracy
print("Neural Network Accuracy:", accuracy_score(y_test, p))