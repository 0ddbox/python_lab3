# libraries
import lab_chat as lc


# functions
def get_username():
    username = input("Enter your username: ")
    cleaned_username = username.strip().upper()
    return cleaned_username


def get_group():
    group = input("Group name: ")
    cleaned_group = group.strip().upper()
    return cleaned_group


def get_message():
    message = input("Message: \n")
    cleaned_message = message.strip().upper()
    return cleaned_message


def init_chat():
    username = get_username()
    group_name = get_group()

    node = lc.get_peer_node(username)
    lc.join_group(node, group_name)

    chat_channel = lc.get_channel(node, group_name)

    return chat_channel


def start_chat():
    channel = init_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")