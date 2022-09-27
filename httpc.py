from email import header
from email.policy import default
import json
import socket
import click
import http.client as httplib
from urllib.parse import urlparse



@click.group()
def httpc():
    '''
    Fancy Commands to manage your assets
    '''
    pass


# @click.group(name='get')
# def get_group():
#     '''
#     Group of commands to get something
#     '''
#     pass

def strip_http_headers(http_reply):
    p = http_reply.find('\r\n\r\n')
    if p >= 0:
        return http_reply[p+4:]
    return http_reply

@click.command(name='get')
@click.argument('host')
@click.option('--verbose/--no-verbose', default=False)
@click.option('-v/-nv', default=False)
def get_connection(host, verbose, v):
    '''
    Gets the connection
    '''
    domain = urlparse(host).netloc
    a1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a1.connect((socket.gethostbyname(domain), 80))
    lengthhh = host.index(domain)
    urlPath = host[lengthhh + len(domain) : len(host)]
    a2 = 'GET '+urlPath+' HTTP/1.1\r\n' + 'Host: '+domain+'\r\n\r\n'
    p = a1.send(a2.encode())
    with a1:
        if verbose or v:
            header_data_Avail = False
        else :
            header_data_Avail = True
        data = a1.recv(1024)
        if(header_data_Avail) :
            dddd = strip_http_headers(data.decode())
            header_data_Avail = False
        else :
            dddd = data
        click.echo(dddd)



@click.command(name='post')
@click.option('-h', multiple=True)
@click.option('--d/--nd', default=False)
@click.argument('da', nargs=-1)
@click.option('-f')
@click.argument('host')
def post_connection(h, d, da, f, host):
    #d = d[1:-1]
    body = []
    domain = urlparse(host).netloc
    if d and (len(da)!=0):
        for arg in da:
            body.append(arg)
        
    if f:
        with open(f, "r") as f:
            body = f.read()
    #click.echo(body)
    #click.echo("ASDFASDFAWEFAWEFAWEFWAEFAWEFAWEFAWEFAWEFAWFE")
    a1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #click.echo(domain)
    a1.connect(("127.0.0.1", 8081))
    
    lengthhh = host.index(domain)
    urlPath = host[lengthhh + len(domain) : len(host)]
    #click.echo(urlPath)
    Headers = 'POST '+urlPath+' HTTP/1.1\r\n'
    #body = 'login=ocketvisnu@gmail.com&password=Visnu@123'   
    Headers += 'Host: '+domain+""+'\r\n'
    for p in h:
        Headers += p
    Headers += "\r\n"
   
    # body_bytes = body[0].encode('ascii')
    # header_bytes = Headers.format(
    #     content_type="application/x-www-form-urlencoded",
    #     content_length=len(body_bytes),
    #     host=str(domain) + ":80"
    # ).encode('iso-8859-1')
    if d:
        contentLength = "Content-Length: " + str(len(body[0])) + "\r\n\r\n"
        payload = (Headers + contentLength + body[0])
    else :
        contentLength = "Content-Length: " + str(len(body)) + "\r\n\r\n"
        payload = (Headers + contentLength + body)

    
    #click.echo(payload)
    
    p = a1.sendall(payload.encode())
    #click.echo(p)
    while True:
        data = a1.recv(1024).decode()
        click.echo(data)
        if data == '':
            break


httpc.add_command(get_connection)
httpc.add_command(post_connection)


#curl post -H 'Content-Type: application/json' -d '{"username":"rocketvisnu@gmail.com","password":"Visnu@123"}' https://www.reqbin.com/api/v1/account/login


#httpc post -h 'Content-Type: application/json' --d '{ "type": "3", "password": "admin", "employeeId": "admin"}' http://www.localhost.com/userAccount/adduseraccount/


#curl -H 'Content-Type: application/json' -d '{ "type": "3", "password": "admin", "employeeId": "admin"}' http://localhost:8081/userAccount/adduseraccount/

#with file
#httpc post -h 'Content-Type: application/json' -f '/Users/macbook/Desktop/COURSE WORK/Networks/Sockets/sampledata.txt' http://www.localhost.com/userAccount/adduseraccount/