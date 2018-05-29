from pyhive import hive
import pandas as pd
import time

#Create Hive connection 
conn = hive.Connection(host="localhost", port=10000, username="hduser")

# Read Hive table and Create pandas dataframe
start = time.time()
#pd.read_sql("use youtube", conn)
df  = pd.read_sql("select * from youtube.youtube_new limit 20", conn)
end = time.time()- start
print(df.head())
print("this is time")
print(end)

