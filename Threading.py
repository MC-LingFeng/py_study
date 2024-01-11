import threading
from pynput import mouse, keyboard
import MouseConfig
import KeybordConfig

class CreateThread(threading.Thread):
  def __init__(self, name):
    threading.Thread.__init__(self)
    self.name = name

  def mouse(self):
      listener = mouse.Listener(
        on_click=MouseConfig.on_click,
        on_move=MouseConfig.on_move,
        on_scroll=MouseConfig.on_scroll,
      )
      listener.start();
      listener.join(100);
  def keyboard(self):
      listener = keyboard.Listener(
        on_press=KeybordConfig.on_press,
        on_release=KeybordConfig.on_release,
      )
      listener.start();
      listener.join();
  
  def count(self):
    count = threading.active_count();
    print ('count is {0}', count)
    return count
  
  def thread(self):
    return threading.current_thread();
  
  def run(self):  
    print("start new Thread")  
    if self.name == 'mouse':
        self.mouse();
    elif self.name == 'keyboard':
        self.keyboard();
    else:
      print('name is not exist')
    print("Thread end")

# Create two threads
threadMouse = CreateThread('mouse')
threadKeyboard = CreateThread('keyboard')

# Start the threads
threadMouse.start()
threadKeyboard.start()

# Wait for both threads to finish
threadMouse.join()
threadKeyboard.join()


