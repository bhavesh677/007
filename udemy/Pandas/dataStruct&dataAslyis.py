import pandas

df1=pandas.DataFrame([[2,4,5],[6,8,9]])

df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"])

df1=pandas.DataFrame([[2,4,6],[3,9,1]],columns=["price","Age","Values"],index=["first","second"])

df2=pandas.DataFrame([{"Name":"Bhavesh","Surname":"Sawant"},{"Name":"Abhishek","Surname":"Walanj"},{"Name":"Sanyukta","Surname":"Mahindrakar"}])


print(df1)

#print(df2)

#print(df1.mean()) # mean of all the columns in the dataframe

#print(type(df1.mean())) 

#print("mean of entire DataFrame",df1.mean().mean()) # mean of entire DataFrame

print(df1.price) #price column

print("mean of price column: ",df1.price.mean()) # mean of price column

print("max of price column: ",df1.price.max()) # max of price column











