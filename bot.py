# -*- coding: utf-8 -*-
import sleekxmpp
import json
import time

user = raw_input("Usuario >> ")
password = raw_input("Contraseña >> ")
mensaje = """
Hola, me cambié de facebook, si querés agregame :)
https://www.facebook.com/ignacio.rodriguez.1999
Por cierto, este mensaje es automático..
Saludos..
--
I moved to another facebook >.>
https://www.facebook.com/ignacio.rodriguez.1999
Add me if you want :)
btw, this is auto msg..
Grettings..
--
https://github.com/i5o/xmpptest
"""


class EchoBot(sleekxmpp.ClientXMPP):

    def __init__(self):
        sleekxmpp.ClientXMPP.__init__(self, user, password)

        self.add_event_handler('session_start', self.start)
        self.add_event_handler('presence', self.test)
        self.enviados = json.loads(open("enviados.json", "r").read())

    def start(self, event):
        self.send_presence()
        self.get_roster()

    def test(self, a):
        if a['from'] in self.enviados:
            print "Ya se lo envíe a: %s" % a['from']
            return

        print "Enviado a: %s" % a['from']
        self.enviados.append(str(a['from']))
        open("enviados.json", "w").write(json.dumps(self.enviados, indent=4))
        self.send_message(a['from'], mensaje)
	time.sleep(2)

if __name__ == "__main__":
    xmpp = EchoBot()
    xmpp.register_plugin('xep_0030')
    xmpp.register_plugin('xep_0004')
    xmpp.register_plugin('xep_0060')
    xmpp.register_plugin('xep_0199')

    if xmpp.connect():
        xmpp.process(threaded=False)
    else:
        print("unable to connected")
