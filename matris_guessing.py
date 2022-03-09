import numpy as np
#entry guide function
def entryguide():
    print(""""
    ******************************************
    **Enter 'what should i learn' to learn  **
    **What you need at the moment.          **
    **-When you learn everything,and        **
    **know every secret, you get the key.   **
    **    ----------------------            **
    **        ASKABLE QUESTIONS             **
    **-Greatest Element                     **
    **-
    ******************************************""")
#requirements_calculation
element_list = np.random.rand(4)
mtrx = element_list.reshape(2,2)
first_element = mtrx[0,0]
#feg founds - checks if the element is found or not.
feg1_found = 0
feg2_found = 0
feg3_found = 0
feg4_found = 0
# element placement
second_element = mtrx[0,1]
third_element = mtrx[1,0]
fourth_element = mtrx[1,1]
print(first_element,second_element,third_element,fourth_element)
     #sum of two
sot1 = np.random.randint(1,3)
sumoftwo  = first_element + element_list[sot1]
    #determinant
mtrx_det = np.linalg.det(mtrx)
mtrx_det = round(mtrx_det)
print(mtrx)
print(f"Welcome,Sir.Your first element is: {first_element}")
    #score
score = 25
#general app loop
while True:
    # line count for score calculating
    linecount = 0
    general_process = str(input("""
The room's key only reachable if you can solve the test.type 'guide' for guide.
Type Here:"""))
    #guide
    if general_process.lower() == "guide":
        entryguide()
        #maximum element
    elif general_process.lower() == "greatest element" or general_process.lower() == "max element":
        print(mtrx.max())
        score -= 6
        #minimum element
    elif general_process.lower() == "lowest element" or general_process.lower() == "low":
        print(mtrx.min())
        score -= 6
        #determinant
    elif general_process.lower() == "determinant" or general_process.lower() == "det":
        print(mtrx_det)
        score -= 1
        #sum of all matrix elements
    elif general_process.lower() == "sum of all matrix" or general_process.lower() == "sum matrix":
        print(mtrx.sum())
        score -= 2
        #sum of first element and a random one
    elif general_process.lower() == "sum of two" or general_process.lower() == "sum2":
        print(sumoftwo)
        score -= 5
        #mean
    elif general_process.lower() == "mean of matrix" or general_process.lower() == "mean":
        print(mtrx.mean())
        score -= 3
        #where the min element located at
    elif general_process.lower() == "lowest index" or general_process.lower() == "min index":
        print(mtrx.argmin())
        score -= 1
        #where the max element located at
    elif general_process.lower() == "greatest index" or general_process.lower() == "max index":
        print(mtrx.argmax())
        score -= 1
        #guessing operations
    elif general_process.lower() == "guess":
        #first element
        if feg1_found == 0: #if the element is found before, you don't need to guess it again- with the help of FEGs.
            first_element_g = float(input("First Element:"))
            if first_element_g == first_element:
                print("First Element is true!")
                score += 1
                feg1_found = 1
            else:
                score -= 5
        #second element
        if feg2_found ==0:
            second_element_g = float(input("Second Element:"))
            if second_element_g == second_element:
                print("Second Element is true!")
                score += 2
                feg2_found = 1
            else:
                score -= 1
        #third element
        if feg3_found == 0:
            third_element_g = float(input("Third Element:"))
            if third_element_g == third_element:
                print("Third Element is true!")
                score += 2
                feg3_found = 1
            else:
                score -= 1
        #fourth element
        if feg4_found == 0:
            fourth_element_g = float(input("Fourth Element:"))
            if fourth_element_g == fourth_element:
                print("Fourth Element is true!")
                score += 2
                feg4_found = 1
            else:
                score -= 1
        #score operations
    elif general_process.lower() == "score":
        print(f"""
********************************
Current Score Is: {score}
If you'd like to see your last 
10 scores, please type score10.""")
        #prints last 10 scores
    elif general_process.lower() == "score10":
       fileread = open("mtrx_scores","r")
       for line in fileread:
           if linecount == 10:
               break
           print(line)
           linecount += 1

      
    #quits from the app
    elif general_process.lower() == "quit":
        print("See you again!")
        break
        #end of guessing. if all of the elements are found.Calculates the total score and saves it to the mtrx_scores.
    if feg1_found == 1 and feg2_found == 1 and feg3_found == 1 and feg4_found == 1:
        print(f"""
*************************************************
Congrats! You finished  and passed the guess!
Your Score is: {score}""")
        file = open("mtrx_scores","a")
        file.write(str(score))
        file.close()







