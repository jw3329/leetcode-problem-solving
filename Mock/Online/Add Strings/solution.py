    def addStrings(self, num1: str, num2: str) -> str:
        return self.add(num1,num2,False)
        
    def add(self,num1,num2,carry_on):
        if carry_on:
            return self.add(num1,self.add(num2,'1',False),False)
        if not num1: return num2
        if not num2: return num1
        
        last_num1 = int(num1[-1])
        last_num2 = int(num2[-1])
        carry_on = False
        if last_num1 + last_num2 >= 10:
            carry_on = True
        return self.add(num1[:-1],num2[:-1],carry_on) + str((last_num1 + last_num2) % 10)

