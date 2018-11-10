# Date: December 9, 2017
# Author: Edward Tang
# Purpose: This program is designed to assign values to two Domino objects (either randomly or manually by the user) and display their arithmetic and relational comparison.
# Input: Keyboard
# Output: Screen, Console
# ===========================================================================================================================================================================

import random

# Date: November 14, 2017
# Author: Edward Tang
# Purpose: This class is intended to be used to edit (through randomization, flippin or programmer/user input)
#          domino values, and display them through text or a GUI interface. 
# Field Data:
#   value - Correlates to the combined value of the two halves of the domino
#   size - Correlates to the size of one half of the domino
#   diameter - Correlates to the diameter of one dot on the domino
#   gap - Correlates to the gap distance between each dot on the domino, and each dot from the domino's sides
#   orientation - Correlates to the angle of the domino (either horizontal or vertical)
#   faceup - Correlates to the shown face of the domino (either the blank or dotted side)
# Methods:
#   __str__() - This method is designed to return the domino's "value" field as a string.
#   getValue() - This method is designed to receive an integer value from the user, ensure it would create a valid domino and return the value.     
#   setValue() - This method is designed to receive an integer and set the domino object's "value" field to it if the value would create a valid domino. Otherwise, "value" is set to 0.
#   flip() - This method is designed to swap the "left" and "right" values of the domino object (1-5 -> 5-1).
#   setOrientation() - This method is designed to receive an orientation value and set the domino object's "orientation" field to it if it is either "horizontal" or "vertical" (defaults to "horizontal").    
#   setSize() - This method is designed to receive a size value and set the domino object's "size", "diameter" and "gap" fields based on it if it is between 30 and 100 (default 30).   
#   setFace() - This method is designed to receive a faceup value and set the domino object's "faceup" field to it if it is a boolean (default True)
#   randomize() - This method is designed to set the domino object's "value" field to a random valid value.
#   drawDots() - This method is designed to receive a num value and create an array of dot positions based on it.
#                It will then create the dots of the domino object based on X and Y parameters and the domino
#                object's "diameter" and "gap" fields.
#   draw() - This method is designed to display the two halves of the domino object, drawing the dots on them if
#            the object's "faceup" field is True or colouring them gray if the object's "faceup" value is False.
#   drawDominoVariations() - This method is designed to delete all shapes in the Canvas widget and display the domino object,
#                            its flipped version, its vertical version and its facedown version.
#   getValidInteger() - This method is designed to ask the user for an integer and perform checks to make sure the integer is within a certain range.  
#   orderAscending() - This method is designed to return the the Domino object value arranged to be ascending.
#   __add__() - This method is designed to return the sum of the Domino object value and a second Domino object value, both ascending.
#   __sub__() - This method is designed to return the difference of the Domino object value and a second Domino object value, both ascending.
#   __mul__() - This method is designed to return the product of the Domino object value and a second Domino object value, both ascending.
#   __gt__() - This method is designed to determine whether or not the Domino object value is greater than a second Domino object's value, with both values ascending.        
#   __lt__() - This method is designed to determine whether or not the Domino object value is less than a second Domino object's value, with both values ascending.
#   __ge__() - This method is designed to determine whether or not the Domino object value is greater than or equal to a second Domino object's value, with both values ascending.
#   __le__() - This method is designed to determine whether or not the Domino object value is less than or equal to a second Domino object's value, with both values ascending.
#   __eq__() - This method is designed to determine whether or not the Domino object value is equal to a second Domino object's value, with both values ascending.
#   __ne__() - This method is designed to determine whether or not the Domino object value is unequal to a second Domino object's value, with both values ascending. 
# =============================================================================================================================================================================================================

