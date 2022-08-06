# 리스트를 이용해 데이터를 관리하는 프로그램을 만들어보겠습니다.
# 입력값에 help를 입력하면 아래처럼 나오게 해주세요.
# 명령어를 입력해주세요: 는 exit를 치기 전까지 계속 나와야 합니다.

'''
(입출력 예시)

명령어를 입력해주세요: help

add : 데이터 추가
read : 데이터 조회
update : 데이터 수정
delete : 데이터 삭제

명령어를 입력해주세요:
'''

while True:
    cmd = input("명령어를 입력해주세요 : ")
    # print("입력받은 명령어 : {}".format(cmd))

    if cmd == "help":
        print("add : 데이터 추가")
        print("read : 데이터 조회")
        print("update : 데이터 수정")
        print("delete : 데이터 삭제")

    elif cmd == "exit":
        print("프로그램이 종료 되었습니다.")
        break
