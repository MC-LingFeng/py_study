
from pynput import keyboard

def on_press(key):
  try:
    print('按键 {0} 被按下'.format(key.char))
  except AttributeError:
    print('特殊按键 {0} 被按下'.format(key))

def on_release(key):
  print('按键 {0} 被释放'.format(key))
  if key == keyboard.Key.esc:
    # 退出监听
    return False
