"""
Main file for summary functionality
"""
from src.utils import network_arping, get_current_network, get_current_ip, get_hostname
from prettytable import PrettyTable
import time


class Summary:
    """ Summary class """

    def __init__(self, args):
        self.__my_ip = get_current_ip()
        self.__my_network = get_current_network()
        self.__args = args

    def display(self):
        """
        Displays specified information

        :return None:
        """
        start_time = time.time()
        final_output = network_arping(self.__my_network)

        if vars(self.__args).get('hostname'):
            print('Hostname selected.')
            final_output = self._hostname(final_output)
            # TODO: Call hostname method to retrieve hostnames based on $final_output's IP's, and append to each
            #  dictionary within the $final_outputs list

        headers = []
        for item in final_output:
            for key in item.keys():
                if key not in headers:
                    headers.append(key)
        table = PrettyTable(headers)

        for i in final_output:
            values = []
            for value in i.values():
                values.append(value)
            table.add_row(values)

        if not final_output:
            print('No devices found, possibly an interface issue but who knows. This program is pretty scuffed')
        else:
            end_time = time.time() - start_time
            print(table)
            print(f'Execution time: {end_time}')

    def _hostname(self, device_list):
        """
        Takes in a list of device JSON objects. Parses through each item in the list, and uses the IP/MAC to determine
        the hostname and append it back into the JSON object as a new key/value pair.

        :param device_list:
        :return device_list:
        """

        for item in device_list:
            ip = item["IP"]
            item['Hostname'] = get_hostname(ip)

        return device_list
