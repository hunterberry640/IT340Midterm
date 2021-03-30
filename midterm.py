# Author: Hunter Berry
# Date: Jan 26, 2021
# Description: Naive bayesian classifier for spam
# in order to read the data correctly just put the email data folder in the same directory as this file.
import random

non_spam_path1 = 'email data/Ham/300 good emails/'
non_spam_path2 = 'email data/Ham/301-600 good ones/'
spam_path = 'email data/Spam/'
training_emails = 1000
test_emails = 200
words = {} # dict to store training set words and probabilities. format     "lunch": {0: .5, 1: .7};

spam_emails = [] # 2D list to store all spam emails as a list of words appearring in email
good_emails = [] # 2D list to store all non-spam emails as a list of words appearring in email

spam_training_set = [] # randomly choose 500 spam emails
good_training_set = [] # randomly choose 500 non-spam emails

spam_testing_set = [] # the rest of the spam emails go in here
good_testing_set = [] # the rest of the good emails go in here

spam_results_dict = {} # format.  dict = {0: 1, 1: 1, 2: 0, 3: 0};  { index in list: classified as spam(1) or non-spam (0) } label is positive for all in spam list.
non_spam_results_dict = {}

TP = 0 # label: pos(1), class: pos(1)
TN = 0 # label: neg(0), class: neg(0)
FP = 0 # label: neg(0), class: pos(1)
FN = 0 # label: pos(1), class: neg(0)
accuracy = 0 # (TP+TN)/(TP+TN+FP+FN)
precision = 0 # TP / (TP+FP)
recall = 0 # TP / (TP+FN)
F1 = 0 # (2*precision*recall)/(precision+recall)




# Part 1: read in data and fill data structures
#1A
# read in emails word by word and add each word to a list. Then store this list in spam or non-spam email 2D list.
#1B
# after reading in the email add a certain amount of random emails to the training sets and the rest to the testing sets
#1C
# for each new word in the training sets, add it to the word dictionary if not already in there if already in dictionary increment non-spam(0) or spam(1) count by 1.

#1A
try: 
    i = 1
    while(i <= 300):# read in non-spam emails
        temp_email = []
        readFile = open(non_spam_path1 + str(i) + '.txt','r')
        for line in readFile:
            for word in line.split():        
                temp_email.append(word)
        good_emails.append(temp_email[:])
        i+=1
    i = 1

    while(i <= 300):
        temp_email = []
        readFile = open(non_spam_path2 + str(i) + '.txt','r')
        for line in readFile:
            for word in line.split():        
                temp_email.append(word)
        good_emails.append(temp_email[:]) # append copy of temp email to list
        i+=1

    i = 1
    while(i <= 600):# read in spam emails
        temp_email = []
        readFile = open(spam_path + str(i) + '.txt','r')
        for line in readFile:
            for word in line.split():       
                temp_email.append(word)
        spam_emails.append(temp_email[:])
        i+=1

except IOError:
    print("File not found.")
finally:
    readFile.close()

#1B. After reading in the email add a certain amount of random emails to the training sets and the rest to the testing sets
random.shuffle(spam_emails)# randomize emails
random.shuffle(good_emails) 
i =0
while i < training_emails/2: # fill training set for good emails
    good_training_set.append(good_emails[i])
    i+=1
while i < training_emails/2 + test_emails/2:# fill testing set for good emails
    good_testing_set.append(good_emails[i])
    i+=1
i=0
while i < training_emails/2: # fill training set for spam emails
    spam_training_set.append(spam_emails[i])
    i+=1
while i < training_emails/2 + test_emails/2: # fill testin g set for spam emails
    spam_testing_set.append(spam_emails[i])
    i+=1

#1C
# For each new word in the training sets, add it to the word dictionary if not already in there if already in dictionary increment non-spam(0) or spam(1) count by 1.
for i in good_training_set: # fill words dictionary with words in good training set
    for word in i:
        if word not in words:
            words[word] = {0: 1, 1:0}
        else:
            words[word][0] += 1
for i in spam_training_set: # fill words dictionary with words in good training set
    for word in i:
        if word not in words:
            words[word] = {0: 0, 1:1}
        else:
            words[word][1] += 1

print(len(words))
print(len(good_testing_set))
print(len(spam_testing_set))




# Part 2: learning: 
# for each word in words calculate probability: words[w][0] = words[w][0]/500   words[w][1] = words[w][1]/500
for i in words:
    words[i][0] = words[i][0]/(training_emails/2)
    words[i][1] = words[i][1]/(training_emails/2)

print("papyal: " + str(words["paypal"]))
print("company: " + str(words["company"]))
print("meeting: " + str(words["meeting"]))
print("dollars: " + str(words["dollars"]))
print("executive: " + str(words["executive"]))




# Part 3: Classifier
# for each email in testing sets 
#   for each word in email calculate probability it is spam and non-spam:
#       prob_non_spam *= words[word][0]
#       prob_spam *= words[word][1]
#   if spam > non-spam 
        # spam_test_results

# Part 4: print results
# calculate all metrics and print


