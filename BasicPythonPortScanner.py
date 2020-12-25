#!/usr/bin/python3
#import socket module and the ipaddress module (ip address to scan networks)
import socket
import ipaddress
import sys

#ask user if they want to scan a single IP or a network
#user then reqeusts which ports to scan
direction = input("Would you like to Port Scan a single IP, or a Network? (1 for 'Single IP', 2 for 'Network'): ")
if direction.lower() == "1":
    IP = input("Enter IP Address: ")
    range_or_not = input("Would you like to scan a few ports, or a range of ports? (1 for 'One or Few', 2 for 'Range'): ")
    if range_or_not == "1":
        portToTest = input("Enter Port(s) to Scan (separate by comma if multiple): ").strip().split(",")
#empty list that will eventually be appended with Open Ports after the for loop scan
        success = []
        print(f"SCANNING REQUESTED PORTS FOR {IP}...")
        print("----------------------")
        try:
            for port in portToTest:
#create a socket for each port scan and set timeout time
                mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                mysock.settimeout(1)
                result = mysock.connect_ex((IP, int(port)))
                if result == 0:
                    success.append(port)
                    mysock.close()
                else:
                    pass
                    mysock.close()
            if success:
                print(f"The Open ports are: {success}")
            else:
                print("No Open Ports for the Port Scan Parameters")
        except ValueError:
            print("Error in Computation")
# common error with incorrect IP input
        except socket.gaierror:
            print("Error in Computation")
#ask for the range of ports, create range
    elif range_or_not == "2":
        first = int(input("First Port to Scan: "))
        last = int(input("Last Port to Scan: "))
        portToTest = range(first, last+1)
        success = []
        print(f"SCANNING REQUESTED PORTS FOR {IP}...")
        print("----------------------")
        try:
            for port in portToTest:
# create a socket for each port scan and set timeout time
                mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                mysock.settimeout(1)
                result = mysock.connect_ex((IP, int(port)))
                if result == 0:
                    success.append(port)
                    mysock.close()
                else:
                    pass
                    mysock.close()
            if success:
                print(f"The Open ports are: {success}")
            else:
                print("No Open Ports for the Port Scan Parameters")
        except ValueError:
            print("Error in Computation")
#common error with incorrect IP input
        except socket.gaierror:
            print("Error in Computation")

#if they want to scan a network
elif direction == "2":
    IP = input("Enter IP Address: ")
    subnet = input("Enter Subnet Mask: ")
    ipToTest = (IP + "/" + subnet)
#ipaddress module syntax to get the network w/ subnet mask
    ipToTest = ipaddress.ip_network(str(ipToTest), strict=False)
    print(f"We are scanning this network: {ipToTest}")
    range_or_not = input("Would you like to scan a few ports, or a range of ports? (1 for 'One or Few', 2 for 'Range'): ")
    if range_or_not == "1":
        portToTest = input("Enter Port(s) to Scan (separate by comma if multiple): ").strip().split(",")
        success = []
        print(f"SCANNING REQUESTED PORTS FOR {IP}...")
        print("----------------------")
        try:
            for address in ipToTest:
                print(str(address))
                for port in portToTest:
# create a socket for each port scan and set timeout time
                    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    mysock.settimeout(1)
                    result = mysock.connect_ex((str(address), int(port)))
                    if result == 0:
                        success.append(port)
                        mysock.close()
                    else:
                        pass
                        mysock.close()
                if success:
                    print(f"The Open ports for {address} are: {success}")
                    success = []
                else:
                    print(f"No Open Ports for the Port Scan Parameters for {address}")
        except ValueError:
            print("Error in Computation")
# common error with incorrect IP input
        except socket.gaierror:
            print("Error in Computation")
    elif range_or_not == "2":
        first = int(input("First Port to Scan: "))
        last = int(input("Last Port to Scan: "))
        portToTest = range(first, last + 1)
        success = []
        print(f"SCANNING REQUESTED PORTS FOR {IP}...")
        print("----------------------")
        try:
            for address in ipToTest:
                print(str(address))
                for port in portToTest:
# create a socket for each port scan and set timeout time
                    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    mysock.settimeout(1)
                    result = mysock.connect_ex((str(address), int(port)))
                    if result == 0:
                        success.append(port)
                        mysock.close()
                    else:
                        pass
                        mysock.close()
                if success:
                    print(f"The Open ports for {address } are: {success}")
                    success = []
                else:
                    print(f"No Open Ports for the Port Scan Parameters for {address}")
        except ValueError:
            print("Error in Computation")
# common error with incorrect IP input
        except socket.gaierror:
            print("Error in Computation")
else:
    print("Invalid Input. Closing")
    sys.exit()