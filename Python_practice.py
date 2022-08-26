import os
print(os.getcwd())
print ("Hello World")
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())
print(__file__)
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
    