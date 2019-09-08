import sys
import numpy as np
import sounddevice as sd
from numpy import sin, cos, pi
import time
import clipboard

samplerate = 44100 #sd.query_devices(args.device, 'output')['default_samplerate']
start_idx = 0

def callback(outdata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    global start_idx
    global formula
    t = (start_idx + np.arange(frames)) / samplerate
    t = t.reshape(-1, 1)
    outdata[:] = formula(t)
    start_idx += frames

def reproducir(callback, samplerate):
    clipboard_actual = clipboard.paste()
    with sd.OutputStream(channels=1,
                         callback=callback,
                         samplerate=samplerate):
        while True:
            clipboard_next = clipboard.paste()
            while clipboard_actual == clipboard_next:
                time.sleep(0.3)
                clipboard_next = clipboard.paste()
            clipboard_actual = clipboard_next
            if clipboard_actual.lower() in ['salir', 'exit', 'q', 'quit']:
                return None
            try:
                formula_nueva = lambda t: eval(clipboard_actual)
                formula_nueva(0.0) # check that syntax is ok
                return formula_nueva
            except:
                continue

print('A jugar!')
formula = lambda t: eval('0.2 * sin(2 * pi * 500 * t)')
formula_anterior = formula
while True:
    try:
        formula_nueva = reproducir(callback, samplerate)
        if formula_nueva is None:
            break
        formula_anterior = formula
        formula = formula_nueva
    except KeyboardInterrupt:
        break
    except:
        formula = formula_anterior
print('Fin!')
