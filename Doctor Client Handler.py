from codecs import decode
from threading import Thread
from doctor import Doctor

BUFSIZE = 1024
CODE = "ascii"

class DoctorClientHandler(Thread):
    """Handles a session between a doctor and a patient. """

    def __int__(self, client):
        Thread.__init__(self)
        self.client = client
        self.dr = Doctor()

    def run(self):
        self.client.send(bytes(self.dr.greetings(), CODE))
        while True:
            message = decode(self.client.recv(BUFSIZE), CODE)
            if not  message:
                print("Client disconnected")
                self.client.close()
                break
            else:
                self.client(bytes(self.dr.reply(message), CODE))
                
