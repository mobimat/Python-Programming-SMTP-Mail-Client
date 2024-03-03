from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1', from_address='your-email@example.com', to_address='recipient-email@example.com'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')
    #    return

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    #    return

    # Send MAIL FROM command and handle server response.
    mailFrom = f"MAIL FROM: <{from_address}>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != '250':
    #    print('250 reply not received from server after MAIL FROM command.')
    #    return

    # Send RCPT TO command and handle server response.
    rcptTo = f"RCPT TO: <{to_address}>\r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
    #    print('250 reply not received from server after RCPT TO command.')
    #    return

    # Send DATA command and handle server response.
    dataCommand = "DATA\r\n"
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '354':
    #    print('354 reply not received from server after DATA command.')
    #    return

    # Send message data.
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)
    #if recv5[:3] != '250':
    #    print('250 reply not received from server after message data.')
    #    return

    # Send QUIT command and handle server response.
    quitCommand = "QUIT\r\n"
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)
    #if recv6[:3] != '221':
    #    print('221 reply not received from server after QUIT command.')
    #    return

    clientSocket.close()

if __name__ == '__main__':
    smtp_client(port=1025, mailserver='127.0.0.1', from_address='sender@example.com', to_address='receiver@example.com')
