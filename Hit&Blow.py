import random

number = [0,1,2,3,4,5,6,7,8,9]
choice = 4
ChoiceNumber = []
loop = 1

for i in range(choice):
    ChoiceNumber.append(random.choice(number))
# print(ChoiceNumber)

while True:
    UserNumber = []
    print(str(loop) + '回目だよ！')
    keyBoardScanner = input('４桁の数字を打ってね：')

    if str.isdigit(keyBoardScanner):
        keyBoardScanner = int(keyBoardScanner)
        if keyBoardScanner < 10000:

            for i in range(choice):
                UserNumber.insert(0,keyBoardScanner % 10)
                keyBoardScanner = int(keyBoardScanner / 10)

            print(UserNumber)

            Hit = 0
            Blow = 0
            i = 0
            for i in range(choice):
                if UserNumber[i] == ChoiceNumber[i]:
                   Hit += 1
                elif UserNumber[i] != ChoiceNumber[i] and UserNumber[i] in ChoiceNumber:
                   Blow += 1

                i += 1

            print('Hitは' + str(Hit) + 'つ、Blowは' + str(Blow) + 'つ')
            if Hit == 4:
                break;
            print()
            loop += 1

        else:
            print('再度入力してください')
            print()

    else:
        print('数字を入力してください')
        print()

print('正解だよ！')

