import os, wifisec, platform
from speedtest import SpeedTest
from hku import fetch_heroku
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
        main_tab = Table(header_style="bold magenta", show_edge=False, show_lines=False, show_header=False)
        main_tab.add_column("Network")
        main_tab.add_column("Projects")

        projects_tab = Table(header_style="bold magenta", title="Projects")
        projects_tab.add_column("Name")
        projects_tab.add_column("Running")
        for p in fetch_heroku():
            if p[1]:
                projects_tab.add_row(str(p[0]), "[green]True[/green]")
            else:
                projects_tab.add_row(str(p[0]), "[red]False[/red]")

        try:
            st = SpeedTest()
            ping = "%.2f" % st.ping()
            #download = "%.2f" % st.download()
            #upload = "%.2f" % st.upload()
        except OSError:
            ping = "# Connection Error"
        status_tab = Table(title="Network Status", header_style="bold magenta")
        status_tab.add_column("Stat")
        status_tab.add_column("Data")
        status_tab.add_row("Ping", str(ping))
        #status_tab.add_row("Download", str(download))
        #status_tab.add_row("Upload", str(upload))

        devices = wifisec.who()

        connected_tab = Table(title="Connected Devices", header_style="bold magenta")
        connected_tab.add_column("NAME")
        connected_tab.add_column("MAC")
        connected_tab.add_column("IP")

        clear()

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

            connected_tab.add_row(name, mac, ip)

        main_tab.add_row(status_tab, connected_tab, projects_tab)
        print(main_tab)
        #print("[bold red]No device secured, breach possible.[/bold red]")
