#The aim of this assignment is to create a program that tracks fitness activities and calories burned.
Duration=[10,20,15]
Activities=["Dancing", "Swimming", "Biking"]
longest_time=max(Duration)
shortest_time=min(Duration)
longest_time__index__=Duration.index(longest_time)
shortest_time__index__=Duration.index(shortest_time)
total_time=[10, 20, 15]
combined_total=sum(total_time)
measures=3.5
#Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15]
for i in range (len(Activities)):
    if Activities != longest_time:
        print( "You spent a moderate time biking which totaled 15 minutes.")
 #  Task 2: Write a simple function that estimates calories burned based on the activity and duration. 
 #    Task 3: Create a summary function that provides a report of all activities and total calories burned for the day 
        print ("You spent the most time:",Activities[longest_time__index__])
        print ("You spent the least time:", Activities[shortest_time__index__])
        print ("The total amount of time you spent swimming in minutes =",total_time[longest_time__index__])
        print ("The total amount of time you spent dancing in minutes =", total_time[shortest_time__index__])
        print( "The total average time you spent exercising in total =", combined_total / (measures),"! Which is an average of 11.25 minutes per activity (rounded)! Good Job....", )
        break