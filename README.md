### December 30, 2018

## Bikeshare Data Project

### Description

In this project we will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. For example it provides the information like Popular times of travel (i.e., occurs most often in the start time), Popular stations and trip, Trip duration and User information.

### Software Requirements
The following software requirements apply:
- Python 3, NumPy, and pandas installed using Anaconda
- A text editor, like Sublime or Atom. (Optional : In case user wants to view/modify files)
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

### Files Used

- #####  Three city dataset Files

  - chicago.csv
  - new_york_city.csv
  - washington.csv


- ##### Scripting File

  - bikeshare.py

    The bikeshare.py file is a python script file that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. There are four questions that will change the answers:

    - Would you like to see data for Chicago, New York, or Washington?
    - Would you like to filter the data by month, day, or not at all?
    - (If they chose month) Which month - January, February, March, April, May, or June?
    - (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

    After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.
