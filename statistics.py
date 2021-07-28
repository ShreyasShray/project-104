# importing csv module
import csv
from collections import Counter

# opening csv file as f and storing it in fileData
with open("WeightHeight.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

# removing the top line of data
fileData.pop(0)

# getting weight and storing it in diffirent list
weight_for_mode = []
weight = []
for i in range(len(fileData)):
    num = fileData[i][2]
    weight.append(float(num))
    weight_for_mode.append(float(num))


# length of fileData
n = len(fileData)

# getting sum of all data
total = 0
for x in weight:
    total += float(x)

# mean = sum of data/number of data
mean = total/n

# sorting the data in ascending order
weight.sort()

# getting the median
if(n % 2 == 0):
    median1 = float(weight[n//2])
    median2 = float(weight[n//2 - 1])
    median = (median1 + median2)/2
else:
    median = float(weight[n//2])

# getting the occurrence of data
data = Counter(weight_for_mode)

mode_data_for_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}

# getting the occurrence in range
for weight,occurence in data.items():
    if(75 < float(weight) <85):
        mode_data_for_range["75-85"] += occurence
    elif(85 < float(weight) <95):
        mode_data_for_range["85-95"] += occurence
    elif(95< float(weight) <105):
        mode_data_for_range["95-105"] += occurence
    elif(105< float(weight) <115):
        mode_data_for_range["105-115"] += occurence
    elif(115< float(weight) <125):
        mode_data_for_range["115-125"] += occurence
    elif(125< float(weight) <135):
        mode_data_for_range["125-135"] += occurence
    elif(135< float(weight) <145):
        mode_data_for_range["135-145"] += occurence
    elif(145< float(weight) <155):
        mode_data_for_range["145-155"] += occurence
    elif(155< float(weight) <165):
        mode_data_for_range["155-165"] += occurence
    elif(165< float(weight) <175):
        mode_data_for_range["165-175"] += occurence

mode_range, mode_occurence = 0, 0

# getting the mode
for range,occurence in mode_data_for_range.items():
    if(occurence > mode_occurence):
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0] + mode_range[1])/2)

# printing all the values
print("Mean is ", mean)
print("Median is ", median)
print("Mode is ", mode)