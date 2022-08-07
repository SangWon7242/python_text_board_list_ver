# 리스트를 이용해 데이터를 관리하는 프로그램을 만들어보겠습니다.
# input() 함수를 이용해 입력값을 받습니다. 입력값을 받을 때는 '명령어를 입력해주세요 : '라고 출력문이 나오도록 합니다.
# 입력값에 delete를 입력하면 아래와 같이 출력되도록 해주세요.

'''
명령어를 입력해주세요 : delete

['hello', 'bye']
삭제 대상을 선택하세요 : 0
hello 값이 삭제되었습니다.

* 만약1 해당하지 않는 인덱스를 입력하면 '올바른 값을 입력해주세요' 출력하고 다시 진행

* 만약2 add, read, update, delete, exit 말고 다른 값을 입력하면 '올바른 명령어를 입력해주세요 출력'
'''

data_store = []

while True:
    cmd = input("명령어를 입력해주세요 : ")
    # print("입력받은 명령어 : {}".format(cmd))

    if cmd == "help":
        print("add : 데이터 추가")
        print("read : 데이터 조회")
        print("update : 데이터 수정")
        print("delete : 데이터 삭제")

    elif cmd == "add":
        input_data = input("저장할 값을 입력해주세요 : ")
        print("{} 이/가 저장되었습니다.".format(input_data))
        data_store.append(input_data)

    elif cmd == "read":
        if len(data_store) == 0:
            print("현재 저장되어 있는 데이터가 없습니다.")
            continue

        print("현재 저장되어 있는 값 : {}".format(data_store))

    elif cmd == "update":
        last_data_index = len(data_store) - 1

        if len(data_store) == 0:
            print("현재 저장되어 있는 데이터가 없습니다.")
            continue

        print(data_store)
        input_index = int(input("수정 대상을 선택하세요 : "))

        if input_index > last_data_index:
            print("{} 이하로 입력해주세요.".format(last_data_index))
            continue

        input_update_data = input("어떤 값으로 수정할까요 : ")
        data_store[input_index] = input_update_data
        print("{} 로 값이 수정되었습니다.".format(input_update_data))

    elif cmd == "delete":
        last_data_index = len(data_store) - 1

        if len(data_store) == 0:
            print("현재 저장되어 있는 데이터가 없습니다.")
            continue

        print(data_store)
        input_index = int(input("삭제 대상을 선택하세요 : "))

        if input_index > last_data_index:
            print("{} 이하로 입력해주세요.".format(last_data_index))
            continue

        print("{} 값이 삭제되었습니다.".format(data_store[input_index]))
        del data_store[input_index]

    elif cmd == "exit":
        print("프로그램이 종료 되었습니다.")
        break
    else:
        print("올바른 명령어 아닙니다.")
