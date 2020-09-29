import subprocess
from mcstatus import MinecraftServer

ip = 'Put your minecraft server ip here!'

def info():
    return '''**Minecraft Server Module**: Minecraft info: *use like* `$serv [command]`
    `temp` Returns temperature of pi
    `clock` Returns clockspeed of core in GHz
    `voltage` Returns core voltage
    `status` Returns ip, players on, latency
'''

#hardware commands
bashTemp = 'vcgencmd measure_temp'
bashClock = 'vcgencmd measure_clock arm'
bashVoltage = 'vcgencmd measure_volts core'

def temp():
    C = float(subprocess.check_output(bashTemp.split(' ')).decode('utf-8')[5:-3])
    F = (C * 9 / 5) + 32 
    return 'Server temp: **' + str(F) + ' F**  **(' + str(C) + ' C)**'

def clock():
    HZ = float(subprocess.check_output(bashClock.split(' ')).decode('utf-8')[14:])
    return 'Server clockspeed: **' + str(HZ / 1000000000) + ' GHZ**'

def voltage():
    V = float(subprocess.check_output(bashVoltage.split(' ')).decode('utf-8')[5:-2])
    return 'Server voltage: **' + str(V) + 'V**'

def status():

    try:
        server = MinecraftServer.lookup(ip)
        latency = server.ping()
        query = server.query()
        status = server.status()
        return '''IP: **''' + ip + '''**
Version: **1.16.1**
Ping: **''' + str(latency) + '''ms**
Players:
> {0}'''.format("\n > ".join(query.players.names))  + '''
Player Count: **''' + str(status.players.online) + '''**'''
    except:
        return '🛑 **Server is down**'
