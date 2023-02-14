#!/usr/bin/env python
# coding: utf-8

# <h1><center>INNOVATIVE ASSIGNMENT</center></h1>
# <h2>TOPIC :- BANKER'S ALGORITHM</h2>

# <b>Course Name and Code :- </b>Operating System (2CS403)<br>
# <b>Roll No and Name :-</b> 21BCE504 (Shashank Chaudhary)

# In[1]:


import numpy as np
import pandas as pd
from IPython.display import display_html


# <b>In these Section we had initialized the required variables and Lists</b>

# In[2]:


user_allocation = []
user_maximum = []
user_instances = []
user_available = []
user_remaining = []
user_sequence = []
available = []
process_no = 0
resource_no = 0


# <center><h2>INPUTS</h2></center>

# <p>User has 2 Options to run the banker's algorithm :- <br><b>1.By Entering Total Instances of the Resources<br>2. By Entering the Available Matrix of the Resources.</b><br>User have to select the appropriate option according to there needs and can move further by entering the Total Numbers of Resources and Total Numbers of Processes.</p>

# In[3]:


ch = int(input("How Do You Want to Enter Data ?\n1. By Instances of Resources.\n2. By Available Matrix of Resources.\nEnter Your Choice : "))
resource_no = int(input("Enter No of Resources : "))
process_no = int(input("Enter No of Processes : "))      


# In[4]:


def find_available():
    tmp = []
    allocation_arr = np.array(user_allocation,dtype=int)
    summation = allocation_arr.sum(axis=0)
    tmp.append((user_instances-summation))
    global user_available 
    user_available = tmp[0].tolist()
    print("Available Matrix : ")
    print(user_available)
def find_instances():
    tmp = []
    allocation_arr = np.array(user_allocation,dtype=int)
    summation = allocation_arr.sum(axis=0)
    tmp.append((summation+user_available))
    global user_instances
    user_instances = tmp[0].tolist()
    print("Instance Matrix : ")
    print(user_instances)


# <b>Now, User has to enter the Allocation Matrix of all the Resources Process Wise.<br>
#    User have to Input the Values Space Seprated per Process.</b>

# In[5]:


print("Enter Allocation Matrix :- ")
for i in range(process_no):
    user_allocation.append(input(f"Enter Allocation Resources for Process {i} : ").split())
    user_allocation[i] = list(map(int,user_allocation[i]))
    
    
dataframe_rows = []
for i in range(process_no):
    dataframe_rows.append("P"+str(i));
dataframe_columns = []
for i in range(resource_no):
    dataframe_columns.append("Resource "+str(i))
dataframe1 = pd.DataFrame(user_allocation,index=dataframe_rows,columns=dataframe_columns)
dataframe1


# <b>Now, User has to Enter the Maximum Need Matrix of all the Resources, Process Wise<br>
#    User has to enter the Values Space Seprated per process.</b>

# In[6]:


print("Enter Maximum Need Matrix :- ")
for i in range(process_no):
    user_maximum.append(input(f"Enter Maximum Resources for Process {i} : ").split())
    user_maximum[i] = list(map(int,user_maximum[i]))
    
dataframe2 = pd.DataFrame(user_maximum,index=dataframe_rows,columns=dataframe_columns)
dataframe2


# <b>If User has Selected to input the Total Instances of Resource then User has to enter total available instances of resources or user has to enter the current available matrix of resources.</b>

# In[7]:


if ch==1:
    user_instances.clear()
    user_available.clear()
    user_instances.append(input("Enter Instances of Each Resources : ").split())
    user_instances = list(map(int,user_instances[0]))
    print(user_instances)
    find_available()
elif ch==2:
    user_available.clear()
    user_instances.clear()
    user_available.append(input("Enter Available Matrix of Resources : ").split())
    user_available = list(map(int,user_available[0]))
    print(user_available)
    find_instances()


