import matplotlib.pyplot as plt
import scratch


sc = scratch.Scratch()

x0 = []
x1 = []
y0 = []
y1 = []
plt.ylim(0, 3.5)
lines0, = plt.plot(x0, y0)
lines1, = plt.plot(x1, y1)

stopflag = False
while stopflag == False:
    message = sc.receive()

    for k, v in message['sensor-update'].items():
        print(k, v)
        if k == 'data':
            a = v.split(' ')
            if len(x0) == 100:
                x0.pop(0)
                x1.pop(0)
                y0.pop(0)
                y1.pop(0)
            x0.append(int(a[2]) / 1000.0)
            x1.append(int(a[4]) / 1000.0)
            y0.append(int(a[1]) / 4095.0 * 3.3)
            y1.append(int(a[3]) / 4095.0 * 3.3)
            lines0.set_data(x0, y0)
            lines1.set_data(x1, y1)
            if len(x0) >= 2:
                plt.xlim(min(min(x0), min(x1)), max(max(x0), max(x1)))
            plt.pause(0.01)

    for s in message['broadcast']:
        print(s)
        if s == 'clear':
            plt.clf()
            x0 = []
            x1 = []
            y0 = []
            y1 = []
            plt.ylim(0, 3.5)
            lines0, = plt.plot(x0, y0)
            lines1, = plt.plot(x1, y1)
            plt.pause(0.01)
        elif s == 'stop':
            stopflag = True
