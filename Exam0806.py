# 입력 받은 데이터 저장소
data_store = []


# 데이터 유무 확인
def data_is_empty():
    if not data_store:
        print("현재 저장되어 있는 데이터가 없습니다.")
        return False

    return True

    '''
    # 위 코드랑 완벽하게 같다.
    # not의 경우 데이터가 없으면 True, 있으면 False를 반환
    if len(data_store) == 0:
        print("현재 저장되어 있는 데이터가 없습니다.")
        return False
        
    return True
    '''


# 데이터 index 길이 구하고, 잘못 입력시 'n 이하로 입력해주세요' 명령
def data_index_checked(input_index):
    last_data_index = len(data_store) - 1

    if input_index > last_data_index:
        print("{} 이하로 입력해주세요.".format(last_data_index))
        return


# 도움말
def help_list():
    print("add : 데이터 추가")
    print("read : 데이터 조회")
    print("update : 데이터 수정")
    print("delete : 데이터 삭제")


# 데이터 추가
def do_add():
    input_data = input("저장할 값을 입력해주세요 : ")
    print("{} 이/가 저장되었습니다.".format(input_data))
    data_store.append(input_data)


# 입력 된 게시물 리스트
def show_list():
    if data_is_empty() == True:
        print("현재 저장되어 있는 값 : {}".format(data_store))


# 게시물 수정
def do_update():
    if data_is_empty() == False:
        return

    print(data_store)
    input_index = int(input("수정 대상을 선택하세요 : "))

    data_index_checked(input_index)

    input_update_data = input("어떤 값으로 수정할까요 : ")
    data_store[input_index] = input_update_data
    print("{} 로 값이 수정되었습니다.".format(input_update_data))


# 게시물 삭제
def do_delete():
    if data_is_empty() == False:
        return

    print(data_store)
    input_index = int(input("삭제 대상을 선택하세요 : "))

    data_index_checked(input_index)

    print("{} 값이 삭제되었습니다.".format(data_store[input_index]))
    del data_store[input_index]


def App():
    cmd = input("명령어를 입력해주세요 : ")

    if cmd == "help":
        help_list()

    elif cmd == "add":
        do_add()

    elif cmd == "read":
        show_list()

    elif cmd == "update":
        do_update()

    elif cmd == "delete":
        do_delete()

    elif cmd == "exit":
        print("프로그램이 종료 되었습니다.")
        exit()

    else:
        print("올바른 명령어 아닙니다.")


while True:
    App()
