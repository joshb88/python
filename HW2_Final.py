#!/usr/bin/env python
# coding: utf-8

# # CS1311-Introduction to Programming with Python
# ## Homework 2
# ## Due Date: 8th of February, 2022

# ## Team Name (if applicable): Group 1

# ## Student Name(s): Joshua Boehm, Michelle Pogue

# **SUBMISSION GUIDELINES**
# 
# 1. First design, develop and test your code in a Jupyter notebook or other development environment
#    - You can expirement and try different things in this notebook
# 2. Then copy your final code and markdown cells into the Jupyter Notebook file (.ipynb) provided for the assignment and submit to Blackboard
#    - **Your submission file should be named HW2_Final.ipynb**
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

# ## Prob 1. [15 points] Comparing two text files

# ### Algorithm Steps:
# 1. Define function to fetch lines from two seperate files and compare them.
#    - Set default files to the ones used in this assignment to accept no arguments.
# 2. Open both "myfile.txt" and "correct.txt" in read as file1 and file2.
#    - By using **with**, it's ensured the files will close automatically after each execution thus limiting errors with I/O issues related to unopened files.
# 3. Set an accumulator to zero to deal with each line number.
#    - This will be used to keep count of each line when printing the output.
# 4. Start a for loop to read each line of "myfile.txt" sequentionally.
#     - Here, we increase the accumulator to 1, starting on the first line of the file.
# 5. In the outer loop of each line in "myfile.txt", start another loop to read the line reflected by the accumulator's value in the file "correct.txt".
#     - With each iteration, the accumulator will also increase to indicate which line is currently being evaluated.
# 6. Compare the two lines of each file, "myfile.txt" and "correct.txt".
#     - If the two lines are equivalent, then print a statement indicating as such.
#     - If the two lines differ, create a list of each files line (as indicated by the accumulator) and display those lists respectively.
# 7. End that iteration of the loops and continue until all lines have been compared.

# In[68]:


# Code for this Problem is copied into this function that will be run the in main program
def file_compare(file1 = 'myfile.txt',file2 = 'correct.txt'):
    
   
    # *******************************************************************************
    # ENTER YOUR FINAL CHECKED CODE AFTER THIS COMMENT BLOCK
    # NOTE:  You may want to check and develop your code in another notebook before
    # copying it here. 
    # YOUR CODE MUST BE CORRECTLY INDENTED OR IT WONT RUN
    # *******************************************************************************
    
    
    with open('myfile.txt', 'r') as file1, open('correct.txt', 'r') as file2:
        line_number = 0
        for line_myfile in file1:
            line_number += 1
            for line_correct in file2:
                if line_myfile == line_correct:
                    print("Line>\t", line_number, "  - same")
                else:
                    correct_as_list = line_correct.splitlines(True)
                    myfile_as_list = line_myfile.splitlines(True)
                    print("Line>\t", line_number, "  in myfile is different\n")
                    print("\t\tCORRECT>>")
                    print(correct_as_list)
                    print("\t\tMYFILE>>")
                    print(myfile_as_list, "\n")
                break
    


# In[71]:


file_compare(myfile,correct)


# In[72]:


# Run your code by calling the function 
# Always test your code to check that you get what you expect
if __name__ == '__main__':
    file1 = "myfile.txt"
    file2 = "correct.txt"
    file_compare(file1,file2)  


# ## Prob 2. [20 points] Counting Duplicate Words

# ### Algorithm Steps:
# 1. Enter text into function to be used.
#    - Check if anything is provided; otherwise, the function will default to the variable **text**.
#    - If a string entry is used, convert the tuple the argument passes back into a string.
# 2. Save the text entered as a lower case, in order to be properly evaluated in the dictionary later.
# 3. Convert the variable entry, which is now a lowercase string, into a list.
#    - This will allow the function to more easily convert the data into a dictionary.
# 4. Creates a dictionary using the unique words (which appear more than once) as keys and their frequency as values.
#    - Utilize dictionary comprehension to formulate the data as keys (the words) and values (their frequency).
# 5. Display the results in a two-columned table.

# In[126]:


