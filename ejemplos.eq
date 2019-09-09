Single tone (1KHz):
0.2*sin(2*pi*1000*t)

1 KHz tone + 700 Hz tone:
0.05*sin(2*pi*1000*t)+0.025*sin(2*pi*700*t)

1 KHz square wave:
0.01 * mod(2*t*1e3,2)


1 KHz that for 0.25 seconds and off for 0.5 seconds:
0.01 * mod(2*t*1e3,2) * (mod(t/0.25,3)==0)


0.01 * (floor(2*t*1e3)%2) * ((floor(t/0.25)%3)==0) + 0.02 * (floor(2*t*2e3)%2) * ((floor(t/0.125+3)%4)==0)

0.05*sin(2*pi*500*(1+0.5*mod(t/0.5,4))*t)

0.05*sin(2*pi*1000*t)+0.025*sin(2*pi*700*t)+0.03*(t*1000%2) * sin(2*pi*(t*1000%4))

0.05*sin(2*pi*1000*t)+0.025*sin(2*pi*700*t)+0.01*(t*1000%2) * sin(2*pi*(t*1000%4))

falopa:
0.1*sin(2*pi*(t*10000%4)*t)

0.1*sin(2*pi*(mod(t*10000,4))*t)

mute:
0

exit:
quit
