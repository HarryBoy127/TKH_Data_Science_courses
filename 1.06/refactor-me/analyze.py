import pandas as pd

# Read in a data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# In following lines of code we are using .agg method to calculate the descriptive statistics of our "Purchase Amount (USD)" column
print("Summary statistics on Purchase Amount (USD):")
df_price = df["Purchase Amount (USD)"].agg(['mean', 'median', 'max', 'min', 'std'])
print(df_price)

# White space to make our output code more easy to read and give the separation between blocks of code outputs
print("                         ")

# In following lines of code we are using .agg method to calculate the descriptive stats of our "Age" columns
print("Summary statistics on Age:")
df_age = df["Age"].agg(['mean', 'median', 'max', 'min', 'std'])
print(df_age)

# White space to make our output code more easy to read and give the separation between blocks of code outputs
print("                         ")

#Winter summary statistics on purchase amount
#fist we create a new list that contains only values that mathc "Winter" in the season column
#then we use .agg feature to determine the summary statistics for this function 
print("Winter summary statistics on Purchase Amount (USD):")
winter = df[df.Season == "Winter"]
df_winter = winter["Purchase Amount (USD)"].agg(['mean', 'median', 'max', 'min', 'std'])
print(df_winter)

# White space to make our output code more easy to read and give the separation between blocks of code outputs
print("                         ")

#Spring summary statistics on purchase amount
#fist we create a new list that contains only values that mathc "Spring" in the season column
#then we use .agg feature to determine the summary statistics for this function 
print("Spring summary statistics on Purchase Amount (USD):")
spring = df[df.Season == "Spring"]
df_spring = spring["Purchase Amount (USD)"].agg(['mean', 'median', 'max', 'min', 'std'])
print(df_spring)

# White space to make our output code more easy to read and give the separation between blocks of code outputs
print("                         ")

#Summer summary statistics on purchase amount
#fist we create a new list that contains only values that mathc "Summer" in the season column
#then we use .agg feature to determine the summary statistics for this function 
print("Summer summary statistics on Purchase Amount (USD):")
summer = df[df.Season == "Summer"]
df_summer = summer["Purchase Amount (USD)"].agg(['mean', 'median', 'max', 'min', 'std'])
print(df_summer)

# White space to make our output code more easy to read and give the separation between blocks of code outputs
print("                         ")

#Fall summary statistics on purchase amount
#fist we create a new list that contains only values that mathc "Fall" in the season column
#then we use .agg feature to determine the summary statistics for this function 
print("Fall summary statistics on Purchase Amount (USD):")
fall = df[df.Season == "Fall"]
df_fall = fall["Purchase Amount (USD)"].agg(['mean', 'median', 'max', 'min', 'std'])
print(df_fall)

print("                         ")

# by dropping the columns "Cursomer ID" and "Discount Applied" we are keeping the more clean data set without this column 
#First we selecte and identify the coulumn we would like to drop 
#proccedd with the .drop operation and drop the unncessary column
selected = ["Customer ID", "Discount Applied"]
df = df.drop (columns=selected)

# figure out most popular payment method in NY
# TODO: is there anyway we could modularize this behavior to apply to all
# TODO: possible states? (OR possibly use a pandas function that does this
# TODO: for us already?)

def pop_payment (state):
    us_states = df[df.Location == state]
    payment_methods = df['Payment Method'].unique()

    most_frequent_method = {}

    for method in payment_methods:
        most_frequent_method[method] = len(us_states[us_states['Payment Method'] == method])

    print("Most Frequient Payment Methods are: ")
    print(most_frequent_method)
pop_payment("New York")
# Write this updated data out to csv file
df.to_csv('data/processed/cleaned_data.csv', index=False)
