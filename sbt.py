import subprocess
import sys
import os

# asking for standard inputs from the user
c_filename =str(input("C source file path: \n"))
test_folder_path = str(input("Test file directory path: \n"))

# ./pa1/pythagorean/pythagorean.c

c_compile = "gcc -Wall -Werror -std=c11 " + c_filename + " -o pythagorean -lm"

# running the c file and compiling
# "result" = CompletedProcess instance
result = subprocess.run(c_compile, shell = True)
if result.returncode != 0:
    print("failed to compile your code")
    sys.exit()
else:
    test_dir_obj_1 = os.scandir(test_folder_path)    
    for entry in test_dir_obj_1:
            #make a os.scandir object with the path as entry.path
         test_dir_obj_2 = os.scandir(entry.path)
         for entry_2 in test_dir_obj_2:
             if entry_2.name ==  "input.txt":
                 run_1 = os.popen("./pythagorean < " + entry_2.path)
                 # get the output
                 machine_output = run_1.read()
                 #print the output
             else:
                 run_2 = open(entry_2.path)
                 original_output = run_2.read()
             #make comparisons here
         for x in range(3):
             if machine_output[x] != original_output[x]:
                 print("#### Test: " + entry.name +  " failed! ####")
                 print("#### EXPECTED TO SEE:")
                 print(run_2.read())
                 print("#### INSTEAD GOT:")
                 print(run_1.read())
         print("#### Test: " + entry.name +  " passed! ####")     
                    
                        
                    
