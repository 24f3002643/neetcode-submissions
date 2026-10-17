## Idea of Optimized Approach
- We need to use a stack.
- The key idea is that at any moment the elements of the stack will be in decreasing order i.e. top element will always be the smallest element in the stack.
- Now, while inserting the element into the stack, we check if the current element is smaller than the top element or not.
    - If yes (i.e. smaller), insert the current element into the stack.
    - If not, then pop the top element, and update the index of the popped element in result to "current index - index of popped element". 
    - Repeat this process till the current element is smaller than the current element.
- What is the idea behind this :
    - This monotonic approach of inserting value in stack ensure that the element in the stack only get processed when the current element is bigger than it, thus satisfying the criteria of a warmer day of the question.
    

