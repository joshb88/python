#!/usr/bin/env python
# coding: utf-8

# # CS2311 - Data Structures and Algorithms with Python
# ## Homework 3
# ## Due Date: See BlackBoard

# ## Team Name (If Applicable): Team number 1

# ## Student Name(s): Joshua Boehm and Michelle Pogue

# **SUBMISSION GUIDELINES**
# 
# 1. First design, develop and test your code in a Jupyter notebook or other development environment
#    - You can expirement and try different things in this notebook
# 2. Then copy your final code and markdown cells into the Jupyter Notebook file (.ipynb) provided for the assignment and submit to Blackboard
#    - **Your submission file should be named HW3Final.ipynb**
#    - I must be able to open and run your notebook in order to grade it
# 3. Note that the Jupyter notebook provided for final submission may contain testing code to help you check that your output and expected match.  
#    - Follow the instructions in the notebook for copying your code and running the testing code
#    - The instructor may run additional tests to check that your code runs correctly
# 4. If asked, also provide any supporting files or images requested in the assignment
#    - If there are multiple files to submit you should zip the files into one folder and submit the folder
# 
# **GRADING CRITERIA:**
# 1. Good documentation/comments and program readability using both markdown cells and code comments
# 2. Algorithm/pseudo-code is explained in a markdown cell and is efficiently written
# 3. Program runs correctly for test cases with no syntax errors or logical errors
# 
# ***The instructor should be able to reproduce your work from your notebook.***

# ## 1. [40 points] Minimum in list algorithms – benchmark and plot

# ### Algorithm Steps (Linear):
# 1. Get the list of random integers
# 2. Set the first item to the minimum
# 3. For each item in the list compare to the previous minimum and set item to minimum if lower
# 4. Return the minimum found

# In[1]:


import timeit
import random


# In[2]:


# Complete the code
def p1_f_linear(x):

    """DocTest module Expected Output Test - don't change or delete these lines
        
    >>> x = [565, 872, 711, 964, 340, 761, 2, 233, 562, 854]
    >>> print("The minimum is: ",p1_f_linear(x))
    The minimum is:  2
    """
    # ******ENTER YOUR FINAL CHECKED CODE AFTER THIS COMMENT BLOCK*******************
    
    # Setting the first element as the tentative minimum
    minimum = x[0]
    
    # For each item in the list, compare to the tentative minimum and set item to minimum if lower
    
    for item in x:
        if item < minimum:
            minimum = item
    return minimum


# ### Algorithm Steps (Quadratic):
# 1. Get the list of random integers
# 2. Get first item and compare to all remaining items and look for the smallest value
# 3. Go to the next item in the list and repeat step 2
# 4. Return the minimum found

# In[3]:


# Complete the code
def p1_f_quadratic(x):

    """DocTest module Expected Output Test - don't change or delete these lines
        
    >>> x = [565, 872, 711, 964, 340, 761, 2, 233, 562, 854]
    >>> print("The minimum is: ", p1_f_quadratic(x))
    The minimum is:  2
    """

    # Given in the problem
    min = x[0]
    l = len(x)
    for i in range(l):
        for j in range(i+1,l):
            if x[i]<x[j] and x[i]<min:
                min = x[i]
    return min


# ### Create a function to do a benchmark for linear algorithm using test using timeit.Timer
# 1. Pass an array of random numbers and measure how long it takes to run the linear algorithm
# 2. Set **t.timeit(number=1)**.  Otherwise the code will run much more slowly.

# In[4]:


# Complete the code
def p1_timeit_linear(x):
    """DocTest module Expected Output Test - don't change or delete these lines
        
    >>> x=[2, 3, 4, 5, 6, 4, 0, 1]
    >>> lin  = p1_timeit_linear(x)
    >>> print(lin*1000_000>0.3)
    True
    
    """
    # ******ENTER YOUR FINAL CHECKED CODE AFTER THIS COMMENT BLOCK*******************
    linear = timeit.Timer(lambda: p1_f_linear(x))
    return linear.timeit(number=1)


# In[5]:


x = [600,200,300,400,500]
p1_timeit_linear(x)


# ### Create a function to do a benchmark for quadratic algorithm using test using timeit.Timer
# 1. Pass an array of random numbers and measure how long it takes to run the quadratic algorithm
# 2. Set **t.timeit(number=1)**.  Otherwise the code will run much more slowly.

# In[6]:


# Complete the code
def p1_timeit_quad(x):
    """DocTest module Expected Output Test - don't change or delete these lines
        
    >>> x=[2, 3, 4, 5, 6, 4, 0, 1]
    >>> lin  = p1_timeit_linear(x)
    >>> quad = p1_timeit_quad(x)
    >>> print(quad*1000_000>5)
    True
    >>> print(round(quad/lin,3)>1)
    True
    
    """
    quadratic = timeit.Timer(lambda: p1_f_quadratic(x))
    return quadratic.timeit(number=1)


# In[7]:


# Run your code by calling the function(s) 
# Always test your code to check that you get what you expect
if __name__ == '__main__':
    
# Test: p1_f_linear(x)
    # test list of random integers
    x = [565, 872, 711, 964, 340, 761, 2, 233, 562, 854]
    min = p1_f_linear(x)
    print("Linear: The minimum is: ", min)
    
# Test: p1_f_quadratic(x) 
    # test list of random integers
    x = [565, 872, 711, 964, 340, 761, 2, 233, 562, 854]
    min = p1_f_quadratic(x)
    print("Quadratic: The minimum is: ", min)
    
