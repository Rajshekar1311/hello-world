
# coding: utf-8

# In[5]:


# Question 1
# This is the first assignment for string operations in Python

print ('Apples are better than \\n oranges')


# In[15]:


# Question 2
# string_ex = “I love python because it is so easy to use it and also it is used by many other IT companies”
# I want you to split the above string on the separator “it”. How will you do it?
string_ex = "I love python because it is so easy to use it and also it is used by many other IT companies"

#sWords= [] ;
sWords = string_ex.split("it");

for x in sWords :
    print (x)
    


# In[45]:


#Question 3
#How do you swap the cases of letters in the input string?

string_ex = "I Love Python"
sAlterNateCase = string_ex.lower()
string_new = ""
inLen = len(string_ex)
i=0
while (i < inLen) :
    
    
    if ((string_ex[i].isupper()) == True):
        string_new += string_ex[i].lower()
    else:
        string_new += string_ex[i].upper()
        
    i = i + 1            
    
print (string_new)


# In[60]:


#Question 4
#str_input = “Hey how are you doing. I am doing great”
#Get the first 10 characters and the last 10 characters of the above the string and join them with a “_”
string_ex = "Hey how are you doing. I am doing great"

print (string_ex)
print (string_ex[:10])
print (string_ex[:10] + '_' + string_ex[10:20])
string_new = string_ex[:10] + '_' + string_ex[10:20]
print (string_new)

#string_arr=[]

#string_arr = "_".join(string_new)
#print (string_arr)


# In[106]:


#Question 5
#string1 = “Hotelspace”
#string2=”Facilities”
#I want you to swap the first three letters and last three letters of both the strings and print
#the output by separating them with a “@”

string1 = 'Hotelspace'
string2 = 'Facilities'
# get the first 3 and last 3 letters and get the middle part
string1_first_part = string1[:3]
string1_last_part = string1[len(string1)-3:len(string1)]

print ( string1_last_part + '@' + string1[3:len(string1)-3] + '@' + string1_first_part)

string2_first_part = string2[:3]
string2_last_part = string2[len(string2)-3:len(string2)]

print ( string2_last_part + '@' + string2[3:len(string2)-3] + '@' + string2_first_part)


# In[112]:


#Question 6
#How do you extract the string ‘Worl’ from the above string using negative inde
strr = 'Hello World'
str_arr= strr.split()
print (str_arr[1][:4])


# In[143]:


#question 7
# Reverse the string “5+6*3-45”. The output should be “45-3*6+5”.

strr = "5+6*3-45"
str_arr = strr.split('*')
str_arr1 = (str_arr[0][::-1])
str_arr2 = str_arr[1][2:4] + str_arr[1][1:2] +  str_arr[1][0:1]
print ( str_arr2  + '*' + str_arr1)


# In[207]:


#Question 8
#I want you to remove the common words appearing in the above strings and display the leftover words as one single string.

str_s = "India is a great country with a lot of heritage"
str_x = "South Africa is a great country with a lot of freedom"
#str_n = str_s + ' ' + str_x
str_s_arr = str_s.split()
str_x_arr = str_x.split()

i = 0
wordfound = 0
arr_found_s = []
arr_found_x = []
arr_found.clear()
# add the first element into the found array


for x in str_s_arr:
    wordfound = 0
    i = 0
    while (i < len(str_s_arr)):
        if (x == str_s_arr[i]):
            wordfound +=1
        i += 1

    if (wordfound == 1):
        arr_found_s.append(x)
        
for x in str_x_arr:
    wordfound = 0
    i = 0
    while (i < len(str_x_arr)):
        if (x == str_x_arr[i]):
            wordfound +=1
        i += 1

    if (wordfound == 1):
        arr_found_x.append(x)

str_finalstring = ""  
for x in arr_found_s:
    str_finalstring = str_finalstring + ' '  + x


for x in arr_found_x:
    str_finalstring = str_finalstring + ' '  + x

print (str_finalstring)


# In[220]:


# Question 9


#I want you to identify all the unique characters in the above string and also mention the
#number of times these unique characters are repeated in the above string.

arr_string=[]
variable1='This is a test to check the unique characters in the string'
new_string = ""
for x in variable1:
    count=0
    if (new_string.find(x) == -1):
        for y in variable1:
            if (x==y):
                count+=1
        new_string = new_string + x
        arr_string.append(x + " - " + str(count))

for a in arr_string:
    print (a)
    


# In[233]:


#Question 10
#I want you to transform the above string to “a2c4e8g10”
var3 = 'abcdefghijklmnopqrstuvwxyz'
int_a_ascii_value = 96
new_str = ""
for a in var3:
    if ((ord(a) - int_a_ascii_value) % 2 == 0 ):
        new_str += str(ord(a) - int_a_ascii_value)
    else:
        new_str += a
        
print (new_str)

