# LocalFTP Server

This Python script creates a simple FTP server using the `pyftpdlib` library. The server is configured to run locally, and you can customize the host, port, user credentials, and root directory as needed.

## Requirements
- Python 3.x
- `pyftpdlib` library (install using `pip install pyftpdlib`)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Eclipse91/LocalFTP-Server.git
   ```

2. Navigate to the project directory:

   ```bash
   cd LocalFTP-Server
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python local_server.py
   ```

5. The script will start a fake FTP server on the specified host and port.

## Configuration

You can customize the FTP server's configuration by modifying the parameters in the `LocalFTPServer` class constructor:

- `host`: The IP address on which the server will listen (default is "127.0.0.1").
- `port`: The port on which the server will listen (default is 2121).
- `user`: The username for FTP authentication (default is "user").
- `password`: The password for FTP authentication (default is "password").
- `root_directory`: The root directory for the FTP server (default is "./").

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Notes

Feel free to contribute or report issues!
This README provides a clearer structure, concise information, and instructions for setting up and running the LocalFTP-Server. Adjust the content as needed for your project.

