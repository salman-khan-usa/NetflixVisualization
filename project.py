import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('netflix_titles.csv')
print(df.head)


#Droping some coloumns
df.drop(['description','date_added','cast','show_id'],axis=1,inplace=True)
print(df)



#clean Datan and visualize
df = df.dropna(subset=['type','duration','country','release_year','rating'])

type = df['type'].value_counts()
print(type)

plt.bar(type.index,type.values,color=['Green','orange'])
plt.title('No of Movies vs Tv Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


# Counting rating pie chart

rating_c = df['rating'].value_counts()
plt.pie(rating_c,labels=rating_c.index,autopct='%1.1f%%',startangle=90)
plt.title('Percentage of content Ratings')
plt.tight_layout()
plt.show()


#Movies released in each year
release = df['release_year'].value_counts()
print(release)

plt.plot(release.index,release.values,color='Red')
plt.title('Netflix Movies Released In Each Year')
plt.xlabel('Release Year')
plt.ylabel('Counts')
plt.tight_layout()
plt.show()


#Movies by Country
country = df['country'].value_counts().head(10)

plt.bar(country.index,country.values,color='Blue')
plt.title('Top 10 Countries By No of Releases(NetFlix)')
plt.xlabel('Countries')
plt.ylabel('Number of Movies')
plt.xticks(rotation=40)
plt.tight_layout()
plt.show()




# Group by country and type
countryt = df.groupby(['country', 'type']).size().unstack().fillna(0)

# Select Top 10 countries by total releases
top_countries = countryt.sum(axis=1).sort_values(ascending=False).head(10)
countryt = countryt.loc[top_countries.index]


plt.figure(figsize=(14,6))

# Movies
plt.subplot(1,2,1)
plt.bar(countryt.index, countryt['Movie'], color='purple')
plt.title('Top 10 Movies on Netflix by Country')
plt.xlabel('Countries')
plt.ylabel('Number of Movies')
plt.xticks(rotation=40)

# TV Shows
plt.subplot(1,2,2)
plt.bar(countryt.index, countryt['TV Show'], color='orange')
plt.title('Top 10 TV Shows on Netflix by Country')
plt.xlabel('Countries')
plt.ylabel('Number of TV Shows')
plt.xticks(rotation=40)

plt.tight_layout()
plt.show()
