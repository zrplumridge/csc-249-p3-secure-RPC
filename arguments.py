from argparse import ArgumentTypeError

def _ip_address(x):
    bytes = x.split('.')
    if len(bytes) != 4:
        raise ArgumentTypeError
    for byte in bytes:
        byte = int(byte)
        if byte < 0 or byte > 255:
            raise ArgumentTypeError
    return x

def _port(x):
    x = int(x)
    
    # Usable port numbers are between 1024 and 65535 exclusive
    if x < 1024 or x > 65535:
        raise ArgumentTypeError
    return x

ip_addr_arg     = {'type': _ip_address,
                   'default': '127.0.0.1',
                   'metavar': 'IP_ADDRESS'}
server_port_arg = {'type': _port,
                   'default': 65432,
                   'metavar': 'PORT #'}
vpn_port_arg    = {'type': _port,
                   'default': 55554,
                   'metavar': 'PORT #'}
