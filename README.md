# C950-routing-program

This program is the final project for Western Governors University course C950 - Data Structures and Algorithms II

The project is a modified version of the Traveling Salesman problem.

The goal of this project was to create a program that took in a list of packages and a list of destinations and then sort and deliver the packages while keeping the total miles driven by all trucks under 140.

To achieve that goal I implemented the following:

          * A resizable hash-map only using lists (for this project, the use of dictionaries was prohibited)
          * A huristic "Greedy" algorithm to deliver packages.
          * A 2D adjacency matrix to store all destination nodes and related data
          

## Instructions

    Option #1 (PyCharm IDE):
    1.	Open project in PyCharm IDE
    2.	Navigate to main.py file within project directory
    3.	Right click on ‘class Main:’ 
    4.	Select option Run ‘main’
    5.	In PyCharm terminal select option #1 to run program 
    a.	*Running the program must be done before searching for packages or printing out all package status reports*
    6.	Once program has run, select option #2 to search for a package status report for a specific time.
    7.	Select option #3 to get a printout of the status of all packages at three specific times. 
    8.	Select option #4 to quit program. 

    Option #2 (Terminal):
    1.	Open terminal and navigate to wherever unzipped project folder is located
    2.	cd into project folder and type ‘python main.py’ and hit enter to run program
    3.	In terminal select option #1 to run program 
    a.	*Running the program must be done before searching for packages or printing out all package status reports*
    4.	Once program has run, select option #2 to search for a package status report for a specific time.
    5.	Select option #3 to get a printout of the status of all packages at three specific times. 
    6.	Select option #4 to quit program. 
    

## Senario 

The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and deliverydistribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by theirpromised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to delivereach day. Each package has specific criteria and delivery requirements.

Your task is to determine an algorithm, write code, and present a solution where all 40 packages (listed in the attached “WGUPS Package File”) will be delivered on time while meeting each package’s requirements and keeping the combinedtotal distance traveled under 140 miles for both trucks. The specific delivery locations are shown on the attached “SaltLake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent isto use the program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you madewhile writing your scripts.
