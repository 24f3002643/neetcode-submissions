# Optimized Approach
There are many optimized approach :
    - Hash Map : count the frequency of each unique element in a single pass, and return element with count > n//2.
    - Sorting : sort the array and return element at n//2 index.
    - Boyer-Moore Voting Algorithm
    - Randomization
    - Bit Manipulation
    
## Hash Map Approach
- In a single pass over the array, count the frequency of each unique element.
- Now iterate over the hash map, and return the element with count > n//2.
- Time Complexity : O(n)
- Space Complexity : O(n)


## Sorting Approach
- Now since the majority element has the count > n//2.
- That means, once the element is sorted, the majority element will always be present at index n//2, no matter what.
- Time Complexity : O(n log n), due to sorting
- Space Complexity : O(1)

## Boyer-Moore Voting Algorithm
- The key idea is that number of occurence of majority element is more than number of occurence of all other numbers combined.
- So we maintain candidate and count. 
- Iterate over the list. If the current element is candidate, we increase the count. If current element is not the candidate, we decrease the count. If the count becomes zero, we set the current element to be the candidate.
- Since the majority element occurs more than half the time, count for it will be increased more than half the time, and decreased less than half the time. Ultimately having the count positive.
- Time Complexity : O(n)
- Space Complexity : O(1)

## Randomization
- Total elements = n
- Majority elements occurs m times.
- Probability of randomly picking the majority element is `p(success) > 1/2`
- Now we pick a random number from the list, and check if it is majority element. If yes, we stop. If no, we repeat the process.
- So we repeat the process until the first success (which is picking a majority element). This is geometric distribution.
- Expectation of geometric distribution is `E[X] = 1/p`, where `p` is the probability of success.
- Since `p > 0.5`, therefore `1/p < 2` i.e. `E[X] < 2`.
- That is, the expected number of picks is less than 2.


Algorithm :
- Pick a random number from the list.
- Count how many times it occurs in the list. 
- If count > n//2, return it. If not, again repeat the process, till you get the majority element.
- Time Complexity : O(n)
- Space Complexity : O(1)

## Bit Manipulation
- The idea is to count the total number of 1 and 0 at each of 32 bit position, across all numbers.
- Now for each of 32 bit position, we check which of 0 or 1 has  count greater than n//2, we set that bit position of final result to that bit.
- Time Complexity : O(32n) ~ O(n)
- Space Complexity : O(32) ~ O(1), for bits array.
