from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import threading


class LocalFTPServer:
    def __init__(self, host='127.0.0.1', port=2121, user='user', password='password', root_directory='./'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.root_directory = root_directory

    def start_server(self):
        # Create an authorizer
        authorizer = DummyAuthorizer()
        authorizer.add_user(self.user, self.password, self.root_directory, perm='elradfmw')

        # Instantiate the FTP handler with the authorizer
        handler = FTPHandler
        handler.authorizer = authorizer

        ip_port = self.host, self.port

        # Instantiate the FTP server with the handler
        server = FTPServer(ip_port, handler)

        # Start the FTP server in a separate thread
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()

        print(f'Fake FTP Server started on {ip_port[0]}:{ip_port[1]}')

if __name__ == '__main__':
    fake_ftp_server = LocalFTPServer()
    fake_ftp_server.start_server()
