# 리스트를 이용해 데이터를 관리하는 프로그램을 만들어보겠습니다.
# 입력값에 add를 입력하면 아래처럼 나오게 해주세요.

'''
(입출력 예시)

명령어를 입력해주세요 : add

저장할 값을 입력해주세요 : hello
hello 이/가 저장되었습니다.
(실제 리스트에 추가 한 데이터가 저장 되어야 합니다.)

만약 add, exit 말고 다른 값을 입력하면 '올바른 명령어를 입력해주세요' 출력
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

    elif cmd == "exit":
        print("프로그램이 종료 되었습니다.")
        break
    else:
        print("올바른 명령어 아닙니다.")
