print('Welcome to Maths Tester Pro.\nSelect a difficulty:\n1) Easy\n2) Medium\n3) Hard')
ans=int(input())

score=0
if ans==1:
        
    liv=3
    print('Easy mode selected!')
    print('\nQuestion 1 of 5. You have {} lives remaining.'.format(liv))
    ans1=int(input('What is 5-10? '))
    if ans1== -5:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was -5.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
        
    print('\nQuestion 2 of 5. You have {} lives remaining.'.format(liv))
    ans2=int(input('What is 5-3? '))
    if ans2== 2:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 2.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    print('\nQuestion 3 of 5. You have {} lives remaining.'.format(liv))
    ans3=int(input('What is 3+6? '))
    if ans3== 9:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 9.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    print('\nQuestion 4 of 5. You have {} lives remaining.'.format(liv))
    ans4=int(input('What is 4-10? '))
    if ans4== -6:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was -6.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    print('\nQuestion 5 of 5. You have {} lives remaining.'.format(liv))
    ans5=int(input('What is 12-11? '))
    if ans5== 1:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 1.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()

    per=(score/5)*100
    print('\nTest complete.')
    print('You scored {}/5 ({}%).'.format(score,per))
    print('You passed!')




elif ans==2:
    liv=2
    print('Medium mode selected!')
    print('\nQuestion 1 of 5. You have {} lives remaining.'.format(liv))

        
    ans1=int(input('What is 65-19? '))
    if ans1== 46:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 46.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
        
    print('\nQuestion 2 of 5. You have {} lives remaining.'.format(liv))
    ans2=int(input('What is 55-31? '))
    if ans2== 24:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 24.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    print('\nQuestion 3 of 5. You have {} lives remaining.'.format(liv))
    ans3=int(input('What is 33-68? '))
    if ans3== -35:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was -35.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    print('\nQuestion 4 of 5. You have {} lives remaining.'.format(liv))
    ans4=int(input('What is 224+144? '))
    if ans4== 368:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 368.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    print('\nQuestion 5 of 5. You have {} lives remaining.'.format(liv))
    ans5=int(input('What is 1245-1168? '))
    if ans5== 77:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 77.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    per=(score/5)*100
    print('\nTest complete.')
    print('You scored {}/5 ({}%).'.format(score,per))
    print('You passed!')



        
else:
    liv=1
    print('Hard mode selected!')

    print('\nQuestion 1 of 5. You have {} lives remaining.'.format(liv))

        
    ans1=int(input('What is the square of 8? '))
    if ans1== 64:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 64.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
        
    print('\nQuestion 2 of 5. You have {} lives remaining.'.format(liv))
    ans2=int(input('What is 55X31? '))
    if ans2==1705:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 1705.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    print('\nQuestion 3 of 5. You have {} lives remaining.'.format(liv))
    ans3=int(input('What is 340/68? '))
    if ans3== 5:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 5.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    print('\nQuestion 4 of 5. You have {} lives remaining.'.format(liv))
    ans4=int(input('What is 224+144-12? '))
    if ans4== 356:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 356.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            
    print('\nQuestion 5 of 5. You have {} lives remaining.'.format(liv))
    ans5=int(input('What is 125^2? '))
    if ans5== 15625:
        print('Correct!')
        score=score+1
    else:
        print('Incorrect! The correct answer was 15625.')
        liv=liv-1

        if liv==0:
            print('\nOut of lives. Game Over!')
            quit()
            

    per=(score/5)*100
    print('\nTest complete.')
    print('You scored {}/5 ({}%).'.format(score,per))
    print('You passed!')

        
