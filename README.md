# TCPServerProject
TCP Socket Programming Assignment
Group Members

Nilan Patel, Bryce Wellman, Noah Nielsen

Programming Language & Libraries:
Language: Python 3
Libraries Used:

socket - a built in socket programming library for network communication
threading - which is for handling multiple client connections at the same time for the extra credit part
random - random num generation
sys - For system specific parameters and functions

Justification: Python was chosen because of how much more simple it is for socket programming and it was the recommended language in thw lab. Its vast amount of libraries made sense for us.

Program Operation
Overview
This implementation consists of a TCP server and client that exchange integer values and calculate their sum. The communication follows a simple protocol where messages are formatted as name|number

To Run:
1. Download all files and enter vscode or any IDE
2. Ensure python3 or windows equivalent is downloaded
3. Set up a split terminal 
4. Type python3 server.py into the left side terminal
5. Type python3 client.py into right side terminal
6. Enter an int value and hit enter
7. View the server side terminal for the addition of client number and randomly generated server number showing lab was successful!
