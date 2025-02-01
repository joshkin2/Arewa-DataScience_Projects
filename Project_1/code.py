import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.ion()
# Import Student Depression Data
df=pd.read_csv('datasets\Student Depression Dataset.csv',index_col=0)
print(df.head(5))
print(df.info())
print(df.describe())
# check missing values in columns
print(df.isnull().sum())
# visualize missing data
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cmap="viridis", cbar=False,yticklabels=False,)
plt.title("Missing Values Heatmap")
#plt.savefig("missing_values_heatmap.png")
print(df.dtypes)
#drop rows with missing values
df.dropna(inplace=True)
print(df['Financial Stress'].value_counts())
# detect relationships and corr btw numerical variables
#sns.pairplot(df)
#plt.savefig("pairplot.png")
# Summary Statistics
print(df.describe(include=['object']))
# count qunique val for categorical variables
cat_cols= ['Gender', 'City', 'Profession', 'Degree', 'Sleep Duration', 'Dietary Habits', 
                    'Have you ever had suicidal thoughts ?', 'Family History of Mental Illness']
for col in cat_cols:
    print(f"\nUnique values in {col}:\n",df[col].value_counts())
import seaborn as sns
import matplotlib.pyplot as plt
num_cols= ['Age', 'Academic Pressure', 'Work Pressure', 'CGPA', 'Study Satisfaction', 
            'Job Satisfaction', 'Work/Study Hours', 'Financial Stress', 'Depression']
plt.figure(figsize=(12,8))
for i, col in enumerate(num_cols):
    plt.subplot(3,3,i+1)
    sns.histplot(df[col],bins=30,kde=True)
    plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig("distribution_plots1.png")
# Check correlations
numeric_cols=df.select_dtypes(include=[np.number])
correlation_matrix= numeric_cols.corr()
#heatmap
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm",vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.savefig("correlation_matrix.png") 