"""This function calculatest the Greatest Common Denominator of two integers
 - In thefirst step devide 'a' with 'b'. If the result is 0 the answer is b. If not the value of 'a'
   will be equal to 'b' and the value of 'b' will be equal to the reminder."""

class GCDCalc:

    # Define the entry point for main script
    def __init__(self, a, b):
        self.b = int(b)
        self.a = int(a)

    def execute(self):
        output = self.calculation()
        return output

    # Calculation
    def calculation(self):

        if (self.a % self.b) == 0:
            return self.b
        else:
            while self.a % self.b != 0:
                reminder = (self.a % self.b)
                self.a = self.b
                self.b = reminder

                result = self.b

                return result




