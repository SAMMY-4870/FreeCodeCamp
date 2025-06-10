import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4. Advanced education filter
    advanced_edu = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced_edu)]
    lower_edu = df[~df['education'].isin(advanced_edu)]

    # 5. Percentage of higher education >50K
    higher_edu_rich = round((higher_edu[higher_edu['salary'] == '>50K'].shape[0] / higher_edu.shape[0]) * 100, 1)

    # 6. Percentage of lower education >50K
    lower_edu_rich = round((lower_edu[lower_edu['salary'] == '>50K'].shape[0] / lower_edu.shape[0]) * 100, 1)

    # 7. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 8. % of rich among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers_percent = round((min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100, 1)

    # 9. Country with highest % of >50K earners
    country_counts = df['native-country'].value_counts()
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_country_percent = (rich_by_country / country_counts * 100).dropna()
    highest_earning_country = rich_country_percent.idxmax()
    highest_earning_country_percentage = round(rich_country_percent.max(), 1)

    # 10. Top occupation in India for >50K
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Return the results in a dictionary
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_edu_rich)
        print("Percentage without higher education that earn >50K:", lower_edu_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % among min workers:", rich_min_workers_percent)
        print("Country with highest % rich:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_min_workers_percent,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
