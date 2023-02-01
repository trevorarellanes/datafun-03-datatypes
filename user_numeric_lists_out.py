"""
Trevor Arellanes
Data Analytics Fundamentals

Task 3. Numeric Lists - Create lists (list1, listx, listy)

Lists 2 - Correlation and Prediction

We will let list1 represent number of bacteria in a sample from a patient in millions, and let listx represent time with patients spent by physician.
Listy will represent the resulting patient satisfaction scores.

Below are some stastistical calculations to analyze the data given.

The mean of list1 = 331.1
The median of list1 = 289.5
The mode of list1 is = 114

The standard deviation of list1 = 270.98
The variance of list1 = 73427.88
The correlation of listx and listy = 0.95

The slope intercept of listx and listy = 14.45, 89.00
The slope is = 14.45
And the Y-intercept is = 89.00

Let's try to predict some data next.

Given the time with physicians of 15, the predicted patient satisfaction survey score is = 305.82
This makes sense as the general trend of the data is positive.

Lists 3 - Using Python Built - in Functions

Below are some Python Built-in Function results on the list1 data
The lowest colony of bacteria: 25
The largest colony of bacteria: 889
Number of colonies of bacteria: 20
Sum of bacteria: 6622
Average bacteria: 331.1
Set for bacteria: {258, 788, 25, 29, 159, 444, 321, 322, 585, 78, 469, 352, 97, 864, 101, 366, 114, 247, 889}
Bacteria sorted ascending: [25, 29, 78, 97, 101, 114, 114, 159, 247, 258, 321, 322, 352, 366, 444, 469, 585, 788, 864, 889]
Bacteria sorted descending: [889, 864, 788, 585, 469, 444, 366, 352, 322, 321, 258, 247, 159, 114, 114, 101, 97, 78, 29, 25]

Lists 4 - List Methods

Below are a demonstration of using List Methods

Beginning with the original list: 55, 105, 225, 255.
We can add 300 to the end of the list:

[55, 105, 225, 255, 300]

Here we extend the list to add 1, 2, 3 at the end:
[55, 105, 225, 255, 300, 1, 2, 3]

Here we insert 525 into the list at the 3rd index of the list:
[55, 105, 225, 525, 255, 300, 1, 2, 3]

Here we remove 525 from the list
[55, 105, 225, 255, 300, 1, 2, 3]

Here we count how many times "2" appears in the list:
1

Here we sort the list in ascending order:
[1, 2, 3, 55, 105, 225, 255, 300]

Here we sort the list in descending order:
[300, 255, 225, 105, 55, 3, 2, 1]

Below we copy lst to a newlst:
[300, 255, 225, 105, 55, 3, 2, 1]

Here we take our new list and remove the first number of the list:
The old list: [300, 255, 225, 105, 55, 3, 2, 1] has 300 removed from it
leaving the current list: [255, 225, 105, 55, 3, 2, 1]

Below we remove the last number from the list:
The previous list has 1 removed leaving: [255, 225, 105, 55, 3, 2]

List 5 - List transformations using filter and map functions

Let's isolate the previous list to numbers below 100:
[55, 3, 2, 1]

Next, we will show each of the remaining numbers from the previous list square rooted:
[7.42, 1.73, 1.41, 1.0]

Now we will use the map function to find the volume of a cube using the number 2 from our list
Since there is only 1 occurence of 2 in our list, the result is: [8]
[8]

List 6 - List Transformations - Using List Comprehension

Below we will find the numbers above 105 using list comprehension.
The result is listed below:
[300, 255, 225]

Below we will triple each number in lst:
[900, 765, 675, 315, 165, 9, 6, 3]

Next I will transform the data by subtracting 10 from each number:
The result is:
[290, 245, 215, 95, 45, -7, -8, -9]
"""