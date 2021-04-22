import threading 
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import*
import time

#'dictionary' is the dictionary(map like functionality) in which we store data in form of key-value pair
dictionary={} 

#Function for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in dictionary:
        #error message1
        print("error: this key already exists")  
    else:
        if(key.isalpha()):
            #constraints for file size less than 1GB and Jasonobject value less than 16KB 
            if len(dictionary)<(1024*1024*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                #constraints for input key_name capped at 32chars
                if len(key)<=32:  
                    dictionary[key]=l
            else:
                #error message2
                print("error: Memory limit exceeded!! ") 
        else:
            #error message3
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

#Function read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in dictionary:
        #error message4
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=dictionary[key]
        if b[1]!=0:
            #comparing the present time with expiry time
            if time.time()<b[1]:
                #to return the value in the format of JasonObject i.e.,"key_name:value"
                string=str(key)+":"+str(b[0])
                return string
            else:
                #error message5
                print("error: time-to-live of",key,"has expired")
        else:
            string=str(key)+":"+str(b[0])
            return string

#Function for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dictionary:
        #error message4
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=dictionary[key]
        if b[1]!=0:
            #comparing the current time with expiry time
            if time.time()<b[1]:
                del dictionary[key]
                print("key is successfully deleted")
            else:
                #error message5
                print("error: time-to-live of",key,"has expired")
        else:
            del dictionary[key]
            print("key is successfully deleted")
