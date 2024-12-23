class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
    """
    def __init__(self, msg, sender, recipient_name):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name

class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Append the email to the inbox of the client it is addressed to."""
        self.clients[email.recipient_name].inbox.append(email)
#self.clients[email.recipient_name]：通过收件人的名字查找对应的 Client 对象。

    def register_client(self, client):
        """Add a client to the dictionary of clients."""
        self.clients[client.name] = client

class Client:
    """A client has a server, a name (str), and an inbox (list).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    >>> b.inbox[1].sender.name
    'Alice'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_client(name)
#server.register_client(self)：将客户端注册到服务器的 clients 字典中。

    def compose(self, message, recipient_name):
        """Send an email with the given message to the recipient."""
        email = Email(message,self, recipient_name)
        self.server.send(email)
    #这里email里使用的self是指Client对象（实例对象），email类中间的sender也是Client