from Tkinter import *
from tcp.mboard.sessions.client.protocol import *
import sched, time
import logging
FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
logging.basicConfig(level=logging.DEBUG,format=FORMAT)
LOG = logging.getLogger()

server = ('127.0.0.1',int('7777'))
    
msgs = open_file(server, 'myfirstfile.txt')

serverResponded = True

def motion(event):
  global serverResponded
  if(serverResponded):
      view = event.widget
      text = event.widget.get("1.0",END)
      cursorIndex = view.index(INSERT)
      view.delete("1.0", END)
      serverResponded = False
      view.insert("1.0", ''.join(update_file(server, 'myfirstfile.txt', text)))
      serverResponded = True
      line, column = cursorIndex.split(".")
      view.mark_set(INSERT, "%s.%s" % (line, column))
    
def updateTextFromServer():
      LOG.info("Called update from server")
      cursorIndex = msg.index(INSERT)
      msg.delete("1.0", END)
      serverResponded = False
      msg.insert("1.0", ''.join(open_file(server, 'myfirstfile.txt')))
      serverResponded = True
      line, column = cursorIndex.split(".")
      msg.mark_set(INSERT, "%s.%s" % (line, column))
      master.after(3000, updateTextFromServer)
         
master = Tk()
msg = Text(master)
msg.bind('<KeyRelease>',motion)
msg.insert(END, ''.join(msgs))
msg.pack()

master.after(1000, updateTextFromServer)

mainloop()

