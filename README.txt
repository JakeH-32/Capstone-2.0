Universal Automated Tutor Guide


How to run the tutor: Enter the Controller foler, then click one of the two *.exe files or if you want to run in python, open the UAT.py file, download the packages, then run the file.


Here is a brief overview of all the files used in our tutor:

autograder.py - Overview: This file is to be pasted in place of the normal cs110 autograder, as it sends information from the autograder to our listener (in UAT).

UAT Testing Procedure.docx -	Overview: This outlines how to get the tutor working properly on someone's machine.


Folder - Controller:

UAT.py -	Overview: This file is to be run throughout the duration of the tutoring process
		1. It will begin by running initialize.py, which initalizes the first question, the problem difficulty values, and the distributions of each question
		2. The initial question is printed, and the student then opens that file and begins coding an answer
		3. It constantly waits for a submission, adds the submissions to a df until a score of 100, 
		4. Once a score of 100 is submitted, the df is condensed to one line: student_id, problem, total incorrect, total hints, and total duration
		5. Then, this data, along with the current problem, questionDifficulty, and distributions is sent to modelBuilder.py to generate the next question
		6. Once this question is printed, the process iterates back to step 2 and this process repeats until the tutor session is complete.

initialize.py - Overview: This file is to be run when booting up UAT.py
		1. The initialize() function imports the data.csv to then initialize the first question, the problem difficulty values, and the distributions of each question
		2. This function calls modelBuilder.py for each line, as modelBuilder.py contains all the functions needed to generate these dataframes.

modelBuilder.py - 	Overview: This file is the backbone of the model, it contains all necessary functions to create the model and to generate the next question
			1. The main files are importData(), distributionBuilder(), difficulty(), nextQuestion(), and startingQ(). 
			2. Every other function within modelBuilder supplements these functions.

problemDistributions.csv- 	Overview: Contains over 200 cs110 problems and their corresponding difficulty. This difficulty was found by normalizing (0-1) the number of hints, incorrect, and 
					the time it took students to answer. Using there three metrics, we added up their scores and divided by 3.

distributions.csv	-	Overview: Contains over 200 cs110 problems and their corresponding upper and lower bounds for duration, hints, and incorrect. 

*.spec files		- 	Overview: Needed for the *.exe files

"build" folder		- 	Overview: Needed for the *.exe files

UAT.exe			-	Overview: Runs the UAT without having to execute any python code or have packages installed.

UATwithDifficulty.exe	-	Overview: Runs the UAT (with difficulty) without having to execute any python code or have packages installed.


Folder - Labs:

"Labs" folder		-	Overview: Contains all the cs110 python files and corresponding htmls needed for students to use the tutor.


Folder - View:

NextQOutputScreen.ui 	-	Overview: This file has GUI interface information saved on it. For information on how to adjust it, please contact Jacob Hall.


How to run the tutor:

Either click one of the two *.exe files or if you want to run in python, open the UAT.py file, download the packages, then run the file.





