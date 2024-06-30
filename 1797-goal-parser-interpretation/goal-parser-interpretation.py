import re
class Solution:
    def interpret(self, command: str) -> str:
        
        result = []
        for i in range(len(command)):
           
            if command[i]  == "G":
                result.append("G")
            elif command[i:i+2] == "()":
                result.append("o")
            elif command[i:i+4] == "(al)":
                result.append("al")
        return "".join(result)