import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')
  # print(df.head(10))
  # df.info()

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  # print(df['race'].value_counts())
  
  race_count = pd.Series(df['race'].value_counts()).rename('race_count')
  # print(race_count.index)
  

  # What is the average age of men?
  average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)
  # print(average_age_men)

  # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = round((
    df['education'].value_counts().loc['Bachelors'])/len(df['education'])*100, 1)
  # print(percentage_bachelors)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?
  # with and without `Bachelors`, `Masters`, or `Doctorate`

  higher_education = (
    df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')

  nerd_count = len(df[higher_education])  

  # print(df[higher_education].loc[df['salary'] == '>50K'].head())

  # higher_education = len(df[nerd_vision].loc[df['salary'] == '>50K'])/nerd_count
  lower_education = (
    df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')

  # percentage with salary >50K
  higher_education_rich = round((len(df[higher_education].loc[df['salary'] == '>50K'])/nerd_count) * 100, 1)
  lower_education_rich = round((len(df[lower_education].loc[df['salary'] == '>50K'])/len(df[lower_education])) * 100, 1)

  #print('-------', higher_education_rich, lower_education_rich, '--------')

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  # print('describe----\n')
  # print(df['hours-per-week'].describe().loc['min'])
  # print('info----\n')

  min_work_hours = df['hours-per-week'].describe().loc['min']

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  # print (df[df['hours-per-week'] == 1])
  min_hours_mask = df['hours-per-week'] == 1
  num_min_workers = len(df[min_hours_mask])

  rich_percentage = (len(df[min_hours_mask].loc[df['salary'] == '>50K'])/num_min_workers)*100

  # What country has the highest percentage of people that earn >50K?
  #print((df['native-country'].loc[df['salary'] == '>50K'].value_counts() / df['native-country'].value_counts()).sort_values(ascending=False).index[0])
  highest_earning_country = (df['native-country'].loc[df['salary'] == '>50K'].value_counts() / df['native-country'].value_counts()).sort_values(ascending=False).index[0]
  highest_earning_country_percentage = round((df['native-country'].loc[df['salary'] == '>50K'].value_counts() / df['native-country'].value_counts()).sort_values(ascending=False)[0]*100, 1)

  # Identify the most popular occupation for those who earn >50K in India.
  rich_IN_mask = (df['native-country'] == 'India') & (df['salary'] == '>50K')
  top_IN_occupation = df['occupation'].loc[rich_IN_mask].value_counts().index[0]
  # print(top_IN_occupation.value_counts().index[0])


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
