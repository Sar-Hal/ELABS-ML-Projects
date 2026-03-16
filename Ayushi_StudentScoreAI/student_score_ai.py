import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Load Data
data = pd.read_csv("student-math.csv", sep=';')

# 2. Yeh line terminal mein check karein (Spelling verify karne ke liye)
print("Apki file ke columns ye hain:", data.columns.tolist())

# 3. Agar niche error aaye, toh upar wali list se spelling match karein
X = data[['studytime', 'absences', 'failures']] 
y = data['G3']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("R2 Score:", r2_score(y_test, predictions))