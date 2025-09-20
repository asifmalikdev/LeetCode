class Solution():
    def exceptionQuestion(self, num):
        try:
            print(num/2)
        except:
            print("null")
        else:
            print("in else")
        finally:
            print("completed")

    def agecheck(self,age):
        if age>18:
            return "access granted"
        raise ValueError("Access Denied")
    

num = 15
obj = Solution()
obj.exceptionQuestion(num)

try:
    age = int(input("please enter your age"))
    result = obj.agecheck(age)
    print(result)
except Exception as e:
    print("Error", e)