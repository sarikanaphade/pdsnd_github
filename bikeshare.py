import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        cities = ['chicago' , 'new york', 'washington']
        city = str(input("Which City would you like to see data for (Chicago, New York, Washington):\n")).lower().strip()
        if(city not in cities):
            print("Please enter correct city name [chicago or new york city or washington] \n")
            continue
        break

    while(True):
        filters = ['month' , 'day', 'both','none']
        filter = str(input("Would you like to filter data by month, day, both or not at all? [Type 'none' for no time filter] \n")).lower().strip()
        if(filter not in filters):
            print("Please enter correct time filter [day or month or both or none] \n")
            continue
        if(filter == 'day'):
            month = 'all'
        elif(filter == 'none'):
            month = 'all'
            day = 'all'
        elif(filter == 'month'):
            day = 'all'
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    if(filter == 'month' or filter == 'both'):
        while(True):
            months = ['january', 'february', 'march', 'april', 'may','june']
            month = str(input("Please enter name of the month [january, february, march, april, may or june]: \n")).lower().strip()
            if(month not in months ):
                print("Please enter correct value for month [january, february, ... , june] ")
                continue
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if(filter =='day' or filter == 'both'):
        while(True):
            days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
            day = str(input("Please enter day of a week [monday, tuesday, ... , sunday] : \n")).lower().strip()
            if(day.lower() not in days):
                print("Please enter correct value for day [monday, tuesday, ... sunday]")
                continue
            break

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
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may','june']
        month = months.index(month) + 1
        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract hour.month, day of week from the Start Time column to create an hour, month and day of week column
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Display the most common month
    months_name={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'}
    popular_month = df['month'].mode()[0]
    print('The most popular month is {}'.format(months_name[popular_month]))

    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of week is {}'.format(popular_day))

    # Display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    popular_start_sation_count = df['Start Station'].value_counts()[0]
    print('\nThe most popular start station is {} , Count: {}'.format(popular_start_station,popular_start_sation_count))

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    popular_end_sation_count = df['End Station'].value_counts()[0]
    print('\nThe most popular End station is {} , Count: {}'.format(popular_end_station,popular_end_sation_count))

    # Display most frequent combination of start station and end station trip
    popular_start_end_station = df.groupby(['Start Station' , 'End Station']).size().reset_index(name="Trip Count").sort_values(by='Trip Count',ascending=False).head(1)
    print('\nThe most popular trip is \n{}'.format(popular_start_end_station.to_string(index=False)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].count()
    print('\nThe total travel time is {}'.format(total_travel_time))

    # Display mean travel time
    total_travel_time = df['Trip Duration'].mean()
    print('\nThe average travel time is {}'.format(total_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Different User Types Count : \n {}'.format(user_types_count))

    # Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('\nGender Count : \n {}'.format(gender_count))
    else:
        print('\nNo Gender data to share.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        print('\nEarliest birth year : {}'.format(earliest_birth_year))
        print('\nMost Recent birth year : {}'.format(recent_birth_year))
        popular_birth_year = df['Birth Year'].mode()[0]
        print('\nThe most popular birth year : {}'.format(popular_birth_year))
    else:
        print("\nNo Birth Year data to share.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_data(df,city):
    """Displays statistics on individual trip data."""
    index = 0
    while True:
        restart = input('\nWould you like to see individual trip data? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        if index == 0:
            start = 0
            stop = 5
            if(city == 'washington'):
                df = df.drop(df.columns[[7,8,9]], axis=1)
            else:
                df = df.drop(df.columns[[9,10,11]], axis=1)
        df.rename(columns={'Unnamed: 0':''},inplace = True)
        # Display raw trip data
        print(json.dumps(df[start:stop].to_dict('records'), indent=4,sort_keys=True, default=str))
        start +=5
        stop += 5
        index = index + 1
        continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        trip_data(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
