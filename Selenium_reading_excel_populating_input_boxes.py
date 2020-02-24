from selenium import webdriver
import csv
import time
# with open ("Testing_data.csv","w",newline="") as fw:
#     thewriter=csv.writer(fw)
#     thewriter.writerow(["Sl.No","Username","Email-ID","Password","Confirm password","Date of birth","Phone"])
#     thewriter.writerow([1,"Arun Kumar","arundruk@gmail.com","Jan1234","Jan1234","30-09-2000","6346365346"])
#     thewriter.writerow([2, "Swapna", "swapna@gmail.com", "Jan1234", "Jan1234", "30-09-1900", "6346376346"])

# with open("Testing_data.csv",'r') as fr:
# ####################################################################################################
# #Method1
#     thereader=csv.reader(fr)
#     data=list(thereader)
#     row_count=len(data)
#     print(type(data),data[1][1],row_count,sep="\n")
#     col_count=0
#     for i in data[0]:
#         col_count+=1
#     print("column length= ",col_count, "And the columns are: ", data[0],sep="\n")
####################################################################################################
#Method2
    # col=fr.readline() # readline returns string characters
    # col_count=col.count(",") +1
    # row=fr.readlines()  # readlines returns list of string characters
    # row_count=len(row)
    # print(col,col_count)
    # print(row,row_count,sep="\n")
    # print(type(row),row[0][1])
   # print(type(data),data[1][1],sep="\n")

driver=webdriver.Chrome()
driver.get("http://www.thetestingworld.com/testings/")
driver.maximize_window()
with open("Testing_data.csv",'r') as fr:
    thereader=csv.reader(fr)
    data=list(thereader)
    row_count=len(data)
    print(type(data),data[1][1],row_count,sep="\n")
    col_count=0
    for i in data[0]:
        col_count+=1
    print("column length= ",col_count, "And the columns are: ", data[0],sep="\n")
    # i=j=1
    for i in range(1,row_count):
        #for j in range(1,col_count):
        driver.find_element_by_name("fld_username").send_keys(data[i][1])
        driver.find_element_by_name("fld_email").send_keys(data[i][2])
        driver.find_element_by_name("fld_password").send_keys(data[i][3])
        time.sleep(5)





# After reading the csv file to print the output.

# for line in data:
#     for word in line:
#         print(word,"\t",end="")
#     print()


