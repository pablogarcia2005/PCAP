# Este código no puede ser abortado
# presionando Ctrl-C.
 
from time import sleep
 
seconds = 0
 
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("¡No hagas eso!")
        break
 