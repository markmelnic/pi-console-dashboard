import os, wifisec, platform
from speedtest import SpeedTest
from rich import print
from rich.table import Table

def display():
    plat = platform.system()
    global clear
    if plat == "Linux":
        clear = lambda: os.system('clear')
    elif plat == "Windows":
        clear = lambda: os.system('cls')

    while True:
        devices = wifisec.who()

        try:
            st = SpeedTest()
            ping = st.ping()
            ping = "%.2f" % ping
        except OSError:
            ping = "# Connection Error"

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("IP")
        table.add_column("MAC")
        table.add_column("NAME")

        clear()

        print("[bold cyan]Network stats:[/bold cyan]")
        print(" "*4, "Ping: [green]%s[/green]ms" % ping)
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

            table.add_row(ip, mac, name)

        print(table)
        #print("[bold red]No device secured, breach possible.[/bold red]")
