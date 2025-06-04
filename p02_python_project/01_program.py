# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

def main():
    print("Servers: ")
    for server in server_config.keys(): print(server)
    server_name = input("Please select server: ")
    status = get_server_status(server_name)
    print(f"{server_name} status: {status}")

if __name__ == "__main__":
    main()
