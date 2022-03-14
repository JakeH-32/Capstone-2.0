Universal Automated Tutor Guide

Download the following python files and csv:

listener.py -	Overview: This file is to be run throughout the duration of the tutoring process; takes about 4 minutes to boot up
		1. It will begin by running main.py, which initalizes the first question, the problem difficulty values, and the distributions of each question
		2. The initial question is printed, and the student then opens that file and begins coding an answer
		3. It constantly waits for a submission, adds the submissions to a df until a score of 100, 
		4. Once a score of 100 is submitted, the df is condensed to one line: student_id, problem, total incorrect, total hints, and total duration
		5. Then, this data, along with the current problem, questionDifficulty, and distributions is sent to modelBuilder.py to generate the next question
		6. Once this question is printed, the process iterates back to step 2 and this process repeats until the tutor session is complete.

main.py - 	Overview: This file is to be run when booting up listener.py; takes about 4 minutes to boot up
		1. The initialize() function imports the data.csv to then initialize the first question, the problem difficulty values, and the distributions of each question
		2. This function calls modelBuilder.py for each line, as modelBuilder.py contains all the functions needed to generate these dataframes.

modelBuilder.py - 	Overview: This file is the backbone of the model, it contains all necessary functions to create the model and to generate the next question
			1. The main files are importData(), distributionBuilder(), difficulty(), nextQuestion(), and startingQ(). 
			2. Every other function within modelBuilder supplements these functions.

data.csv - 	Overview: Contains 600K+ student submissions into the CS110 autograder 