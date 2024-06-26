class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []

        for i in range(len(height)):
            while len(stack)>0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                dis = i-stack[-1]-1
                ht = min(height[i],height[stack[-1]]) - height[top]
                ans+=dis * ht
            stack.append(i)
        
        return ans
                













        # ans =0
        # st=[]
        # for i in range(len(height)):
        #     while(len(st) > 0 and height[i] > height[st[-1]]):
        #         top = st.pop()
        #         if len(st) ==0:
        #             break
        #         dis = i-st[-1] -1
        #         ht = min(height[i], height[st[-1]]) - height[top]
        #         ans+= dis*ht
        #     st.append(i)
        # return ans
        