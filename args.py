import argparse

def main():
    parser = argparse.ArgumentParser(description='Display port and IP addresses.')
    
    # Optional arguments for server/client mode, port, and IP address
    parser.add_argument('-s', '--server', action='store_true', help='enable the server mode')
    parser.add_argument('-c', '--client', action='store_true', help='enable the client mode')
    parser.add_argument('-p', '--port', type=int, default=8088,
                        help='port number on which the server will listen or the client will connect to '
                             '(default: %(default)s)', choices=range(1024, 65536))
    parser.add_argument('-i', '--ip', type=str, default='127.0.0.1',
                        help='IP address of the server\'s interface where the client should connect '
                             '(default: %(default)s, format: 10.0.0.2)')

    args = parser.parse_args()

    # Check if both server and client modes are specified
    if args.server and args.client:
        print("You cannot use both at the same time.")
        return

    # Display port and IP addresses based on user's input
    if args.server:
        print("Server mode enabled.")
    elif args.client:
        print("Client mode enabled.")
    
    print("Port:", args.port)
    print("IP Address:", args.ip)

if __name__ == "__main__":
    main()
