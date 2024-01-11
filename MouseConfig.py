def on_move(x, y):
  print('鼠标移动到 ({0}, {1})'.format(x, y))

def on_click(x, y, button, pressed):
  if pressed:
    print('鼠标点击在 ({0}, {1})'.format(x, y))

def on_scroll(x, y, dx, dy):
  print('鼠标滚动 {0} at ({1}, {2})'.format(
    '向下' if dy < 0 else '向上',
    x, y))