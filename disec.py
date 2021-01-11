from re import T
import wifisec
import platform
from rich import print
import os
import pyspeedtest

def display():
    plat = platform.system()
    if plat == "Linux":
        clear = lambda: os.system('clear')
    elif plat == "Windows":
        clear = lambda: os.system('cls')

    while True:
        devices = wifisec.who()

        st = pyspeedtest.SpeedTest()
        ping = st.ping()

        clear()

        print("[bold cyan]Network stats:[/bold cyan]")
        print(" "*4, "Ping:", ping)
        #print(" "*4,st.download())
        #print(" "*4,st.upload())

        print("\n[bold cyan]Connected devices:[/bold cyan]")
        for d in devices:
            ip = d[1].split(".")
            for i, sec in enumerate(ip[1:-1]):
                ip[i+1] = "#"*len(sec)
            ip = ".".join(ip)

            mac = d[3].split(":")
            for i, sec in enumerate(mac[1:-1]):
                mac[i+1] = "#"*len(sec)
            mac = ":".join(mac)

            name = d[-1]
            if "(" in name:
                name = name[:name.find("(")]

            print(" "*4, "[green]{}[/green]; [green]{}[/green]; [green]{}[/green]".format(ip, mac, name))