# <center><h2>SAFETY ALGORITHM</h2></center>
# <img src="Safety.png"
#      alt="Markdown Monster icon"
#      style="float: center; margin-right: 10px;" />

# <b>This Function is Used to Find the Remaining Matrix.<b>

# In[8]:


def reshape(list1,list2):
    last = 0
    res = []
    for ele in list1:
        res.append(list2[last : last + len(ele)])
        last += len(ele)
    return res
def find_remaining(allocation_matrix,maximum_matrix):
    tmp = []
    for i in range(process_no):
        for item1,item2 in zip(allocation_matrix[i],maximum_matrix[i]):
            tmp.append(item2-item1)
    global user_remaining 
    user_remaining = reshape(maximum_matrix,tmp)
    remain_df = pd.DataFrame(user_remaining,index=dataframe_rows,columns=dataframe_columns)
    print(remain_df)


# <b>This Function check's the Safe State of the Processes and if the process is in safe state then find the safe sequence of the process.</b>

# In[9]:


def find_sequence(allocation_matrix,remaining_need_matrix,available1):
    available_matrix = np.array(available1)
    allocation_matrix = np.array(allocation_matrix)
    y = 0
    global user_sequence
    global available
    ind = 0
    f = [0]*process_no
    ans = [0]*process_no
    print("\n")
    for k in range(5):
        for i in range(process_no):
            if (f[i] == 0):
                flag = 0
                for j in range(resource_no):
                    if (remaining_need_matrix[i][j] > available_matrix[j]):
                        flag = 1
                        break
                if (flag == 0):
                    print(f"Process {i} Executed!")
                    ans[ind] = i
                    ind += 1
                    for y in range(resource_no):
                        available_matrix[y] += allocation_matrix[i][y]
                        available.append(available_matrix[y].tolist())
                    f[i] = 1
    if(all(f)==1):
        print("\nSAFE STATE!")
        user_sequence.clear()
        for i in ans:
            user_sequence.append(i)
        available1 = np.array(available)
        available1.resize(process_no,resource_no)
        available = available1.tolist()
    else:
        print("UNSAFE STATE!")


# In[10]:


while True:
    choice = int(input("Select Operation :-\n1. Find Remaining Need Matrix.\n2. Find Safe Sequence.\n3. Exit.\nEnter Your Choice : "))
    if choice==1:
        user_remaining.clear()
        find_remaining(user_allocation,user_maximum)
    elif choice==2:
        user_sequence.clear()
        available.clear()
        find_sequence(user_allocation,user_remaining,user_available)
    elif choice==3:
        break
    else:
        print("Invalid Option!")


# <b>This Function is used to Print all the Tables and Safe Sequence of the Process if found!</b>

# In[11]:


rows = []
for i in range(process_no):
    rows.append("P"+str(i));
column = []
for i in range(resource_no):
    column.append("R"+str(i))
print("Initial Available : ",user_available)
print()
allocation_df = pd.DataFrame(user_allocation,index=rows,columns=column)
maximum_df = pd.DataFrame(user_maximum,index=rows,columns=column)
remaining_df = pd.DataFrame(user_remaining,index=rows,columns=column)
available_df = pd.DataFrame(available)
space = "\xa0" * 10
df1_styler = allocation_df.style.set_table_attributes("style='display:inline'").set_caption('Allocation')
df2_styler = maximum_df.style.set_table_attributes("style='display:inline'").set_caption('Maximum')
df2_t_styler = remaining_df.style.set_table_attributes("style='display:inline'").set_caption('Remaining')
df3_t_styler = available_df.style.set_table_attributes("style='display:inline'").set_caption('Available')
display_html(df1_styler._repr_html_()+space+df2_styler._repr_html_()+space+df2_t_styler._repr_html_()+space+df3_t_styler._repr_html_(), raw=True)
print("\n\nSafe Sequence :- \n")
for i in range(process_no - 1):
    print(" P", user_sequence[i], " ->", sep="", end="")
