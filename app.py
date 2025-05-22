import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit configuration
st.set_page_config(page_title="Mental Health Insights", layout="wide")
sns.set(style="whitegrid")

# Load dataset from GitHub (replace this URL with your own raw CSV link)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/shayrokban/midtermnew/refs/heads/main/mental_health_dataset%20(1).csv"
    return pd.read_csv(url)

# Load the data
df = load_data()

# Create age group bins
df['age_group'] = pd.cut(df['age'], bins=[18, 25, 35, 45, 55, 65],
                         labels=['18–25', '26–35', '36–45', '46–55', '56–65'])

# Title
st.title("🧠 Mental Health Data Insights")

# -------- INSIGHT 1: Distributions --------
st.header("🔍 Insight 1: Distributions of Key Variables")
numeric_vars = ['age', 'stress_level', 'sleep_hours', 'depression_score', 'productivity_score']
for var in numeric_vars:
    fig, ax = plt.subplots()
    sns.histplot(data=df, x=var, kde=True, bins=30, color='steelblue', ax=ax)
    ax.set_title(f'Distribution of {var}')
    ax.set_xlabel(var)
    ax.set_ylabel('Count')
    st.pyplot(fig)

# -------- INSIGHT 2: Depression Score by Gender --------
st.header("🔍 Insight 2: Depression Score Distribution by Gender")
fig, ax = plt.subplots()
sns.histplot(data=df, x='depression_score', hue='gender', kde=True, bins=30, multiple='stack', ax=ax)
ax.set_title('Depression Score by Gender')
ax.set_xlabel('Depression Score')
ax.set_ylabel('Count')
st.pyplot(fig)

# -------- INSIGHT 3: Sleep vs. Stress --------
st.header("🔍 Insight 3: Sleep Hours vs. Stress Level")
fig, ax = plt.subplots()
sns.regplot(data=df, x='sleep_hours', y='stress_level', scatter_kws={'alpha':0.3}, ax=ax)
ax.set_title('Stress Level vs. Sleep Hours')
ax.set_xlabel('Sleep Hours')
ax.set_ylabel('Stress Level')
st.pyplot(fig)

# -------- INSIGHT 4: Sleep Hours by Treatment Seeking --------
st.header("🔍 Insight 4: Sleep Hours by Treatment Seeking")
fig, ax = plt.subplots()
sns.barplot(data=df, x='seeks_treatment', y='sleep_hours', ci='sd', ax=ax)
ax.set_title('Average Sleep Hours by Treatment Seeking')
ax.set_xlabel('Seeks Treatment')
ax.set_ylabel('Average Sleep Hours')
st.pyplot(fig)

# -------- INSIGHT 5: Depression Score by Gender --------
st.header("🔍 Insight 5: Depression Score by Gender")
fig, ax = plt.subplots()
sns.boxplot(data=df, x='gender', y='depression_score', ax=ax)
ax.set_title('Depression Score by Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Depression Score')
plt.xticks(rotation=45)
st.pyplot(fig)

# -------- INSIGHT 6: Depression by Age Group --------
st.header("🔍 Insight 6: Depression Score by Age Group")
fig, ax = plt.subplots()
sns.barplot(data=df, x='age_group', y='depression_score', ci='sd', ax=ax)
ax.set_title('Average Depression Score by Age Group')
ax.set_xlabel('Age Group')
ax.set_ylabel('Depression Score')
st.pyplot(fig)

# -------- INSIGHT 7: Productivity and Age --------
st.header("🔍 Insight 7: Productivity Score vs. Age")
fig, ax = plt.subplots()
sns.regplot(data=df, x='age', y='productivity_score', scatter_kws={'alpha':0.2}, ax=ax)
ax.set_title('Productivity Score vs. Age')
ax.set_xlabel('Age')
ax.set_ylabel('Productivity Score')
st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
