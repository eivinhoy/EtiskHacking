from scapy.all import sniff



def packet_callback(packet):
    print(packet.show())


sniff(filter="ip", prn=packet_callback, count=1)