
# Baato: _A file sharing application_

This is a sample code for sharing files form one windows system to another system using the Wifi Direct.
This code is capable of sharing files at a speed of 40 Mb/s.

Note: Speed increases when both the devices are connected without Internet connection. (hostednetwork adapter in windows 10)

Just an example of how peer to peer connections work using Python3

### Accessing through Terminal/Command-line  
The python version of this application is latest!  

1. Open the app by running ```python3 baatoApp.py```  
2. The the desired option.
    - If you are the sender:  
        - Set up your `IP-Address` or `Hosting URL`  
        - Wait for the reciver to connect  
        - Choose the files that you want to send  
    - If you are the receiver  
        - Provide the sender's `IP-Address` or `Hosting URL`  
        - Wait for the files to arrive  
3. _You can use localhost (127.0.0.1) for testing on the same machine._  

### Accessing through Executable  
Head towards [dist](dist/) directory and following simple steps:  
1. Just start hotspot manually from one system. (Host)
2. Connect to the host system from an another system. (Client)
3. Put socket_server.exe on host system and socket_client.exe file on client system
4. First run server and then client executables in respective system.
5. Sit back as your transfer is happening.

