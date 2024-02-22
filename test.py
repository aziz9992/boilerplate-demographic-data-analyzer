import pandas as pd
df = pd.read_csv('adult.data.csv')
print(df.head())
# Count the number of people for each race
race_counts = df['race'].value_counts().values.tolist()

print("race counts:" ,race_counts)
#print(race_counts)
# Filter the DataFrame to include only rows where the gender is 'male'
male_df = df[df['sex'] == 'Male']

# Calculate the average age of men
average_age_men = round(male_df['age'].mean(), 1)

print("Average age of men:", average_age_men)
# Count the number of people who have a Bachelor's degree
bachelors_count = df[df['education'] == 'Bachelors'].shape[0]

# Calculate the total number of people in the dataset
total_people = df.shape[0]

# Calculate the percentage of people who have a Bachelor's degree
percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

print("Percentage of people with a Bachelor's degree:", percentage_bachelors)

# Filter the DataFrame to include only rows with advanced education and income > 50K
advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
high_income_advanced_edu = advanced_education[advanced_education['salary'] == '>50K']

# Calculate the total number of people with advanced education
total_advanced_edu = advanced_education.shape[0]

# Calculate the number of people with advanced education and income > 50K
high_income_count = high_income_advanced_edu.shape[0]

# Calculate the percentage
percentage_high_income = round((high_income_count / total_advanced_edu) * 100, 1)

print("Percentage of people with advanced education earning more than 50K:", percentage_high_income)

# Find the minimum number of hours a person works per week
min_hours_per_week = df['hours-per-week'].min()

print("Minimum number of hours a person works per week:", min_hours_per_week)

# Find the minimum number of hours a person works per week
min_hours_per_week = df['hours-per-week'].min()

# Filter the DataFrame to include only rows where the hours-per-week equals the minimum
min_hours_df = df[df['hours-per-week'] == min_hours_per_week]

# Calculate the total number of people who work the minimum hours per week
total_min_hours = min_hours_df.shape[0]

# Calculate the number of people who work the minimum hours per week and have a salary >50K
high_income_min_hours = min_hours_df[min_hours_df['salary'] == '>50K'].shape[0]

# Calculate the percentage
percentage_high_income_min_hours = round((high_income_min_hours / total_min_hours) * 100, 1)

print("Percentage of people who work the minimum hours per week and have a salary >50K:", percentage_high_income_min_hours)

# Calculate the total number of people in each country
total_people_by_country = df['native-country'].value_counts()

# Calculate the number of people earning >50K in each country
high_income_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()

# Calculate the percentage of people earning >50K in each country
percentage_high_income_by_country = (high_income_by_country / total_people_by_country) * 100

# Find the country with the highest percentage of people earning >50K
highest_percentage_country = percentage_high_income_by_country.idxmax()
highest_percentage = percentage_high_income_by_country.max()

print("Country with the highest percentage of people earning >50K:", highest_percentage_country)
print("Percentage:", round(highest_percentage, 1))

# Filter the DataFrame to include only rows where income >50K and native country is India
high_income_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]

# Find the most popular occupation among those earning >50K in India
most_popular_occupation = high_income_india['occupation'].mode()[0]

print("Most popular occupation for those earning >50K in India:", most_popular_occupation)

# Filter the DataFrame to include only rows without higher education
no_higher_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

# Calculate the total number of people without higher education
total_no_higher_edu = no_higher_edu.shape[0]

# Calculate the number of people without higher education who earn >50K
high_income_no_higher_edu = no_higher_edu[no_higher_edu['salary'] == '>50K'].shape[0]

# Calculate the percentage
percentage_high_income_no_higher_edu = round((high_income_no_higher_edu / total_no_higher_edu) * 100, 1)

print("Percentage of people without higher education earning >50K:", percentage_high_income_no_higher_edu)

# Define advanced education as having a bachelor's degree or higher
advanced_education = ["Bachelors", "Masters", "Doctorate"]

# Filter the DataFrame for people without advanced education and with income > 50K
without_advanced_edu_rich = df[(~df['education'].isin(advanced_education)) & (df['salary'] == '>50K')]

# Filter the DataFrame for people without advanced education
without_advanced_edu = df[~df['education'].isin(advanced_education)]

# Calculate the percentage
percentage = round((len(without_advanced_edu_rich) / len(without_advanced_edu)) * 100, 1)

print(f"The percentage of people without advanced education making more than 50K is: {percentage:.2f}%")