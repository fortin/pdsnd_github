#!/usr/bin/env python
#
#  Bikeshare data analysis
#
#  Created by Antonio Fortin on 2018-11-14.
#

import time
import pandas as pd
import numpy as np
import getch
import calendar
import plotly
import plotly.graph_objs as go
from plotly.offline import plot

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\033c')
    print('Hello! Let\'s explore some US bikeshare data! \n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    choices = list(range(1, len(CITIES)+1)) # create list of numbers for each item in CITIES
    choices = list(map(str, choices)) # convert list of ints to list of strings
    city_dict = dict(zip(choices, CITIES)) # create dictionary from numbers and CITIES

    while True:
        print('Pick a city to filter the data: ')
        for x, y in city_dict.items():
            print('(' + x + ')', y.title()) # display menu of choices
        try:
            city_choice = getch.getch() # single key input (1-3)
            if city_choice in city_dict.keys(): # input error checking
                city = city_dict[city_choice] # assign value of keystroke to city
                print('\033c')
                print('You picked ' + city.title() + '\n')
                break
            else:
                print('\033c')
                print('Invalid input! Try again.\n')
        except (TypeError, KeyError, UnboundLocalError):
            print('Invalid input! Try again.\n')


    # get user input for month (all, january, february, ... , june)
    choices = list(range(1, len(MONTHS)+1)) # create list of numbers for each item in MONTHS
    choices = list(map(str, choices)) # convert list of ints to list of strings
    month_dict = dict(zip(choices, MONTHS)) # create dictionary from numbers and MONTHS

    print('Now let\'s pick a month... \n')
    while True:
        print('Filter by month: ')
        for x, y in month_dict.items():
            print('(' + x + ')', y.title()) # display menu of choices
        try:
            month_choice = getch.getch() # single key input (1-7)
            if month_choice in month_dict.keys(): # input error checking
                month = month_dict[month_choice] # assign value of keystroke to month
                print('\033c')
                if month == 'all':
                    print('You chose to display data for all months.\n')
                else:
                    print('You picked ' + month.title() + '\n')
                break
            else:
                print('\033c')
                print('Invalid input! Try again.\n')
        except (TypeError, KeyError, UnboundLocalError):
            print('Invalid input! Try again.\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    choices = list(range(1, len(DAYS)+1)) # create list of numbers for each item in DAYS
    choices = list(map(str, choices)) # convert list of ints to list of strings
    day_dict = dict(zip(choices, DAYS))

    print('Finally, pick a day to filter data: \n')
    while True:
        print('Filter by day: ')
        for x, y in day_dict.items():
            print('(' + x + ')', y.title()) # display menu of choices
        try:
            day_choice = getch.getch() # single key input (1-8)
            if day_choice in day_dict.keys(): # input error checking
                day = day_dict[day_choice] # assign value of keystroke to day
                print('\033c')
                if day == 'all':
                    print('You chose to display data for all days.\n')
                    break
                else:
                    print('You picked ' + day.title() + '\n')
                    break
            else:
                print('\033c')
                print('Invalid input! Try again.\n')
        except (TypeError, KeyError, UnboundLocalError):
            print('Invalid input! Try again.\n')

    print('\033c')
    print('Analyzing data for...\n')
    print('City: ' + city.title() + '\nMonth: ' + month.title() + '\nDay: ' + day.title())

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
    # create DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if necessary
    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    # filter by day if necessary
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    busiest_month = df['month'].mode()[0]
    print('The busiest month is {}.'.format(calendar.month_name[busiest_month]))
    # display the most common day of week
    busiest_day = df['day'].mode()[0]
    print('The busiest day is {}.'.format(busiest_day))

    # display the most common start hour (0-23)
    popular_hour = df['hour'].mode()[0]
    print('The most popular start hour is {}:00.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df.mode()['Start Station'][0]
    print('The most popular start station is {}.'.format(popular_start_station))
    # display most commonly used end station
    popular_end_station = df.mode()['End Station'][0]
    print('The most popular end station is {}.'.format(popular_end_station))
    # display most frequent combination of start station and end station trip
    popular_route = df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most popular route is {} to {}".format(popular_route[0], popular_route[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time:", total_travel, 'seconds')

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel, 'seconds')

    # display shortest travel time
    min_travel = df['Trip Duration'].min()
    print("Shortest travel time:", min_travel, 'seconds')

    # display longest travel time
    max_travel = df['Trip Duration'].max()
    print("Longest travel time:", max_travel, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def type_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    print('Counts of User Types')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    for i, type_count in enumerate(user_type_counts):
        print("  {}: {}".format(user_type_counts.index[i], type_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    # Display counts of gender
    print("Calculating Gender Stats...\n")
    start_time = time.time()
    gender_counts = df['Gender'].value_counts()
    # iteratively print out the total numbers of genders
    for index, gender_count in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))
    print('-'*40)

    print("\nCalculating Birth Year Stats...\n")
    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    # most common year of birth
    popular_year = int(birth_year.value_counts().idxmax())
    print("The most common year of birth:", popular_year)
    # most recent birth year
    most_recent = int(birth_year.max())
    print("The most recent year of birth:", most_recent)
    # earliest birth year
    earliest_year = int(birth_year.min())
    print("The earliest year of birth:", earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def graphs(df):
    """Generates line graph of data based on user choice of either Gender or User Type."""

    graph_dict = dict({'1': 'Gender', '2': 'User Type', '3': 'No graph'})

    # Generate and display graph
    while True:
        print('Would you like to see a graph of travel based on:\n')
        for x, y in graph_dict.items():
            print('(' + x + ')', y.title()) # display menu of choices
        try:
            graph_choice = getch.getch() # single key input (1-3)
            graph = graph_dict[graph_choice] # assign value of keystroke to graph
            print('\nYou picked ' + graph + '...\n')
            if graph == 'Gender':
                v1 = 'Male'
                v2 = 'Female'
            elif graph == 'User Type':
                v1 = 'Customer'
                v2 = 'Subscriber'
            elif graph == 'No graph':
                    print('OK. Bye!')
                    return
            else:
                print('\033c')
                print('Invalid input! \nEnter a number between 1 and 3. ')
            v1_by_date = df.groupby(df[df[graph] == v1]['Start Time'].dt.date).count()
            v2_by_date = df.groupby(df[df[graph] == v2]['Start Time'].dt.date).count()
            v1_data = go.Scatter(
                x = v1_by_date.index,
                y = v1_by_date['Trip Duration'],
                name = v1
            )
            v2_data = go.Scatter(
                x = v2_by_date.index,
                y = v2_by_date['Trip Duration'],
                name = v2
            )
            plot_data = [v1_data, v2_data]
            layout = go.Layout(
                title = 'Trips by ' + graph,
                xaxis = dict(
                title = 'Date',
                ),
                yaxis=dict(
                    title='Number of trips',
                )
            )
            plotly.offline.plot({"data": plot_data, "layout": layout})
        except (TypeError, KeyError, UnboundLocalError):
            print('\nInvalid input! Try again.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        type_stats(df)
        if city != 'washington':
            user_stats(df)
            graphs(df)
        else:
            print('\nUnfortunately, Gender and User Type data are not available for Washington.')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
