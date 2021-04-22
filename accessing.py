#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import maincode as lbr 
#importing the main file("maincode" is the name of the file I have used) as a library 


lbr.create("Mohit",25)
#to create a key with key_name,value given and with no time-to-live property


lbr.create("Sitamarhi",70,90) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


lbr.read("Mohit")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


lbr.read("Sitamarhi")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


lbr.create("Mohit",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#use delete operation and recreate it

 
lbr.delete("Mohit")
#it deletes the respective key and its value from the database(memory is also freed)

lbr.read("Mohit")

#we can access these using multiple threads at a time like
#as per the operation 
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))  
t1.start()
t1.sleep()
#as per the operation
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))  
t2.start()
t2.sleep()
#and so on upto tn threads created

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

