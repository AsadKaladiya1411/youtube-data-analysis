import pandas as pd
import matplotlib.pyplot as plt

#Load dataset
df=pd.read_csv('youtube_data.csv')

#Convert 'upload date' to datetime
df['Upload Date']=pd.to_datetime(df['Upload Date'],dayfirst=True, errors='coerce')

#Print basic dataset info
print("Dataset Overview:")
print(df.head())

#Find video with most views
top_video=df[df['Views']==df['Views'].max()]
print("\nTop Performing Video:")
print(top_video[['Video Title','Views']])

#Sort by Upload Date for time-series plot
df=df.sort_values(by='Upload Date')

#Plot views over time
plt.figure(figsize=(10,5))
plt.plot(df['Upload Date'],df['Views'],marker='o',linestyle='-',color='blue')
plt.title("YouTube Views Over Time")
plt.xlabel("Upload Date")
plt.ylabel("Views")
plt.grid(True)
plt.tight_layout()
plt.show()

#Likes per Video
plt.figure(figsize=(10,5))
plt.bar(df['Video Title'],df['Likes'],color='orange')
plt.title("Likes Per Video")
plt.xlabel("Video Title")
plt.ylabel("Likes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


