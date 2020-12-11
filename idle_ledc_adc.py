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
            x = []
            y = []
            for i in range(1, len(a), 2):
                x.append(int(a[i + 1]) / 1000.0)
                y.append(int(a[i]) / 4095.0 * 3.3)

            sortedx = sorted(x)
            trigpos = round((len(sortedx) * 10) / 100)
            trigx = sortedx[trigpos]
            x = [p - trigx for p in x]

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
