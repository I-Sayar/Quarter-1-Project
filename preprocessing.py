from sklearn.model_selection import train_test_split
import os

dataset =[]
labels = []
#50068911,THE CREPE MASTER,Manhattan,139,WEST  116 STREET,10026,9179951552,American,1/18/2023,Violations were cited in the following area(s) ,04H,Raw  cooked or prepared food is adulterated  contaminated  cross  contaminated  or not discarded in accordance with HACCP plan ,Critical,19,B,1/18/2023,5/14/2023,Cycle Inspection / Re  inspection,40 80252596,73 95087271,110,9,21800,1057396,1019010013,MN11


with open("inspections.csv") as my_file:
    for line in my_file:
        row = line[:len(line)-1].split(",")
        if row[12] == "":
            row[12] = "1/1/2024"
        dataset += [row[:11]+ row[12:]]
        labels += [row[11]]
attributes = dataset[0] + [labels[0]]
dataset = dataset[1:]
labels = labels[1:]

os.remove("cleaned_inspections.txt")
f = open("cleaned_inspections.txt", "a")
f.write(",".join(attributes))
for index, value in enumerate(dataset):
    f.write(",".join(value) +","+labels[index]+"\n")
f.close()

X_train, X_temp, y_train, y_temp = train_test_split(dataset, labels, test_size = 0.3, random_state = 42, stratify= labels)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size = 0.5, random_state = 42, stratify = y_temp)

training_set = []
validation_set = []
testing_set = []
# make sure to delete old before running again
for i in range(len(X_train)):
    training_set += [X_train[i]+ [y_train[i]]]

for i in range(len(X_val)):
    validation_set += [X_val[i]+ [y_val[i]]]
    
for i in range(len(X_test)):
    testing_set += [X_test[i]+ [y_test[i]]]

os.remove("training_set.txt")
os.remove("validation_set.txt")
os.remove("testing_set.txt")

f = open("training_set.txt", "a")
for value in training_set:
    f.write(",".join(value) +"\n")
f.close()

f = open("validation_set.txt", "a")
for value in validation_set:
    f.write(",".join(value)+"\n")
f.close()

f = open("testing_set.txt", "a")
for value in testing_set:
    f.write(",".join(value)+"\n")
f.close()

