# week2-1
def rev_str(str):
    if len(str) == 1:
        return str
    else:
        # print((str[1:]) + ', ' + str[0])
        return rev_str(str[1:]) + str[0]
    
    # week2-2
def list_sum(list):
    if len(input_list) == 0:
        return 0
    return input_list.pop() + list_sum(input_list)

while True:
    input_str = input('Enter integers separated by spaces ==> ')

    if input_str == "done":
        print('program terminated. good bye !!')
        break

    input_list = input_str.split(" ")
    try: 
        for i in range(len(input_list)):
            input_list[i] = int(input_list[i])
    except:
        print("must enter integers separated by spaces")
        continue
    
    if len(input_list) == 1:
        print('must enter more than one integer')
        continue

    print('The sum of the input integers is ==> ' + str(list_sum(input_list)))

#week2-3
import re

while True:
    input_text = input("텍스트를 입력하세요: ")
    p = re.compile('[a-zA-Z0-9-_]+@[a-zA-Z0-9-.]+')
    result = p.finditer(input_text)
    
    first = 0
    for r in result:
        if first == 0:
            print('추출된 이메일 주소:')
            first = 1
        print(r.group())

    if first == 0:
        print('이메일 주소가 발견되지 않았습니다.')


#week2-4
import re
try:
    fhand = open("mbox.txt")
except:
    print("File cannot be opened")
    exit()
count = 0 
sum = 0
for line in fhand:
    line = line.rstrip()
    if re.search('New Revision:',line):
        sum += int(line.split(" ")[-1])
        count = count + 1
print("Total %d lines are matched" % count)
print("Average : " + str(sum/count))