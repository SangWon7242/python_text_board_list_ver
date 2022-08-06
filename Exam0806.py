# 리스트를 이용해 데이터를 관리하는 프로그램을 만들어보겠습니다.
# 입력값에 read를 입력하면 아래처럼 나오게 해주세요.

'''
명령어를 입력해주세요: read

현재 저장되어 있는 값 : [저장된 값들]

만약 add, read, exit 말고 다른 값을 입력하면 '올바른 명령어를 입력해주세요 출력'
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

    elif cmd == "exit":
        print("프로그램이 종료 되었습니다.")
        break
    else:
        print("올바른 명령어 아닙니다.")
