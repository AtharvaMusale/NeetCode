class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position,speed), reverse = True, key = lambda x:x[0])
        stack = []
        for p,s in pairs:
            time = (target-p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)