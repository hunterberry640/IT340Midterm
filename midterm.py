# Author: Hunter Berry
# Date: Mar 31, 2021
# Description: Naive bayesian classifier for spam
# In order to read the data correctly put the email data folder in the same directory as this file.
import random

non_spam_path1 = 'email data/Ham/300 good emails/'
non_spam_path2 = 'email data/Ham/301-600 good ones/'
spam_path = 'email data/Spam/'

training_emails = 1000     # adjust training_emails and test_emails to adjust size of training set vs test set
test_emails = 200

words = {}                  # dict to store training set words and probabilities. format     "lunch": {0: .5, 1: .7};

spam_emails = []            # 2D list to store all spam emails as a list of words appearring in email
good_emails = []            # 2D list to store all non-spam emails as a list of words appearring in email

spam_training_set = []      # randomly choose 500 spam emails
good_training_set = []      # randomly choose 500 non-spam emails

spam_testing_set = []       # the rest of the spam emails go in here
good_testing_set = []       # the rest of the good emails go in here

spam_results_dict = {}      # format.  dict = {0: 1, 1: 1, 2: 0, 3: 0};  { index in list: classified as spam(1) or non-spam (0) } label is positive for all in spam list.
non_spam_results_dict = {}

TP = 0          # label: pos(1), class: pos(1)
TN = 0          # label: neg(0), class: neg(0)
FP = 0          # label: neg(0), class: pos(1)
FN = 0          # label: pos(1), class: neg(0)
accuracy = 0    # (TP+TN)/(TP+TN+FP+FN)
precision = 0   # TP / (TP+FP)
recall = 0      # TP / (TP+FN)
F1 = 0          # (2*precision*recall)/(precision+recall)




# Part 1: read in data and fill data structures
#1A
# read in emails word by word and add each word to a list. 
# Then store this list in spam or non-spam email 2D list.
#1B
# after reading in the email add a certain amount of random emails 
# to the training sets and the rest to the testing sets
#1C
# for each new word in the training sets, add it to the word dictionary if not 
# already in there, if already in dictionary increment non-spam(0) or spam(1) count by 1.

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
while i < training_emails/2 + test_emails/2: # fill testing set for spam emails
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

# print(len(words))
# print(len(good_testing_set))
# print(len(spam_testing_set))




# Part 2: learning: 
# for each word in words calculate probability: words[w][0] = words[w][0]/500   words[w][1] = words[w][1]/500
for i in words:
    words[i][0] = words[i][0]/(training_emails/2)
    words[i][1] = words[i][1]/(training_emails/2)

# print("paypal: " + str(words["paypal"]))
# print("company: " + str(words["company"]))
# print("meeting: " + str(words["meeting"]))
# print("dollars: " + str(words["dollars"]))
# print("executive: " + str(words["executive"]))




# Part 3: Classifier
count = 0
for email in good_testing_set: #labelled negative (non-spam email set)
    good_prob_non_spam = 1
    good_prob_spam = 1
    for word in email:
        if word in words:
            good_prob_non_spam *= words[word][0]
            good_prob_spam *= words[word][1]
        else:
            good_prob_non_spam *= .5
            good_prob_spam *= .5
    if good_prob_non_spam >= good_prob_spam:
        non_spam_results_dict[count] = 0
    else:
        non_spam_results_dict[count] = 1
    count+=1

count = 0
for email in spam_testing_set: #labelled positive (spam email set)
    prob_non_spam = 1
    prob_spam =1
    for word in email:
        if word in words:
            prob_non_spam *= words[word][0]
            prob_spam *= words[word][1]
        else:
            prob_non_spam *= .5
            prob_spam *= .5
    if prob_non_spam >= prob_spam:
        spam_results_dict[count] = 0
    else:
        spam_results_dict[count] = 1
    count+=1




# Part 4: print results
# calculate all metrics and print
nonSpamEmails = 0
for nonSpam in non_spam_results_dict:
    if non_spam_results_dict[nonSpam] == 0:
        nonSpamEmails+=1
        TN += 1
    else:
        FP += 1
spamEmails = 0
for spam in spam_results_dict:
    if spam_results_dict[spam] == 1:
        spamEmails+=1
        TP += 1
    else:
        FN+=1
print("\n============ Naive Bayesian Classifier for Spam Detection ============")
print("\ntraining emails: " + str(training_emails) + 
"\nspam:\t\t " + str(int(training_emails/2)) + 
"\nnon-spam:\t " + str(int(training_emails/2)) + 
"\n\ntesting emails:  "  + str(test_emails) + 
"\nspam:\t\t " + str(int(test_emails/2)) + 
"\nnon-spam:\t " + str(int(test_emails/2)) )

print("\n============ Results ============")
print("\nspam/non-spam:\t " + str(TP+FP) + "/" + str(TN+FN))
print("TN:\t\t " + str(TN))
print("FP:\t\t " + str(FP))
print("TP:\t\t " + str(TP))
print("FN:\t\t " + str(FN))

accuracy = (TP+TN)/(TP+TN+FP+FN)
precision = TP / (TP+FP)
recall = TP / (TP+FN)
F1 = (2*precision*recall)/(precision+recall)

print("\nAccuracy:\t " + str(format(accuracy, '.5f')))
print("Precision:\t " + str(format(precision, '.5f')))
print("Recall:\t\t " + str(format(recall, '.5f')))
print("F1:\t\t " + str(format(F1, '.5f')))


