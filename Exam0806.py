def help_list():
    print("add : 데이터 추가")
    print("read : 데이터 조회")
    print("update : 데이터 수정")
    print("delete : 데이터 삭제")


def do_add():
    input_data = input("저장할 값을 입력해주세요 : ")
    print("{} 이/가 저장되었습니다.".format(input_data))
    data_store.append(input_data)


def show_list():
    if len(data_store) == 0:
        print("현재 저장되어 있는 데이터가 없습니다.")
        return

    print("현재 저장되어 있는 값 : {}".format(data_store))


def do_update():
    last_data_index = len(data_store) - 1

    if len(data_store) == 0:
        print("현재 저장되어 있는 데이터가 없습니다.")
        return

    print(data_store)
    input_index = int(input("수정 대상을 선택하세요 : "))

    if input_index > last_data_index:
        print("{} 이하로 입력해주세요.".format(last_data_index))
        return

    input_update_data = input("어떤 값으로 수정할까요 : ")
    data_store[input_index] = input_update_data
    print("{} 로 값이 수정되었습니다.".format(input_update_data))


def do_delete():
    last_data_index = len(data_store) - 1

    if len(data_store) == 0:
        print("현재 저장되어 있는 데이터가 없습니다.")
        return

    print(data_store)
    input_index = int(input("삭제 대상을 선택하세요 : "))

    if input_index > last_data_index:
        print("{} 이하로 입력해주세요.".format(last_data_index))
        return

    print("{} 값이 삭제되었습니다.".format(data_store[input_index]))
    del data_store[input_index]


data_store = []

while True:
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
        break
    else:
        print("올바른 명령어 아닙니다.")
