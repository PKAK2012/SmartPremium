
# 🚗 Smart Premium Prediction Using Gradient Boosting
This project aims to predict insurance premium values using customer demographics, vehicle details, and policy-related information. It utilizes a Gradient Boosting Regressor to forecast premiums based on historical policyholder data.

## 📊 Dataset Overview
Contains fields such as:
- Demographics: Age, Marital Status, Occupation
- Financials: Annual Income, Credit Score
- Policy Info: Vehicle Age, Insurance Duration, Previous Claims
- Feedback & Behavior: Customer Feedback, Health Score

## 🧹 Data Preprocessing
- Removed unneeded columns: `id`, `Policy Start Date`
- Handled missing values:
  - Imputed numericals using **mean** or **median**
  - Imputed categoricals using **random sampling**
- Dropped duplicates
- Categorical variables cleaned and encoded using **LabelEncoder**
- Outliers detected using **IQR (Interquartile Range)** method (no removal)
- Correlation heatmap plotted to identify key numerical relationships

## 💡 Features Used
Key numerical features:
- `Age`
- `Annual Income`
- `Number of Dependents`
- `Health Score`
- `Previous Claims`
- `Vehicle Age`
- `Credit Score`
- `Insurance Duration`

## 🧠 Model: Gradient Boosting Regressor
- Algorithm: `GradientBoostingRegressor` from `sklearn.ensemble`
- Default hyperparameters used (can be tuned later)
- Trained on the cleaned dataset (`x_train`, `y_train`)

```python
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor().fit(x_train, y_train)

## 💾 Model Saving
The trained model was saved using `pickle`:
pickle.dump(model, open("SPM.pkl", "wb"))

## 📚 Skills Demonstrated

- Data Cleaning & Imputation
- Encoding and Feature Engineering
- Outlier Detection
- Correlation Analysis
- Regression Modeling with Gradient Boosting
- Model Serialization (Deployment Ready)

## ✅ Conclusion

The Smart Premium Prediction model can be used to estimate premiums for new customers based on historical trends. This can help insurance companies in:

- Dynamic pricing
- Risk-based premium planning
- Customer targeting for upselling policies

Further performance can be enhanced by:
- Hyperparameter tuning
- Advanced feature engineering
- Including time-based trends from policy start dates
