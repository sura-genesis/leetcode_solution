Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

    Input: s = "()"
    Output: true
Example 2:

    Input: s = "()[]{}"
    Output: true
Example 3:

    Input: s = "(]"
    Output: false

#solution 
in this probleam we have the string with different kinds of parentheses our goal is to idetify the valid parentheses contained in the string.

      1. Two-pass iteration:
      
           Iterate through the string and find if the string contain the valid parentheses with in the string
      
      2. Recursive approach:
       
       Check the stack at the end and the opening 
      
      3. Regular expressions:
      
      
      4. Finite state automata (FSA):


      5, by the using map 

      6, by using a hash table 

  

          

  


