from scapy.all import *

print("--- Scapy Packet Sniffer ---")
print("Status: Listening for 10 packets on Wi-Fi...")

# This captures 10 packets that are already moving on your network
# iface="Wi-Fi" ensures it looks at your internet card
captured_packets = sniff(iface="Wi-Fi", count=10)

print("\n[SUCCESS] Captured 10 packets successfully!")
print("-" * 30)

# This shows the list of packets caught (TCP, UDP, or ICMP)
captured_packets.summary()

input("\nPress Enter to exit...")