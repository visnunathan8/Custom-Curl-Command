
import socket
import click
import http.client as httplib

@click.group()
def visnu():
    '''
    Fancy Commands to manage your assets
    '''
    pass


@click.group(name='get')
def get_group():
    '''
    Group of commands to get something
    '''
    pass

def strip_http_headers(http_reply):
    p = http_reply.find('\r\n\r\n')
    if p >= 0:
        return http_reply[p+4:]
    return http_reply

@click.command(name='price')
@click.argument('host')
@click.option('--verbose/--no-verbose', default=False)
def get_connection(host, verbose):
    '''
    Gets the connection
    '''
    a1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a1.connect((socket.gethostbyname(host), 80))
    a2 = 'GET /status/418 HTTP/1.1\r\n' + 'Host: '+host+'\r\n\r\n'
    p = a1.send(a2.encode())
    if verbose :
        header_data_Avail = False
    else :
        header_data_Avail = True
    while True :
        data = a1.recv(1024)
        if len(data) == 0:     # No more data received, quitting
            break
        if(header_data_Avail) :
            dddd = strip_http_headers(data.decode())
            header_data_Avail = False
        else :
            dddd = data
        click.echo(dddd)


get_group.add_command(get_connection)
visnu.add_command(get_group)