print(" P", user_sequence[process_no - 1], sep="")


# In[ ]:





# <center><h2>RESOURCE - REQUEST ALGORITHM</h2></center>
# <img src="capture.png"
#      alt="Markdown Monster icon"
#      style="float: center; margin-right: 10px;" />

# In[ ]:


while True:
    cho = int(input("Do You Want to Update any Process?\n1. YES.\n2. NO.\nEnter Your Choice : "))
    if(cho==1):
        backup_process_no = process_no
        backup_resource_no = resource_no
        backup_user_allocation = user_allocation.copy()
        backup_available = available.copy()
        backup_user_available = user_available.copy()
        backup_user_maximum = user_maximum.copy()
        backup_user_remaining = user_remaining.copy()
        backup_user_instances = user_instances.copy()
        backup_user_sequence = user_sequence.copy()
               
        res = []
        pr = int(input("Enter Process Number that you want to change : "))
        res.append(input(f"Enter Allocation Resources for Process {pr} : ").split())
        res[0] = list(map(int,res[0]))
        if ((all(res[0]) <= all(backup_user_maximum[pr])) and (all(res[0]) <= all(backup_user_available))):
            tmp = [element1 - element2 for (element1, element2) in zip(backup_user_available, res[0])]
            for i in range(len(tmp)):
                backup_user_available[i] = tmp[i]
            tmp = []
            tmp = [element1 + element2 for (element1, element2) in zip(backup_user_allocation[pr], res[0])]
            for i in range(len(tmp)):
                backup_user_allocation[pr][i] = tmp[i]
            tmp = []
            tmp = [element1 - element2 for (element1, element2) in zip(backup_user_remaining[pr], res[0])]
            for i in range(len(tmp)):
                backup_user_remaining[pr][i] = tmp[i]
            tmp = []
            available.clear()
            #find_remaining(backup_user_allocation,backup_user_maximum)
            find_sequence(backup_user_allocation,backup_user_remaining,backup_user_available)
        else:
            print("Number of Processes : ",process_no)
            print("Number of Resources : ",resource_no)
            print("Safe Sequence :- ")
            print(user_sequence)
            print("Cannot be done this operation!!")
            print("Previous Safe Sequence : ")
            print("Safe Sequence : ",user_sequence)
    elif(cho==2):
        print("THANKS FOR USING OUR SIMULATION!!!")
        break
    else:
        print("Invalid Option!")


# <b>This Section is for printing all the Tables and Safe sequence after Resource-Request Algorithm</b>

# In[28]:


rows = []
for i in range(process_no):
    rows.append("P"+str(i));
column = []
for i in range(resource_no):
    column.append("R"+str(i))

print("Initial Available : ",backup_user_available)
print()
allocation_df = pd.DataFrame(backup_user_allocation,index=rows,columns=column)
maximum_df = pd.DataFrame(backup_user_maximum,index=rows,columns=column)
remaining_df = pd.DataFrame(backup_user_remaining,index=rows,columns=column)
available_df = pd.DataFrame(available,columns=column)
space = "\xa0" * 10
df1_styler = allocation_df.style.set_table_attributes("style='display:inline'").set_caption('Allocation')
df2_styler = maximum_df.style.set_table_attributes("style='display:inline'").set_caption('Maximum')
df2_t_styler = remaining_df.style.set_table_attributes("style='display:inline'").set_caption('Remaining')
df3_t_styler = available_df.style.set_table_attributes("style='display:inline'").set_caption('Available')
display_html(df1_styler._repr_html_()+space+df2_styler._repr_html_()+space+df2_t_styler._repr_html_()+space+df3_t_styler._repr_html_(), raw=True)

print("\n\nSafe Sequence :- \n")
for i in range(process_no - 1):
    print(" P", user_sequence[i], " ->", sep="", end="")
print(" P", user_sequence[process_no - 1], sep="")


# In[ ]:




