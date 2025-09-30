#!/usr/bin/env python3
"""
TCP Client Implementation
Author: [Your Name Here]
"""

import socket
import sys

class TCPClient:
    def __init__(self, host='127.0.0.1', port=5555):
        """initialize client with server address"""
        self.host = host
        self.port = port
        self.client_name = "Client of Nilan and Bryce"  # change to your name
        
    def connect_and_send(self, number):
        """connect to server and send message"""
        # create tcp socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # connect to server
            print(f"Connecting to server at {self.host}:{self.port}")
            client_socket.connect((self.host, self.port))
            print("Connected successfully!")
            
            # prepare message (name|number)
            message = f"{self.client_name}|{number}"
            
            # send msg to server
            client_socket.send(message.encode('utf-8'))
            print(f"Sent: {self.client_name} with number: {number}")
            
            # receive response from server
            response = client_socket.recv(1024).decode('utf-8')
            
            if response:
                # parse server response
                parts = response.split('|')
                if len(parts) == 2:
                    server_name = parts[0]
                    server_number = int(parts[1])
                    
                    # display all information
                    print("\n" + "="*50)
                    print("RESULTS:")
                    print(f"Client name: {self.client_name}")
                    print(f"Server name: {server_name}")
                    print(f"Client's number: {number}")
                    print(f"Server's number: {server_number}")
                    print(f"Sum of numbers: {number + server_number}")
                    print("="*50)
                else:
                    print("Invalid response from server")
            else:
                print("No response from server")
                
        except ConnectionRefusedError:
            print("Error: Cannot connect to server. Make sure server is running!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # close socket
            client_socket.close()
            print("\nClient socket closed")

def get_user_input():
    """get integer input from user"""
    while True:
        try:
            num = int(input("Enter an integer between 1-100 (or <1 or >100 to shutdown server): "))
            return num
        except ValueError:
            print("Invalid input! Please enter an integer")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

def main():
    """main function to run client"""
    # server configuration - must match server
    HOST = '127.0.0.1'  # server ip address
    PORT = 5555  # server port
    
    print("TCP CLIENT PROGRAM")
    print("="*50)
    
    # get user input
    number = get_user_input()
    
    # create client and send message
    client = TCPClient(HOST, PORT)
    client.connect_and_send(number)

if __name__ == "__main__":
    main()