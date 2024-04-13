import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
columns_name=["user_id","item_id","rating","timestamp"]
df=pd.read_csv("/content/u.data",sep='\t',names=columns_name)
df.head()
df.shape
df['user_id'].nunique()
df['item_id'].nunique()
movie_title = pd.read_csv(r"/content/u.item",encoding="ISO-8859-1",sep="\|",header= None)
movie_title.head()
movie_title=movie_title[[0,1]]
movie_title.columns=["item_id","title"]
movie_title.head()
df=pd.merge(df, movie_title,on ="item_id")
df.head()
df.tail()
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
df
df.groupby('title').mean()['rating'].sort_values()
df.groupby('title').mean()['rating'].sort_values(ascending=False).head()
df.groupby('title').count()['rating'].sort_values(ascending=False)
ratings=pd.DataFrame(df.groupby('title').mean()['rating'])
ratings.head()
ratings["num of rating"]=pd.DataFrame(df.groupby('title').count()['rating'])
ratings.sort_values(by='rating',ascending=False)
plt.figure(figsize=(10,6))
plt.hist(ratings['num of rating'], bins=70)
plt.show()
plt.hist(ratings['rating'],bins=70,color="green")
plt.show()
sns.jointplot(x='rating',y='num of rating',data=ratings,alpha=0.5,color="red")
plt.show()
df.head()
movie_matrix=df.pivot_table(index="user_id",columns='title',values="rating")
movie_matrix.head()
# movie_matrix
ratings.sort_values('num of rating',ascending=False).head()
starwars_user_rating=movie_matrix['Star Wars (1977)']
starwars_user_rating.head()
similar_to_starwars=movie_matrix.corrwith(starwars_user_rating)
corr_starwars=pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()
corr_starwars.sort_values('Correlation',ascending=False)
ratings
corr_starwars = corr_starwars.join(ratings['num of rating'])
corr_starwars
corr_starwars.head()
corr_starwars[corr_starwars['num of rating']>100].sort_values('Correlation',ascending=False)
def predict_movie(movie_name):
    movie_user_ratings = movie_matrix[movie_name]
    similar_to_movie = movie_matrix.corrwith(movie_user_ratings)

    corr_movie=pd.DataFrame(similar_to_movie,columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    corr_movie = corr_movie.join(ratings['num of rating'])
    predictions=corr_movie[corr_movie['num of rating']>100].sort_values('Correlation',ascending=False)
    return predictions
result=predict_movie("Titanic (1997)")
result.head(10)
result1=input("Enter the Movie name : ");
result=predict_movie(result1)
result.head(10)