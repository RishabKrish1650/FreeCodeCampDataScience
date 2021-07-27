import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    #How many people of each race are represented in this dataset? 
    race_count=df['race'].value_counts()
    
    #What is the average age of men?
    men=df[df['sex']=='Male']
    ages=men['age'].sum()/len(men['age'])
    average_age_men=round(ages,1)
    
    #What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors=len(df[df['education']=='Bachelors'])/len(df)
    percentage_bachelors*=100
    percentage_bachelors=round(percentage_bachelors,1)

    #What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_ed=df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    higher_education_rich=len(higher_ed[higher_ed['salary']=='>50K'])/len(higher_ed)
    higher_education_rich*=100
    higher_education_rich=round(higher_education_rich,1)
    
    #What percentage of people without advanced education make more than 50K?
    lower_ed=df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education_rich=(len(lower_ed[lower_ed['salary']=='>50K'])/len(lower_ed))*100
    lower_education_rich=round(lower_education_rich,1)
    
    #What is the minimum number of hours a person works per week?
    min_work_hours=min(df['hours-per-week'])
    #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    rich=df[df['hours-per-week']==min_work_hours]
    rich_percentage=(len(rich[rich['salary']=='>50K'])/len(rich))*100

    #What country has the highest percentage of people that earn >50K and what is that percentage?
    high=df[df['salary']=='>50K']
    rich_counts=high['native-country'].value_counts()
    countries=df['native-country'].value_counts()
    p=rich_counts/countries
    highest_earning_country=p.idxmax()
    highest_earning_country_percentage=p[p.idxmax()]
    highest_earning_country_percentage*=100
    highest_earning_country_percentage=round(highest_earning_country_percentage,1)
    #Identify the most popular occupation for those who earn >50K in India.
    ind=df[df['native-country']=='India']
    rich_ind=ind[ind['salary']=='>50K']
    top_IN_occupation=rich_ind['occupation'].value_counts().idxmax()
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men\n:", average_age_men)
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