class Domino:
    def __init__(self,value=random.randint(0,66),size=30,orientation="horizontal",faceup=True):
        while value%10 > 6 or value//10 > 6:
            value = random.randint(0,66)
        self.value = value
        if size < 30 or size > 100:
            self.size = 30
        else:
            self.size = size
        self.diameter = self.size / 5
        self.gap = self.diameter / 2
        if orientation != "horizontal" and orientation != "vertical":
            self.orientation = "horizontal"
        else:
            self.orientation = orientation
        if faceup != True and faceup != False:
            faceup = True
        else:
            self.faceup = faceup

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the domino's "value" field as a string.
    # Input: N/A
    # Output: [STRING] The domino's value
    # ===================================================================================

    def __str__(self):
        return str(self.value)

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to receive an integer value from the user, ensure it 
    #          would create a valid domino and return the value.
    # Input: Keyboard
    # Output: Console/Screen, [INTEGER] A valid value for the domino
    # ===============================================================================================
    
    def getValue(self):
        tempValue = self.getValidInteger("Enter the value of the domino","0","66")
        while tempValue%10 > 6 or tempValue//10 > 6:
            print("Neither digit can be greater than 6! Please try again.")
            print()
            tempValue  = self.getValidInteger("Enter the value of the domino","0","66")
        return tempValue

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to receive an integer and set the domino object's "value" field to 
    #          it if the value would create a valid domino. Otherwise, "value" is set to 0.
    # Input: [INTEGER] A number value
    # Output: Console/Screen
    # ============================================================================================================

    def setValue(self,num):
        if num%10 <= 6 and num//10 <= 6:
            self.value = num
        else:
            self.value = 0

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to swap the "left" and "right" values of the domino object (1-5 -> 5-1).
    # Input: N/A
    # Output: N/A
    # ==========================================================================================================

    def flip(self):
        self.value = self.value % 10 * 10 + self.value // 10
            
    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to receive an orientation value and set the domino object's "orientation"
    #          field to it if it is either "horizontal" or "vertical" (defaults to "horizontal").
    # Input: [STRING] Orientation value
    # Output: Console/Screen
    # ===========================================================================================================

    def setOrientation(self,value="horizontal"):
        if value == "horizontal" or value == "vertical":
            self.orientation = value
        else:
            self.orientation = "horizontal"

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to receive a size value and set the domino object's "size", "diameter" and
    #          "gap" fields based on it if it is between 30 and 100 (default 30).
    # Input: [INTEGER] Size value
    # Output: Console/Screen
    # ============================================================================================================

    def setSize(self,value=30):
        if value >= 30 and value <= 100:
            self.size = value
        else:
            self.size = 30
        self.diameter = self.size / 5
        self.gap = self.diameter / 2

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to receive a faceup value and set the domino object's "faceup" field to it
    #          if it is a boolean (default True)
    # Input: [BOOLEAN] Faceup value
    # Output: Console/Screen
    # ============================================================================================================

    def setFace(self,value=True):
        if value == True or value == False:
            self.faceup = value
        else:
            self.faceup = True

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to set the domino object's "value" field to a random valid value.
    # Input: N/A
    # Output: N/A
    # ============================================================================================================

    def randomize(self):
        self.value = random.randint(0,66)
        while self.value%10 > 6 or self.value//10 > 6:
            self.value = random.randint(0,66)

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to receive a num value and create an array of dot positions based on it.
    #          It will then create the dots of the domino object based on X and Y parameters and the domino
    #           object's "diameter" and "gap" fields.
    # Input: [INTEGER] Num, X and Y values
    # Output: Screen (GUI), console
    # References: Canvas widget
    # ===========================================================================================================

    def drawDots(self,num,x,y,canvas):
        if num >= 0 and num <= 6:
            dotNums = []
            if num == 1:
                dotNums = [5]
            elif num == 2 and self.orientation == "horizontal":
                dotNums = [1,9]
            elif num == 2 and self.orientation == "vertical":
                dotNums = [3,7]
            elif num == 3 and self.orientation == "horizontal":
                dotNums = [1,5,9]
            elif num == 3 and self.orientation == "vertical":
                dotNums = [3,5,7]
            elif num == 4:
                dotNums = [1,3,7,9]
            elif num == 5:
                dotNums = [1,3,5,7,9]
            elif num == 6 and self.orientation == "horizontal":
                dotNums = [1,2,3,7,8,9]
            elif num == 6 and self.orientation == "vertical":
                dotNums = [1,4,7,3,6,9]
            elif num == 7 and self.orientation == "horizontal":
                dotNums = [1,2,3,5,7,8,9]
            elif num == 7 and self.orientation == "vertical":
                dotNums = [1,4,7,5,3,6,9]
            elif num == 8:
                dotNums = [1,2,3,4,6,7,8,9]
            elif num == 9:
                dotNums = [1,2,3,4,5,6,7,8,9]
            position1 = self.gap
            position2 = self.gap*2 + self.diameter
            position3 = self.gap*3 + self.diameter*2
            if 1 in dotNums:
                canvas.create_oval(x+position1,y+position1,x+position1+self.diameter,y+position1+self.diameter,fill="black")
            if 2 in dotNums:
                canvas.create_oval(x+position2,y+position1,x+position2+self.diameter,y+position1+self.diameter,fill="black")
            if 3 in dotNums:
                canvas.create_oval(x+position3,y+position1,x+position3+self.diameter,y+position1+self.diameter,fill="black")
            if 4 in dotNums:
                canvas.create_oval(x+position1,y+position2,x+position1+self.diameter,y+position2+self.diameter,fill="black")
            if 5 in dotNums:
                canvas.create_oval(x+position2,y+position2,x+position2+self.diameter,y+position2+self.diameter,fill="black")
            if 6 in dotNums:
                canvas.create_oval(x+position3,y+position2,x+position3+self.diameter,y+position2+self.diameter,fill="black")
            if 7 in dotNums:
                canvas.create_oval(x+position1,y+position3,x+position1+self.diameter,y+position3+self.diameter,fill="black")
            if 8 in dotNums:
                canvas.create_oval(x+position2,y+position3,x+position2+self.diameter,y+position3+self.diameter,fill="black")
            if 9 in dotNums:
                canvas.create_oval(x+position3,y+position3,x+position3+self.diameter,y+position3+self.diameter,fill="black")

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to display the two halves of the domino object, drawing the dots on them if
    #          the object's "faceup" field is True or colouring them gray if the object's "faceup" value is False.
    # Input: [INTEGER] X and Y values
    # Output: Screen (GUI)
    # References: Canvas widget
    # ================================================================================================================

    def draw(self,x,y,canvas):
        if self.faceup == True:
            dominoA = canvas.create_rectangle(x,y,x+self.size,y+self.size,fill="white")
            self.drawDots(self.value//10,x,y,canvas)
            if self.orientation == "horizontal":
                dominoB = canvas.create_rectangle(x+self.size,y,x+self.size*2,y+self.size,fill="white")
                self.drawDots(self.value%10,x+self.size,y,canvas)
            else:
                dominoB = canvas.create_rectangle(x,y+self.size,x+self.size,y+self.size*2,fill="white")
                self.drawDots(self.value%10,x,y+self.size,canvas)
        else:
            if self.orientation == "horizontal":
                dominoA = canvas.create_rectangle(x,y,x+self.size*2,y+self.size,fill="#e0e0e0")
            else:
                dominoA = canvas.create_rectangle(x,y,x+self.size,y+self.size*2,fill="#e0e0e0")

    # Date: November 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to delete all shapes in the Canvas widget and display the domino object,
    #          its flipped version, its vertical version and its facedown version.
    # Output: Screen (GUI)
    # References: Canvas widget
    # ==========================================================================================================

    def drawDominoVariations(self,canvas):
        canvas.delete(ALL)
        self.setSize(sliderSize.get())
        self.setFace(True)
        self.orientation = "horizontal"
        self.draw(10,10,canvas)
        self.flip()
        self.draw(dom.size*2 + 30,10,canvas)
        self.flip()
        self.orientation = "vertical"
        self.draw(dom.size*4 + 50,10,canvas)
        self.setFace(False)
        self.draw(dom.size*5 + 70,10,canvas)

    # Date: November 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to ask the user for an integer and perform checks to make sure the integer
    #          is within a certain range.
    # Input: Keyboard, [STRING] The input prompt phrase, [INTEGER] the lowest possible value and the highest 
    #        possible value
    # Output: Console/Screen, [INTEGER] The user-inputted number
    # ============================================================================================================= 

    def getValidInteger(self, prompt="Enter an integer", low = "", high = ""):
        if low.isdigit() and high.isdigit():
            low = int(low)
            high = int(high)
            intUserInput = low - 1
            while intUserInput < low or intUserInput > high:
                strUserInput = ""
                while not strUserInput.isdigit():
                    strUserInput = input(prompt + " between " + str(low) + " and " + str(high) + ": ")
                    print()
                    if not strUserInput.isdigit():
                        print("[ERROR] You did not enter a valid integer! Please try again.")
                        print()
                intUserInput = int(strUserInput)
                if intUserInput < low or intUserInput > high:
                    print("[ERROR] You did not enter an integer between " + str(low) + " and " + str(high) + ". Please try again.")
                    print()
            return intUserInput
        elif low.isdigit() and not high.isdigit():
            low = int(low)
            intUserInput = low - 1
            while intUserInput < low:
                strUserInput = ""
                while not strUserInput.isdigit():
                    strUserInput = input(prompt + " of at least " + str(low) + ": ")
                    print()
                    if not strUserInput.isdigit():
                        print("[ERROR] You did not enter a valid integer! Please try again.")
                        print()
                intUserInput = int(strUserInput)
                if intUserInput < low:
                    print("[ERROR] You did not enter an integer of at least " + str(low) + ". Please try again.")
                    print()
            return intUserInput

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the the Domino object value arranged to be ascending.
    # Input: N/A
    # Output: [INTEGER] A value for the Domino Object   
    # ================================================================================================================================

    def orderAscending(self):
        value = self.value
        if self.value//10 > self.value%10:
            value = self.value%10*10 + self.value//10
        return value

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the sum of the Domino object value and a second Domino object value, both ascending.
    # Input: A second Domino object name
    # Output: [INTEGER] The sum of the two Domino object values
    # ================================================================================================================================

    def __add__(self,secondObject):
        return self.orderAscending() + secondObject.orderAscending()

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the difference of the Domino object value and a second Domino object value, both ascending.
    # Input: A second Domino object name
    # Output: [INTEGER] The difference of the two Domino object values
    # =======================================================================================================================================

    def __sub__(self,secondObject):
        return self.orderAscending() - secondObject.orderAscending()

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the product of the Domino object value and a second Domino object value, both ascending.
    # Input: A second Domino object name
    # Output: [INTEGER] The product of the two Domino object values
    # ====================================================================================================================================

    def __mul__(self,secondObject):
        return self.orderAscending() * secondObject.orderAscending()

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the Domino object value is greater than a
    #          second Domino object's value, with both values ascending.
    # Input: A second Domino object name
    # Output: [BOOLEAN] True or False depending on whether or not the Domino object's value is greater than
    #         that of the second
    # ================================================================================================================================

    def __gt__(self,secondObject):
        isGreater = False
        if self.orderAscending() > secondObject.orderAscending():
            isGreater = True
        return isGreater

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the Domino object value is less than a
    #          second Domino object's value, with both values ascending.
    # Input: A second Domino object name
    # Output: [BOOLEAN] True or False depending on whether or not the Domino object's value is less than
    #         that of the second
    # =====================================================================================================

    def __lt__(self,secondObject):
        isLesser = False
        if self.orderAscending()< secondObject.orderAscending():
            isLesser = True
        return isLesser

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the Domino object value is greater than or
    #          equal to a second Domino object's value, with both values ascending.
    # Input: A second Domino object name
    # Output: [BOOLEAN] True or False depending on whether or not the Domino object's value is greater than
    #         or equal to that of the second
    # =========================================================================================================

    def __ge__(self,secondObject):
        isGreaterOrEqual = False
        if self.orderAscending()>= secondObject.orderAscending():
            isGreaterOrEqual = True
        return isGreaterOrEqual

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the Domino object value is less than or
    #          equal to a second Domino object's value, with both values ascending.
    # Input: A second Domino object name
    # Output: [BOOLEAN] True or False depending on whether or not the Domino object's value is less than
    #         or equal to that of the second
    # =========================================================================================================

    def __le__(self,secondObject):
        isLesserOrEqual = False
        if self.orderAscending() <= secondObject.orderAscending():
            isLesserOrEqual = True
        return isLesserOrEqual

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the Domino object value is equal to 
    #          a second Domino object's value, with both values ascending.
    # Input: A second Domino object name
    # Output: [BOOLEAN] True or False depending on whether or not the Domino object's value is equal to
    #         that of the second
    # ==================================================================================================

    def __eq__(self,secondObject):
        isEqual = False
        if self.orderAscending() == secondObject.orderAscending():
            isEqual = True
        return isEqual

    # Date: December 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the Domino object value is unequal to 
    #          a second Domino object's value, with both values ascending.
    # Input: A second Domino object name
    # Output: [BOOLEAN] True or False depending on whether or not the Domino object's value is unequal to
    #         that of the second
    # ====================================================================================================

    def __ne__(self,secondObject):
        notEqual = False
        if self.orderAscending() != secondObject.orderAscending():
            notEqual = True
        return notEqual

# MAIN CODE

restart = ""
dom1 = Domino()
dom2 = Domino()

while restart != "stop":
    inputMethod = input("Enter any key to manually enter domino values, or enter 'random' to randomize them: ")
    print()
    if inputMethod == "random":
        dom1.randomize()
        dom2.randomize()
    else:
        print("========== Enter the first domino's value below ==========")
        print()
        dom1.setValue(dom1.getValue())
        print()
        print("========== Enter the second domino's value below ==========")
        print()
        dom2.setValue(dom2.getValue())
        print()
    print("Domino 1:",dom1)
    print("Domino 2:",dom2)
    print()
    print("The comparison will use the domino values arranged to be ascending (e.g. 21 becomes 12).")
    print()
    print("Domino 1:",dom1.orderAscending())
    print("Domino 2:",dom2.orderAscending())
    print()
    print("========== Domino Value Comparison ==========")
    print()
    print("Addition:",dom1+dom2)
    print("Subtraction:",dom1-dom2)
    print("Multiplication:",dom1*dom2)
    print("[First Domino] >  [Second Domino]:",dom1>dom2)
    print("[First Domino] <  [Second Domino]:",dom1<dom2)
    print("[First Domino] >= [Second Domino]:",dom1>=dom2)
    print("[First Domino] <= [Second Domino]:",dom1<=dom2)
    print("[First Domino] == [Second Domino]:",dom1==dom2)
    print("[First Domino] != [Second Domino]:",dom1!=dom2)
    print()
    restart = input("Enter any key to restart the program, or enter 'stop' to end it: ")
    print()
    if restart != "stop":
        print("====================================================================================================")
        print()
