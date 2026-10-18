## Brute Force
- The idea in brute force is to explore all the possible path to the end index. It will use recursion.
- There can be two ways :
    1. Pure brute force
    2. Brute force with memoization for optimization
    
### Pure Brute Force
Algorithm :
CAN-JUMP(nums):
- return reachGoal(0, nums)

reachGoal(i, nums):
- if i > = len(nums) - 1
-   return True
- curr_value = nums[i]
- while curr_value > 0:
    - result = reachGoal(i+curr_value, nums)
    - if result == True:
        - return True
    - else:
        = curr_value -= 1
- return False

### Brute Force with Memoization
Algorithm :
CAN-JUMP(nums):
- memo = [None] * len(nums)
- return reachGoal(0, nums, memo)

reachGoal(i, nums, memo):
- if i > = len(nums) - 1
    - memo[-1] = True
    - return True
- curr_value = nums[i]
- while curr_value > 0:
    - if memo[i+curr_value] == True:
        - memo[i] = True
        - return True
    - result = reachGoal(i+curr_value, nums, memo)
    - if result == True:
        - memo[i] = True
        - return True
    - else:
        - curr_value -= 1
- memo[i] = False
- return False
