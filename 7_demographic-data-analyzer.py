import pandas as pd
from pandas import Series, DataFrame


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r"adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = df.groupby('race', sort=False)['race'].count()
    race_count = pd.Series(race)

    # What is the average age of men?
    avg_man = df['age'].groupby(df['sex']).mean()
    average_age_men = round(avg_man['Male'],1)

    # What is the percentage of people who have a Bachelor's degree?
    total_education = df['education'].count()
    bachelor = df['education'].groupby(df['education']=='Bachelors').count()
    result_bachelor = bachelor[True]

    percentage_bachelors = round(result_bachelor/total_education,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    pay_condition = (df['salary']=='>=50K') | (df['salary']=='>50K')

    high_education_condition = (df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')
    high_education = df['education'].groupby(high_education_condition).count()
    high_education_pay = df['salary'].groupby(high_education_condition & pay_condition)



    # What percentage of people without advanced education make more than 50K?

    low_education_condition = ~(df['education']=='Bachelors') & ~(df['education']=='Masters') & ~(df['education']=='Doctorate')
    low_education = df['education'].groupby(low_education_condition)
    low_education_pay = df['salary'].groupby(low_education_condition & pay_condition)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education =  high_education[True]
    lower_education = low_education[True]

    # percentage with salary >50K
    # caution : salary's type is not int but string
    higher_education_rich = round(high_education_pay/high_education,1)
    lower_education_rich = round(low_education_pay/low_education,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

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
