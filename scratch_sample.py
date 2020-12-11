import scratch


sc = scratch.Scratch()

stopflag = False
while stopflag == False:
    message = sc.receive()

    for k, v in message['sensor-update'].items():
        print(k, v)

    for s in message['broadcast']:
        print(s)
        if s == 'stop':
            stopflag = True
