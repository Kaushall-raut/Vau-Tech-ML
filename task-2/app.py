import pandas as pd


df=pd.read_csv('tmdb_movies_dataset.csv')

print(df.head())

# print(df.shape)
print("------------")

print(df.info())



# if i want to create a recommendation model than columns that i need as an input feature are - 

# title , popularity and rating  

# this model will predict best movies to recommend to a user on the user interface


#title= object ,  popularity = decimal , rating =decimal

