# Bibliotheken laden
import network

# Client-Betrieb
wlan = network.WLAN(network.STA_IF)

# WLAN-Interface aktivieren
wlan.active(True)

# WLANs ausgeben
wscan = wlan.scan()
print (type(wscan))
print("Gefundene Netzwerke:")
for i in range(0, len(wscan)):
    print(wscan[i])
