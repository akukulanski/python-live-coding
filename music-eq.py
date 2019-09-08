import numpy as np
import sounddevice as sd
from numpy import sin, cos, pi
import time
import clipboard

samplerate = 44100 #sd.query_devices(args.device, 'output')['default_samplerate']
start_idx = 0

def my_callback(outdata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    global start_idx
    global formula
    t = (start_idx + np.arange(frames)) / samplerate
    t = t.reshape(-1, 1)
    outdata[:] = formula(t)
    start_idx += frames

print('Estamos sonando!!!')
formula_anterior = '0.2 * sin(2 * pi * 500 * t)'
clipboard.copy(formula_anterior)
formula_nueva = clipboard.paste()
formula = lambda t: eval(formula_nueva)
while True:
    try:
        with sd.OutputStream(channels=1,
                             callback=my_callback,
                             samplerate=samplerate):
            formula_anterior = formula_nueva
            while formula_nueva == formula_anterior:
                time.sleep(0.3)
                formula_nueva = clipboard.paste()
            if formula_nueva.lower() not in ['salir', 'exit', 'q', 'quit']:
                try:
                    print('cambiando fórmula...')
                    formula = lambda t: eval(formula_nueva)
                except:
                    print('Error en fórmula')
                    formula_nueva = formula_anterior
                    formula = lambda t: eval(formula_nueva)
            else:
                print('saliendo...')
                break
    except KeyboardInterrupt:
        print('salida forzada')
        exit()
    except:
        print('Error en fórmula')
        formula_nueva = formula_anterior
        formula = lambda t: eval(formula_nueva)

print('Fin!')
