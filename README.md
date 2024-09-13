# python_lab3

def get_peer_node(username): # function name is get_peer_node

username: This seems to be the peer's unique identifier or the username.

def join_group(node, group): # function name is join_group

node: This represents the Pyre node instance
group: The group to join

returns the node

def chat_task(ctx, pipe, n, group):  # function name is chat_task

ctx: This is a ZeroMQ Connection Context
pipe: This is a communications pipe polled by ZeroMQ for messages.
n: This is the peer to peer node my chat app is connected as
group: This is the peer chat group I wanted to join

The chat_task method does not return anything, it appears to be the send/recieve manager.

def get_channel(node, group): # function name is get_channel

node: This represents the Pyre node instance
group: The group to join

What is returned is a new thread that runs the chat_task function

