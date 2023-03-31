import nmap3
# Information gathering
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("scanme.nmap.org")
print(results)