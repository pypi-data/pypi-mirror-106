def cmp(file):
    import hashlib, base64, requests

    def sethostandport(host, port):
      global hp 
      hp = (host, port)

    def sends(text):
      import socket 

      s = socket.socket() 
      s.bind(hp)
      s.listen(1)
      while 1:
        conn, addr = s.accept() 
        conn.sendall(f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n{text}'.encode())
    def md5encode(string):
      return hashlib.md5(string.encode()).hexdigest()

    def b64encode(string):
      return base64.b64encode(string.encode()).decode()

    def getfilecontents(name):
      return open(name).read()

    def writefilecontents(name, text, mode='Overwrite'):
      if mode == 'Overwrite':
        open(name, 'w').write(text)
      if mode == 'KeepAppend':
        open(name, 'a').write(text)
      return len(text)


    [exec(line) for line in open(file) if not line.startswith('!')] 

    
