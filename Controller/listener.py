# ---------------------------------------------
# SQL Helper
# Author:  Lt Col Adrian de Freitas / DFCS
# Date:  23 December 2021
# Purpose:  Performs Simple Queries on MYSQL Databases
# ---------------------------------------------
from datetime import datetime
import time
import pandas as pd
import socket
import numpy as np
import datetime
import matplotlib.pyplot as plt
import modelBuilder as mb
import main
import sys
import requests
import json
import dummyMain
    

nextQ, questionDifficulty, distributions = dummyMain.initialize()
print(nextQ)

host = socket.gethostname()
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as es:
    print(str(es))
    
s.listen(5)   

columns = ["student_id", "problem","timestamp","graded","score","sourcehash"]
attempt = pd.DataFrame(columns = columns)

while (True):
    # waits for notification from autograder, then fetches new submission 
    conn, addr = s.accept()
    print(f"conn from {addr}")
    tmsg = conn.recv(1024)
    #umsg = conn.recv(1024)
        
    timestamp = tmsg.decode("utf-8")
    #username = umsg.decode("utf-8")
    
    ts = time.localtime()
    tsStop = (time.strftime("%Y-%m-%d %H:%M:%S", ts))
    
    problem = "sample"
    #problem = nextQ
    course = "1"

    time.sleep(.5)

    API_Response = requests.get("https://tutor.dfcs-cloud.net/api/v1/getSubmissionHistory.php?apiKey=dfcs_capstone&course=" + course + "&problem=" + problem + "&start="+ timestamp, timeout = 3)

    response = API_Response.json()  #full resonse from API
    submissions = response.get("submissions")   #list of submissions
    num_submissions = response.get("size")  #number of submissions in 'submissions'
    
    print(response)
            #check if there is more than one submission
    if num_submissions == 1:
        submission = submissions.get("0")
            #else if more submissions check usernames ADD LATER
    
    
    
    submission.pop("user_name")
    responseSeries = pd.Series(submission)
    attempt = attempt.append(responseSeries, ignore_index=True)
    
    
    if submission["score"] == 100.0:
        qData = mb.convertRawtoClean(attempt)
        nextQ = mb.nextQuestion(problem, questionDifficulty, distributions, qData)
        attempt = pd.DataFrame(columns = columns)
        submission = ""
        QuestionLabelText = nextQ
        print(QuestionLabelText)
