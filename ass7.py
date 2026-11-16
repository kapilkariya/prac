# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("spam.csv", encoding="latin-1")

# Select required columns
data = data[["v1", "v2"]]
data.columns = ["label", "message"]

# Preprocessing
data = data.dropna()

# Select input and output
X = data["v1"]
y = data["v2"].map({"ham": 0, "spam": 1})

# Convert text into numbers
cv = CountVectorizer()
X = cv.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
p1 = knn.predict(X_test)

# SVM
svm = SVC()
svm.fit(X_train, y_train)
p2 = svm.predict(X_test)

# Check accuracy
print("KNN Accuracy:", accuracy_score(y_test, p1))
print("SVM Accuracy:", accuracy_score(y_test, p2))