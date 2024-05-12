##################
### Copy Lists ###
##################

import copy

list_org = ["banana", "cherry", "apple"]# original list

list_cpy1 = list(list_org)              # use list function
list_cpy2 = list_org[:]                 # use slice
list_cpy3 = list_org.copy()             # use copy function
list_cpy4 = copy.deepcopy(list_org)     # from copy modul the deepcopy function  

list_cpy1.append("lemon")               # just the copy get a new element
list_cpy2.append("lemon")               
list_cpy3.append("lemon")               
list_cpy4.append("lemon")

print(list_org)                         # seeing the result                         
print(list_cpy1,"\n",                   
      list_cpy2,"\n",                   
      list_cpy3,"\n",                   
      list_cpy4                         
      )


##########################
### List Comprehension ###
##########################

mylist = [1, 4, 3, 4, 5, 6]             # just a unsorted list
b = [i*i for i in mylist]               # list comprehension

print(mylist)                           # printed list
print(b)                                # printed new list with the effect
                                        # of list comprehension

liste = [0] * 5 + mylist[:5]