# Code for this Problem is copied into this function that will be run the in main program
def p1_word_counts(*str):

    # *******************************************************************************
    # EXPECTED OUTPUT FROM YOUR CODE
    #
    # The following is the expected output from your code that will be tested for
    # By the 'DocTest' module.
    # Do not change these lines or the test will fail. Your instructor may run 
    # additional test scenarios on your code so check your code carefully.
    # *******************************************************************************
    """Tokenize a string
        
    >>> text = ('this is sample Text with several words this is more sample text with some different Words')
    >>> p1_word_counts(text)
    WORD        COUNT
    is          2
    sample      2
    text        2
    this        2
    with        2
    words       2
    
    >>> text = ('how much wood could a wood chuck chuck if a wood chuck could chuck wood')
    >>> p1_word_counts(text)
    WORD        COUNT
    a           2
    chuck       4
    could       2
    wood        4
    
    >>> text = ('this is the time for all good men to come to the aid of their country')
    >>> p1_word_counts(text)
    WORD        COUNT
    the         2
    to          2
    """

    # *******************************************************************************
    # ENTER YOUR FINAL CHECKED CODE AFTER THIS COMMENT BLOCK
    # NOTE:  You may want to check and develop your code in another notebook before
    # copying it here. 
    # YOUR CODE MUST BE CORRECTLY INDENTED OR IT WONT RUN
    # *******************************************************************************
    


    # The function will check if an argument was provided. 
    # If not, it will default to the variable text.

    if str == ():
        entry = text
        
    # If a string was provided as the argument instead, 
    # the function will convert the tuple output back into a string.
    
    else:
        entry = "".join(str)

    # Set the case of the string to lower to accurately evaluate.

    entry = entry.lower()

    # Makes a list out of the variable entry.           

    words = entry.split()

    # Creates a dictionary using the unique words as keys and their frequency as values, 
    # if and only if the words appear more than once.        

    counts = {word: words.count(word) for word in words if word in words if words.count(word) > 1}
    interim = counts.items()
    sorted_counts = dict(sorted(interim))


    # Prints a 2 column table of the words and their counts
    # In the instructions, it specifies a field width of 12, but it's actually 11.
    
    print('{:11}'.format("WORD"),"COUNT")
    for key, value in sorted_counts.items():
        print('{:11}'.format(key),value)

text = ('this is sample Text with several words this is more sample text with some different Words')
            
p1_word_counts()
    


# In[113]:


# Run your code by calling the function 
# Always test your code to check that you get what you expect
if __name__ == '__main__':
    text = ('this is sample Text with several words ' +
            'this is more sample text with some different Words')
    p1_word_counts(text)
    print()
    
    text = ('this is the time for all good men to come to the aid of their country')
    p1_word_counts(text)
    print()
    
    text = ('how much wood could a wood chuck chuck if a wood chuck could chuck wood')
    p1_word_counts(text)
    print()


# ## Prob 3. [20 points] Duplicate Word Removal

# ### Algorithm Steps:
# 1. Enter text into function to be used.
#    - Check if anything is provided; otherwise, the function will default to the variable **text**.
#    - If a string entry is used, convert the tuple the argument passes back into a string.
# 2. Clean the data to be handled as a set.
#     - Remove periods.
#     - Force the case to lower.
#     - Change the string into a list.
# 3. Organize the relevant data.
#     - Create a set of the list in order to keep only unique words.
#     - Sort the set alphabetically.
# 4. Display the information.
#     - Print the data in a singular column.

# In[118]:


# Code for this Problem is copied into this function that will be run the in main program
def p2_unique_words(*str):

    # *******************************************************************************
    # EXPECTED OUTPUT FROM YOUR CODE
    #
    # The following is the expected output from your code that will be tested for
    # By the 'DocTest' module.
    # Do not change these lines or the test will fail. Your instructor may run 
    # additional test scenarios on your code so check your code carefully.
    # *******************************************************************************
    """Unique words in a string
        
    >>> text = ('This. is. sample. text. with. several. words. This is more sample text with some different Words')
    >>> p2_unique_words(text)
    UNIQUE SORTED WORDS:
    different
    is
    more
    sample
    several
    some
    text
    this
    with
    words
    """

    # *******************************************************************************
    # ENTER YOUR FINAL CHECKED CODE AFTER THIS COMMENT BLOCK
    # NOTE:  You may want to check and develop your code in another notebook before
    # copying it here. 
    # YOUR CODE MUST BE CORRECTLY INDENTED OR IT WONT RUN
    # *******************************************************************************

    # The function will check if an argument was provided. 
    # If not, it will default to the variable text.
    
    if str == ():
        entry = text
        
    # If a string was provided as the argument instead, 
    # the function will convert the tuple output back into a string.
        
    else:
        entry = "".join(str)
    
    # Remove periods, force the case to lower, and change the string into a list.
    
    entry = entry.replace(".","")
    entry = entry.lower()
    entry = entry.split()
    
    # Create a set, i.e. omit duplicate values, and sort it alphabetically from the list. 
    
    unique_words = sorted(set(entry))
    
    # Print the alphabetized set as a column.
    
    print("UNIQUE SORTED WORDS:")
    for words in unique_words:  
        print(words)
    
text = ('this is sample Text with several words this is more sample text with some different Words')    
    
p2_unique_words(text)
    


# In[127]:


# Run your code by calling the function 
# Always test your code to check that you get what you expect
if __name__ == '__main__':
    text = ('This. is. sample. text. with. several. words. This is more sample text with some different Words')
    p2_unique_words(text)


# ## Prob 4. [20 points] Dictionary Manipulations

