#Author: Mothapo Rampedi Lesley
#Email: rampedilesley@gmail.com
#30 April 2021

"""
Write a Python script to check whether a given key already exists in a dictionary

"""
#define a dictonary called customer
customer = {
    "name" : "Mothapo Rampedi",
    "age" : 33,
    "language" : "Python"
   
}
print(customer.keys())
new_key = input("Enter a key: ")

if new_key in customer:
    print("Key exist")
    
else:
     print("Key does not exist")
