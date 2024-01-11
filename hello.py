import threading

def print_number(number):
  print(number)

# Create two threads
thread1 = threading.Thread(target=print_number, args=(1,))
thread2 = threading.Thread(target=print_number, args=(2,))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()
