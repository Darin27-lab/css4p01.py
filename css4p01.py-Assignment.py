# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:09:52 2024

@author: Darin Holman
"""
import pandas as pd
df= pd.read_csv("C:/Users/Darin Holman/css4p01.py/movie_dataset.csv")

# Question 1
print(df['Rating'])
print(df['Rating'].max())
# = 9.0

print(df[df['Rating']==9.0])
# = The Dark Knight
 
# Question 2
x = df["Revenue (Millions)"].mean()
print(df["Revenue (Millions)"].mean())
# = 82.96 Million

# Question 3
d6= (df[df['Year']==2015])
d7= (df[df['Year']==2016])
d8= (df[df['Year']==2017])

d9 = pd.concat([d6, d7, d8], ignore_index=True)
print(d9['Revenue (Millions)'].mean())
# = 63 Million

# Question 4
print(df[df['Year']== 2016])
# = 297

# Question 5
print(df[df['Director']== 'Christopher Nolan'])
# = 5

# Question 6

r8= df[df['Rating']>=8]
print(r8)
r8.count()

r8['Rating'].describe()
r8['Rating'].value_counts()

# = 78

# Question 7
CNolanMovies=(df[df['Director']== 'Christopher Nolan'])
print(CNolanMovies['Rating'])

Rating = [8.6, 9.0, 8.5, 8.8, 8.5]
# Rating (Low to High) = [8.5, 8.5, 8.6, 8.8, 9.0]
# = 8.6

# Question 8

# Find the year with the highest average rating (2006, 2007, 2008, 2016)
# 2006
AR2006=(df[df['Year']== 2006])
print(df[df['Year']== 2006])
print(AR2006['Rating'].mean())
           
#2007
AR2007=(df[df['Year']== 2007])
print(df[df['Year']== 2007])
print(AR2007['Rating'].mean())

# 2008
AR2008=(df[df['Year']== 2008])
print(df[df['Year']== 2008])
print(AR2008['Rating'].mean())

#2016
AR2016=(df[df['Year']== 2016])
print(df[df['Year']== 2016])
print(AR2016['Rating'].mean())
# 2007 has the highest average rating at 7.13

# Question 9
print(df[df['Year']== 2006])
A1= "44" #Movies were made in 2006
print(df[df['Year']== 2016])
A2= "297" #Movies were made in 2016 

((297-44)/(44))*100
# = 575.0

# Question 10
# Find the most common actor in all the movies?
# Find a way to search for the most common actor in all the movies.
grouped= df.groupby('Actors')
count_Mark_Wahlberg = grouped['Actors'].count()

print("\nCount of Mark Wahlberg:")
print(count_Mark_Wahlberg)
# = 15

# Question 11
# How many unique genres are there in the dataset? 
# Find a way to identify them individually.

Genre= df.groupby('Genre')
count_Unique_Genre = grouped['Genre'].count()
# Least number would be the most unique
print("\nCount of Genre:")
print(count_Unique_Genre)
# = 20

# Question 12
print(df.describe())
            Rank        Year     ...   Revenue (Millions)   Metascore
count  1000.000000  1000.000000  ...          872.000000  936.000000
mean    500.500000  2012.783000  ...           82.956376   58.985043
std     288.819436     3.205962  ...          103.253540   17.194757
min       1.000000  2006.000000  ...            0.000000   11.000000
25%     250.750000  2010.000000  ...           13.270000   47.000000
50%     500.500000  2014.000000  ...           47.985000   59.500000
75%     750.250000  2016.000000  ...          113.715000   72.000000
max    1000.000000  2016.000000  ...          936.630000  100.000000