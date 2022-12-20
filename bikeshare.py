>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
Include the date you created this project and README file.
Thursday, December 15, 2022

### Project Title
Replace the Project Title
Explore US bikeshare Data 

### Description
Describe what your project is about and what it does
our project was to make a python code that asks the user to choose a city he/she want to explore their bikeshare data

### Files used
Include the files used
- washington.csv
- new_york_city.csv
- chicago.csv


### Credits
It's important to give proper credit. Add links to any repo that inspired you or blogposts you consulted.
Udacity teachers were helpful..

###Project
import time
import pandas as pd
import numpy as np


def get_filters():
    """
 
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Which cities data would you like to read about?, Enter Chicago, new york city or washington: \n").lower()
    citys = ['chicago', 'new york city', 'washington']
    
    while city not in citys:
      city = input("\n Sorry.. invalid input. please try again.\n").lower()
   
    # get user input for month (all, january, february, ... , june)
    month = input("Which month would like to read about?, Enter 'january', 'february', 'march', 'april', 'may', 'june', 'all': \n").lower()
        
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        
    while month not in months:
      month = input("\n Sorry.. invalid input. please try again.\n").lower()
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of the week would you like to read about?, Enter  "sunday", "monday", "tuesday", "Wednesday", "thursday", "friday" or "saturday", "all": \n').lower()
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
        
    while day not in days:
      day = input("\n Sorry.. invalid input. please try again.\n").lower()

    print('-'*40)
    return city, month, day

    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day'] == day,:]

    return df

    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = str(df['month'].mode().values[0])
    print("The most common month is: {}\n".format(common_month))

    # display the most common day of week
    common_day = str(df['day'].mode().values[0])
    print("The most common day of the week: {}\n".format(common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = str(df['hour'].mode().values[0])
    print("The most common start hour: {}\n".format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

   # display total travel time
    total = str(df['duration'].sum())
    print("The total travel time is: {}\n".format(total))

    # display mean travel time
    mean = str(df['duration'].sum())
    print("The mean travel time is: {}\n".format(mean))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
   
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_sta = df['Start Station'].mode().values[0]
    print("The most common start station is: {}\n".format(start_sta))

    # display most commonly used end station
    end_sta = df['End Station'].mode().values[0]
    print("The most common end station is: {}\n".format(end_sta))

    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    frequent_comb = df['routes'].mode().values[0]
    print("The most frequent combination of start station and end station is: {}\n".format(frequent_comb))
   

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Displaying the counts of user types: \n")
    print(df['User Type'].value_counts())

    if city != 'washington':
        # Display counts of gender
        print("Displaying the counts of gender:")
        print(df['Gender'].value_counts())


        # Display earliest, most recent, and most common year of birth
        #1st earliest year of birth
        earliest_year = str(int(df['Birth Year'].min()))
        print("The earliest birth year is: {}".format(earliest_year))
        
        #2nd the most recent year of birth
        recent_year = str(int(df['Birth Year'].max()))
        print("The latest birth year is: {}".format(recent_year))
        
        #3rd the most common year of Birth
        common_year = str(int(df['Birth Year'].mode().values[0]))
        print("The most common birth year is: {}".format(common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    


def display_data(df):
    display = input('Do you want to see more raws of data?: Enter Yes or No ').lower()
    print()
    if display=='yes' or display=='y':
        display=True
    elif display=='no' or display=='n':
        display=False
    else:
        print("\n Sorry.. invalid input. please try again.\n")
        display_data(df)
        return

    if display:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            display = input("Do you want to continue explore data? Enter Yes or No\n").lower()
            if display=='yes' or display=='y':
                continue
            elif display=='no' or display=='n':
                break
            else:
                print("\n Sorry.. invalid input. please try again.\n")
                return

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you want to restart exploring? Enter yes or no.\n').lower()
        if restart == 'no':
           break
        elif restart == 'yes':
           continue
        else:
          restart = input("\n Sorry.. invalid input. please try again.\n").lower()

           


if __name__ == "__main__":
	main()
