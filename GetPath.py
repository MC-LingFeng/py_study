import psutil

def get_running_processes():
  processes = []
  for proc in psutil.process_iter(['pid', 'name']):
    processes.append({'pid': proc.info['pid'], 'name': proc.info['name']})
  return processes

if __name__ == '__main__':
  running_processes = get_running_processes()
  for process in running_processes:
    print(f"PID: {process['pid']}, Name: {process['name']}")
