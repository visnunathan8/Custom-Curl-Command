
import socket
import argparse
import click
import logging
import http.client as httplib
import struct

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


@click.command(name='price')
@click.argument('host')
def get_connection(host):
    '''
    Gets the connection
    '''
    a1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a1.connect((socket.gethostbyname(host), 80))
    a2 = 'GET / HTTP/1.1\r\n' + 'Host: '+host+'\r\n\r\n'
    p = a1.send(a2.encode())
    while True :
        data = a1.recv(1024)
        click.echo(data)
    


get_group.add_command(get_connection)
visnu.add_command(get_group)
