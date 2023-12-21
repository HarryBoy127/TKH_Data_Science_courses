
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        
        averages = [] #creating a list named averages where we will plant our mean. 
        for row in self.data:
            values = [] #we create a list called value, here we will sort our values witout the firs column (date) 
            for val in row[0:]: 
                try:  #we use Try and Except method because not all out values can be transfered to float so we skip the error. 
                    num = float(val) #making sure that all values are float type
                    values.append(num) #adding our new values to the values list from line 24
                except ValueError:
                    pass
            if values: 
                avg = round(sum(values)/len(values), 3) #calculating mean by using new list values
                averages.append(avg)  # putting this answer for average into our main list called averages 
        return averages #everytime when function average01 will be used, the list called averages with mean for this date, will be used. 

      
    def median02(self):
        
        medians = [] #creating a list called medians 
        for row in self.data[0:]:
            values = [] #creating list values
            for val in row: 
                try: #using this concpet (ty and except) to avoid ValueError and format our data to a float format
                    num = float(val)
                    values.append(num) #putting this new list of data into "values" list
                except ValueError:
                    pass
            if values: 
                data = sorted(values) #firt ordering the data in each row so it will go from lower to highest 
                data1 = len(data) #figuring our how long is each row (like how many data in it)
                middle = (data1 - 1) // 2 #figuring our the middle value 
                if data1 % 2 == 1:  #we are using this if our row is odd 
                    median = round(data[middle], 6) 
                else: #using this if our data on the row is even 
                    median = round((data[middle] + data[middle + 1]) / 2, 6)
                medians.append(median) #adding our answers in our main list medians
            else:
                medians.append(0.0) 
        return medians #the new values for medians will be returned when triggered
                

    def stddev03(self):
        
        stdev3 = []
        for row in self.data[0:]:
            values = [] #creating an empty list for tranformed data 
            for val in row: 
                try:  #using try and excpet concept to filter the data and remove the first column (date)
                    num = float(val)
                    values.append(num) #adding new data to the list created in line 62
                except ValueError:
                    pass
            if len(values): #standart fromulat for finding the standart deviation 
                n = len(values) 
                mean = sum(values) / n
                deviations = [(x - mean) ** 2 for x in values]
                variance = sum(deviations) / (n - 1)
                stdev = (variance ** 0.5)
                stdev3.append(round(stdev, 3))  #rounding and adding the stadart deviation for each row
            else: 
                stdev3.append(0.0) 
        return stdev3 #new values for stdev will be returned when trifgered