import sys
###Rest of the code is in the jupyter notebook
filenames = []
if len(sys.argv) < 3:
    print("Need 3 filenames to execute the program.")
    
else:
    print("Permanent Employee Data File Name-", sys.argv[0])
    print("Employee Working Hours Data File Name-", sys.argv[1])
    print("Final File Name to save data-", sys.argv[2])
    print("--------------------")
    print("Please check the above data before proceeding.")
    for i in sys.argv:
        filenames.append(i)
    filenames.pop(0)
    print(filenames)

###OUTPUT
#Permanent Employee Data File Name- Ex3.2.py
#Employee Working Hours Data File Name- pmempdata.txt
#Final File Name to save data- wrkinghrs.txt
#--------------------
#Please check the above data before proceeding.
#['pmempdata.txt', 'wrkinghrs.txt', 'combineddata.txt']