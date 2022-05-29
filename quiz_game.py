

def quiz_game():
    
    score = 0
    q1 = input('What is the full form of CPU : ')
    if q1.lower() == 'control processing unit':
        print('CORRECT! ')
        score +=  1
    else:
        print("Incorrect input!\nCPU stands for Control processing unit ")
        pass

    q2 = input('What is the full form of RAM : ')
    if q2.lower() == 'random access memory':
        print("CORRECT! ")
        score += 1
    else: 
        print("Incorrect input!\nRAM stands for Random access memory")
        pass

    q3 = input('What is the full form of GPU : ')
    if q3.lower() == 'graphical processing unit':
            print("CORRECT!")
            score += 1
    else:
            print('Incorrect Input!\nGPU stands for Graphical processing unit')
            pass

    q4 = input("What is the full form of GUI : ")
    if q4.lower() == 'graphical user interface':
            print("CORRECT!")
            score += 1
    else:
            print("GUI stands for Graphical user interface")
            pass
    q5 = input('What is the full form form of Wi-Fi : ')
    if q5.lower() == 'wireless fidelity':
            print("CORRECT!")
            score += 1
    else:
        print('Wi-Fi stands for Wireless Fidelity')
        pass

    print("Your score out of 5 : "+ str(score))    

quiz_game()