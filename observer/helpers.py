import socket

def communicate(host, port, request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(request.encode('utf-8'))
    response = str(s.recv(1024), "utf-8")
    s.close()
    return response
