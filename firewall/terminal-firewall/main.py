#main.py 

#!usr/bin/python3

print('-'*100)
print('*'*25, 'Python Firewall', '*'*25)
print('-'*100)

print('\nRUN THIS AS ROOT.This firewall makes use of the Linux kernel\'s iptables package to ACCEPT, DROP, RETURN packets.It uses the filter table of iptables to help you easily create rules to control packets on your network')



def retr_interfaces():
    #imports
    from get_nic import getnic
    #main
    interfaces = list(getnic.interfaces())
    interfaces_with_information = getnic.ipaddr(interfaces)
    return interfaces, interfaces_with_information
def main():
    ifs, ifs_with_info = retr_interfaces()
    for interface in ifs:
        print (f'{ifs.index(interface)+1}: {interface}')
    #print(ifs_with_info)
    interface = int(input('Select interface number: '))
    #setting selected interface
    selected_interface = ifs[interface-1]
    #showing selected interface to user
    print(f'Using {ifs[interface-1]}')
    #filter chains
    filter_chains = ['INPUT', 'FORWARD', 'OUTPUT']
    #showing filter chains to user
    print('Filter chains: \n')
    print('1: INPUT\n2: Forward\n3: Output'
            )
    #setting selected filter chain
    input_for_selected_filter_chain = int(input('Select filter chain: '))
    selected_filter_chain = filter_chains[input_for_selected_filter_chain-1]

    #run rest of ip rule
    print('Supported rules arguments:\n-p [tcp|udp]\n--dport[22|80|443]\n-s[ip-range(eg.192.168.1.2)]\n
            ')
    print('An example of a rule you can use below is:\n1.) -s -j ACCEPT')
    rules = input('IP rules: ')
    os.system(rules)
if __name__ == '__main__':
    main()