# Test: p1_timeit_linear(x) and p1_timeit_quad(). Check that running time is longer for quadratic algorithm   
    # test list of random integers
    x=[2, 3, 4, 5, 6, 4, 0, 1]
    linear_time  = p1_timeit_linear(x)
    quadratic_time = p1_timeit_quad(x)
    # ratio 
    print("Ratio of quad/linear is greater than 1: ",round(quadratic_time/linear_time,3))


# In[8]:


# ************************************************************************
# DocTest: RUN THIS CELL TO CHECK THAT YOUR CODE MATCHES THE EXPECTED OUTPUT
# ************************************************************************
# this code checks that your output matches the expected result
# continue to test your code until you get an Ok result for your test
# the instructor will run this test and possibly others to check your code
# Submit your code even if you can't get the tests to run without failures.
# The instructor will look at your code and try to spot any errors and provide feedback
if __name__ == '__main__':
    import doctest
    print("RUNNING UNIT TESTS - NO FEEDBACK = OK!!")
    doctest.testmod(verbose=False)   # Set verbose = True if you want to see detailed log


# ### Algorithm Steps for Benchmark Test:
# 1. Write a for loop to create arrays of random integers from 0 to 999 of size n with n ranging from 'Lowx' to 'Highx' in increments of 'Increment'
# 2. Run the linear time and quad time function for each of the arrays
# 3. Save the results in size, linear, and quad arrays
# 4. Calcuate the ratio of quadratic time to linear time
# 5. Display a table showing array size, linear time, quadratic time, and quadratic/linear time ratio

# In[9]:


# Complete/Enter your code

import random

# Size of random number arrays to test
Lowx      = 1
Highx     = 20_000
Increment = 2000

# Set up table header
print("Array Size".ljust(20),"Linear".ljust(20),"Quad".ljust(20),"Ratio".ljust(20))

# Set up arrays to hold values for run times
size   = []
linear = []
quad   = []

# Write a for loop to create the arrays of random numbers (0 to 999) for the different size arrays
# and run the benchmark tests
for n in range(Lowx,Highx,Increment):
    
    # create a random array of integers from 0 to 999 of size n
    x = [random.randint(0,999) for n in range(n)]
    
   
    # run the benchmark on each of the linear and quad functions
    lin_time    = p1_timeit_linear(x)
    quad_time   = p1_timeit_quad(x)
    
    # calculate the run time ratio of quadratic time to linear time
    ratio = quad_time/lin_time
    
    # print table showing array size, linear time, quadratic time and ratio of quadratic/linear time
    print("%-20s" % len(x),"%-20f" % lin_time,"%-20f" % quad_time,"%-20.3f" % ratio)
    
    #store the results in the arrays for plotting.
    size.append(len(x))
    linear.append(lin_time)
    quad.append(quad_time)


# ### Create linear, log time and NlogN time curves
# 1. Create curves for linear time, log time and NlogN time functions
# 2. Scale these so they can be overlaid on a chart

# In[10]:


# use this code
import math

# Create functions for linear, log time, and nlog time
# Set scale to get charts to plot on one chart
scale = 1/25_000

n_time = [(n*scale,math.log(n)*scale,n*math.log(n)*scale) for n in range(Lowx,Highx,Increment)]

# Use these arrays for your plots
lin_time  = [item[0] for item in n_time]
log_time  = [item[1] for item in n_time]
nlog_time = [item[2] for item in n_time]


# ### Create plot of your linear algorithm vs logN curve
# 1. Create a function to plot x vs y1, y2 with a title, legend, labelled x and y axis
# 2. Pass in the x, y1, y2 values as lists, and the label1, label2 for the legend and title for the plot
# 2. Plot the run time for your linear algorithm against the LogN curve
# 3. Plot the run time for your linear algorithm against the LogN curve
# 4. Your figure should look something like the figures shown (note your run times will be different becuase of our environment)

# In[40]:


# Complete/Enter your code
import matplotlib.pyplot as plt

def plot_scenario(x,y1,y2,label1,label2,Title):
    plt.plot(x, y1, label = label1)
    plt.plot(x, y2, label = label2)
    plt.title(Title)
    plt.legend()
    
    plt.show()                          


# ### Figure 1:  Runtime for linear algorithm

# In[41]:


plot_scenario(size,linear,log_time,"Linear","Log Time","Linear Algorithm")


# ### Figure 2:  Runtime for quadratic algorithm

# In[42]:


plot_scenario(size,quad,nlog_time,"Quadratic","NlogN","Quadratic Algorithm")


# ### Try to answer the following questions:

# 1. Why do we use an array of random integers to run our benchmark tests?
# 
# Answer: We use arrays of random integers in order to produce more accurate results: as the graphs show, there are certain values (read: breakpoints) for which a certain test is superior to the others; an array filled with `n` integers randomly generated makes it simpler to test.

# 2. What could account for the “jagged” shape of the run-times in the plots?
# 
# Answer: Well, I don't have any "jagged" shapes in my curve, but assuming there were: the "jagged-ness" of the curve could be attributed to resource management of the machine running the test at that particular time. Another variable to consider is the incriments chosen in the size of each testing batch. It goes up by 10% of the total number of tests each incriment.

# 3. Is this a big enough sample size to be confident that we understand the Big-O performance of the algorithms – why or why not?
# 
# Answer: For these cases, yes. It's reasonably sound that these tests are accurate based on the visual representation of their curves plotted. The plotted curves are indicative of each functions Big-O status.
