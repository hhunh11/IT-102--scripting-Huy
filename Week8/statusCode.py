import re
from collections import Counter

#path to the file
file='access.log'

"""
regex pattern for extractStatus function
"[A-Z]+ :       match any upper case words after request quotes (ex: GET,..)
[^"]+ :         match everthing inside the request quotes
HTTP/1\.[01]" : match this pattern
(\d{3}) :       grab any three-digits code into a group 
"""
pattern=r'"[A-Z]+ [^"]+ HTTP/1\.[01]" (\d{3})'


#reading all lines from the given file above
def readFile(f):
    with open(f,'r') as F:
        return F.readlines()

"""
Extract status code from 
    p : pattern
    logs : list from readFile function
return a list contain extracted status code
"""
def extractStatus(p,logs):
    statusCode=[]
    for line in logs:
        match=re.search(p,line)
        if match:
            statusCode.append(match.group(1))
    return statusCode

#printing result
def printStatus(c:Counter):
    for k,v in c.items():
        print(f"Status Code[{k}] : {v} times")

#gather all functions
def main():
    logsInput=readFile(file)
    StatusList=extractStatus(pattern,logsInput)
    #count status code occurence 
    counterList=Counter(StatusList)
    printStatus(counterList)

#run main function
main()
"""
Summary: This script reads an Apache access log file and extracts all HTTP status 
codes using a regular expression. It then counts how many times each status code 
appears by using Counter class. The results help show the occurence of each status code
"""
