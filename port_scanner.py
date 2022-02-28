import socket
import re
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    ValidIpAddressRegex = re.compile(r'^\d+[.]\d+[.]\d+[.]\d+$')

    try:
        address = socket.gethostbyname(target)
    except:
        if ValidIpAddressRegex.match(target):
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"

    if address:
        for port in range(port_range[0], port_range[1] + 1):
            s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

            try:
                s.settimeout(1)
                s.connect((address, port))
                open_ports.append(port)
            except:
                pass
            s.close()
     
        
    if verbose: 
      try:
        hostname = socket.gethostbyaddr(target)[0] 
      except: 
        hostname = target
      IPAddr = socket.gethostbyname(hostname)

      returnString = "Open ports for " + hostname
      if hostname != target or hostname != IPAddr:     
        returnString +=" (" + IPAddr + ")"
      returnString +=  "\nPORT     SERVICE"
      for ports in open_ports:
          returnString += "\n" + str(ports).ljust(8) + " " + ports_and_services.setdefault(ports, target)

      return returnString
    else:
      return(open_ports)