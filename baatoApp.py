import socket_server as sender
import socket_client as receiver

def app(choice):

    ## making host to share files
    if choice == '1':
        Sender = sender.socket_server()
        Sender.send()
        return True

    ## making client to get files
    elif choice == '2':
        Receiver = receiver.socket_client()
        Receiver.recieve()
        return True

    ## invalid input
    else:
        print("Something went wrong!!")
        return False


if __name__ == '__main__':

    flag = True

    while flag:
        mainMenu = '''\t\t*** Menu ***
        \t1. Send Files!
        \t2. Receive Files!
        '''

        print(mainMenu)
        ch = input("Enter your choice: ")
         
        flag = app(ch)

    print("\nThanks for using Baato!!\n")