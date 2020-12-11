import matplotlib.pyplot as plt
import scratch


sc = scratch.Scratch()

x = []
y = []
plt.ylim(0, 3.5)
lines, = plt.plot(x, y)

stopflag = False
while stopflag == False:
    message = sc.receive()

    for k, v in message['sensor-update'].items():
        print(k, v)
        if k == 'data':
            a = v.split(' ')
            if len(x) == 100:
                x.pop(0)
                y.pop(0)
            x.append(int(a[2]) / 1000.0)
            y.append(int(a[1]) / 4095.0 * 3.3)
            lines.set_data(x, y)
            if len(x) >= 2:
                plt.xlim(min(x), max(x))
            plt.pause(0.01)

    for s in message['broadcast']:
        print(s)
        if s == 'clear':
            plt.clf()
            x = []
            y = []
            plt.ylim(0, 3.5)
            lines, = plt.plot(x, y)
            plt.pause(0.01)
        elif s == 'stop':
            stopflag = True
