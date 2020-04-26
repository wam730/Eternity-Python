from random import randint as r
while True:
    min = input('Input the min-number:')
    max = input('Input thr max-number:')
    time = input('How many times you what to guess:')
    try:
        min = int(min)
        max = int(max)
        time = int(time)
        assert(min < max)
        assert(time <= 1+int(max)-int(min))
    except:
        print("Your Enter is error. Please check the number you entered")
    else:
        def guess(minValue,maxValue,times):
            answer = r(minValue,maxValue)
            for i in range(times):
                prompt = '\nStart to guess:' if i == 0 else 'Guess again:'
                try:
                    x = int(input(prompt))
                except:
                    print('The number you entered must is a integer between {0} and {1}'.format(minValue,maxValue))
                else:
                    if x == answer:
                        print('\nComgratulations! You win!')
                        break
                    elif x > answer:
                        print('\n{0} is Too big'.format(x))
                    else:
                        print('\n{0} is Too little'.format(x))
            else:
                print('\nGame over . You fail .')
                print('\nThe answer is {0}'.format(answer))
        guess(min,max,time)
        break