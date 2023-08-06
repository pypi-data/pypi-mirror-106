"""
Helpers file
"""
from scapy.arch import get_if_addr, get_if_hwaddr
from scapy.config import conf
from scapy.sendrecv import srp
from scapy.layers.l2 import ARP, Ether
from ipaddress import ip_address, ip_network

from socket import getfqdn
import ipaddress


def get_current_ip():
    """ Returns the local IP of default interface """
    ip = get_if_addr(conf.iface)
    return ip_address(ip)


def get_current_network():
    ip = get_if_addr(conf.iface)
    return ip_network(ip + '/255.255.255.0', strict=False)


def get_current_mac():
    return get_if_hwaddr(conf.iface)


def network_arping(network):
    active_devices = []
    # TODO: Determine proper interface to use for windows. Default needs to be correctly identified
    res = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=str(network)), timeout=5, verbose=0, iface=conf.iface)[0]

    for index, item in enumerate(res, start=1):
        device_dict = {
            "Device #": index,
            "IP": item[1].psrc,
            "MAC": item[1].hwsrc
        }
        active_devices.append(device_dict)
    return active_devices


def get_hostname(ip):
    """
    Takes in a single IP address and retrieves the hostname form the connected network

    :param ip:
    :return:
    """

    # TODO: Each unsuccessful hostname request currently takes on average 4.5 seconds to complete, while a successful
    #  request takes 1.5 seconds. This should be fixed with some sort of timeout function capped at around 2 seconds

    name = getfqdn(ip)
    try:
        if ipaddress.ip_address(name):
            return 'Unknown'
    except ValueError:
        return name

