# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         pair = [(p,s) for p,s in zip(position,speed)]
#         pair.sort(reverse = True)
#         stack = []
#         for p,s in pair:
#             stack.append((target-p)/s)
#             if len(stack)>=2 and stack[-1]<=stack[-2]:
#                 stack.pop()
#         return len(stack)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create list of (position, speed) pairs and sort descending by position
        pairs = sorted(zip(position, speed), reverse=True, key=lambda x: x[0])
        
        # Initialize the stack to hold times needed for each car to reach the target
        stack = []
        
        # Calculate time for each car to reach the target
        for p, s in pairs:
            time = (target - p) / s
            # Only add time to stack if it does not form a fleet with the car before it
            if not stack or time > stack[-1]:
                stack.append(time)
        
        # The size of the stack is the number of car fleets
        return len(stack)
