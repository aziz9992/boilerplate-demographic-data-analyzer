import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts().values

    # What is the average age of men?
    male_df = df[df['sex'] == 'Male']
    average_age_men = round(male_df['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_people = df.shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_income_advanced_edu = advanced_education[advanced_education['salary'] == '>50K']
    total_advanced_edu = advanced_education.shape[0]
    high_income_count = high_income_advanced_edu.shape[0]
    advanced_education = ["Bachelors", "Masters", "Doctorate"]
    without_advanced_edu_rich = df[(~df['education'].isin(advanced_education)) & (df['salary'] == '>50K')]
    without_advanced_edu = df[~df['education'].isin(advanced_education)]
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = round((high_income_count / total_advanced_edu) * 100, 1)
    lower_education_rich = round((len(without_advanced_edu_rich) / len(without_advanced_edu)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_per_week = df['hours-per-week'].min()
    min_hours_df = df[df['hours-per-week'] == min_hours_per_week]
    total_min_hours = min_hours_df.shape[0]
    num_min_workers = min_hours_df[min_hours_df['salary'] == '>50K'].shape[0]

    rich_percentage = round((num_min_workers / total_min_hours) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    total_people_by_country = df['native-country'].value_counts()
    high_income_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    percentage_high_income_by_country = (high_income_by_country / total_people_by_country) * 100
    highest_earning_country = percentage_high_income_by_country.idxmax()
    highest_earning_country_percentage = round(percentage_high_income_by_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_income_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = high_income_india['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
