
"""
TCP server project
Nilan and Bryce
"""

import socket
import random
import threading

class TCPServer:
    def __init__(self, host='127.0.0.1', port=5555):
        """initialize server with host and port"""
        self.host = host
        self.port = port
        self.server_name = "Server of Nilan + Bryce "  # change to your name
        self.server_number = random.randint(1, 100)  # server picks random number
        self.running = True
        
    def handle_client(self, client_socket, address):
        #handle client connection in separate thread
        try:
            # receive msg from client
            data = client_socket.recv(1024).decode('utf-8')
            
            if not data:
                return
                
            # parse client message
            parts = data.split('|')
            if len(parts) != 2:
                print("Invalid message format")
                return
                
            client_name = parts[0]
            client_number = int(parts[1])
            
            # print client and server names
            print(f"\nClient name: {client_name}")
            print(f"Server name: {self.server_name}")
            
            # check if number in range
            if client_number < 1 or client_number > 100:
                print(f"Received out of range number: {client_number}")
                print("Shutting down server...")
                self.running = False
                client_socket.close()
                return
            
            # calculate and display numbers
            sum_value = client_number + self.server_number
            print(f"Client's number: {client_number}")
            print(f"Server's number: {self.server_number}")
            print(f"Sum: {sum_value}")
            
            # send response to client
            response = f"{self.server_name}|{self.server_number}"
            client_socket.send(response.encode('utf-8'))
            
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()
    
    def start(self):
        """start server and listen for connections"""
        # create tcp socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # allow reuse of address
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            # bind socket to address and port
            server_socket.bind((self.host, self.port))
            
            # listen for incoming connections
            server_socket.listen(5)
            
            print(f"Server listening on {self.host}:{self.port}")
            print(f"Server name: {self.server_name}")
            print("Waiting for clients...")
            print("(Send number < 1 or > 100 to shutdown)")
            print("-" * 50)
            
            while self.running:
                try:
                    # set timeout to check running flag
                    server_socket.settimeout(1.0)
                    
                    # accept client connection
                    client_socket, address = server_socket.accept()
                    print(f"\nConnection from: {address}")
                    
                    # handle client in new thread for concurrency
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, address)
                    )
                    client_thread.start()
                    
                except socket.timeout:
                    continue
                except Exception as e:
                    if self.running:
                        print(f"Error accepting connection: {e}")
                    
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            # close server socket
            server_socket.close()
            print("\nServer shutdown complete")

def main():
    """main function to run server"""
    # server configs
    HOST = '127.0.0.1'  
    PORT = 5555  
    
    server = TCPServer(HOST, PORT)
    server.start()

if __name__ == "__main__":
    main()