# ### Algorithm Steps:
# 1. Establish both the dictionary "d" and the parameters "params"
#    - Both will be used to fetch data and manipulate it in the program 
# 2. Check whether the dictionary contains the key 'Canada'.
#    - Using indexing with the params list, check if the value associated with Canada is in the dictionary's keys.
# 3. Check whether the dictionary contains the key 'France'.
#    - Using the same method, perform the same task with France.
# 4. Iterate through the key???value pairs and display them in two-column format.
#     - Use a for loop to print each key and value inline.
# 5. Add a key-value pair, Sweden: sw, to the dictionary.
# 6. Correct the same, newly added key-value pair with a new value.
#     - Change the value from "sw" to "se".
# 7. Inverse the keys and values through the use of the dictionary comprehension.
# 8. Utilize dictionary comprehension again to capitalise the names of the countries.

# In[131]:


d = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}


# In[16]:


# Code for this Problem is copied into this function that will be run the in main program
def p3_Dictionary_Manipulations(d,params):

    # *******************************************************************************
    # EXPECTED OUTPUT FROM YOUR CODE
    #
    # The following is the expected output from your code that will be tested for
    # By the 'DocTest' module.
    # Do not change these lines or the test will fail. Your instructor may run 
    # additional test scenarios on your code so check your code carefully.
    # *******************************************************************************
    """
    >>> d = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
    >>> params = ['Canada','France','sw','se']
    >>> p3_Dictionary_Manipulations(d,params)
    Dictionary is:
    {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'} 
    <BLANKLINE>
    a. Canada in dict:
    True 
    <BLANKLINE>
    b. France in dict:
    False 
    <BLANKLINE>
    c. Keys and values in dict (key in field width 20):
    Canada              ca
    United States       us
    Mexico              mx
    <BLANKLINE>
    d. Dict with Sweden set to 'sw':
    {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx', 'Sweden': 'sw'} 
    <BLANKLINE>
    e. Dict with Sweden corrected to 'se':
    {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx', 'Sweden': 'se'} 
    <BLANKLINE>
    f. Reverse mapping using dictionary comprehension:
    {'ca': 'Canada', 'us': 'United States', 'mx': 'Mexico', 'se': 'Sweden'} 
    <BLANKLINE>
    g. Reverse mapping uppercase using dictionary comprehension:
    {'ca': 'CANADA', 'us': 'UNITED STATES', 'mx': 'MEXICO', 'se': 'SWEDEN'} 
    <BLANKLINE>
    """

    # *******************************************************************************
    # ENTER YOUR FINAL CHECKED CODE AFTER THIS COMMENT BLOCK
    # NOTE:  You may want to check and develop your code in another notebook before
    # copying it here. 
    # YOUR CODE MUST BE CORRECTLY INDENTED OR IT WONT RUN
    # *******************************************************************************
    
    
    print("Dictionary is:")
    print(d, "\n")

    # Check whether the dictionary contains the key 'Canada'.
    
    print("a. Canada in dict:")
    print(params[0] in d,"\n")
    
    # Check whether the dictionary contains the key 'France'.
    
    print("b. France in dict:")
    print(params[1] in d,"\n")
    
    # Iterate through the key???value pairs and display them in two-column format.
    
    print("c. Keys and values in dict (key in field width 20):")
    for key in d:
        print('{:20}'.format(key),d[key], sep = "")
        
    # Add the key-value pair to the dictionary.
    
    print("\nd. Dict with Sweden set to 'sw':")
    d["Sweden"] = params[2]
    print(d,"\n")
    
    # Update the key-value pair to correct the mistaken value.
    
    print("e. Dict with Sweden corrected to 'se':")
    d["Sweden"] = params[3]
    print(d,"\n")
    
    # Use a dictionary comprehension to reverse the keys and values.
    
    print("f. Reverse mapping using dictionary comprehension:")
    d2 = {tld: country for country, tld in d.items()}
    print(d2,"\n")
    
    # Use a dictionary comprehension to convert the country names to all uppercase letters.
    
    print("g. Reverse mapping uppercase using dictionary comprehension:")
    d2 = {tld: country.upper() for tld, country in d2.items()}
    print(d2,"\n")    


# In[12]:


# Run your code by calling the function 
# Always test your code to check that you get what you expect
if __name__ == '__main__':
    # set up the dictionary & parameters
    d = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
    params = ['Canada','France','sw','se']

    # Call the function to run and print out the scenarios in the script
    p3_Dictionary_Manipulations(d,params)


# In[17]:


# ************************************************************************
# RUN THIS CELL TO CHECK THAT YOUR CODE MATCHES THE EXPECTED OUTPUT
#*************************************************************************
# this code checks that your output matches the expected result
# continue to test your code until you get an Ok result for your test
# the instructor will run this test and possibly others to check your code
# Submit your code even if you can't get the tests to run without failures.
# The instructor will look at your code and try to spot any errors and provide feedback
if __name__ == '__main__':
    import doctest
    print("RUNNING UNIT TESTS - SEE THE LOG FOR FEEDBACK>>>")
    doctest.testmod(verbose=True)

