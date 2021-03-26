# List of packages to import
from cobra.mit.session import LoginSession
from cobra.mit.access import MoDirectory
import urllib3
import requests
import json
import string
from hostList import hostListDNV, hostListCGY
from credentials import credentials
from pprint import pprint


urllib3.disable_warnings()


def getDC():
    # prompt to choose Data Center APIC
    print()
    print('ACI Fabric Interface Details')
    print('1 - Fortrust Data Center APIC')
    print('2 - Q93 Data Center APIC')
    print('0 - Exit Program')
    print()
    while True:
        dc = input('Choose which Data Center: ')

        if dc == '1' or dc == '2':
            break
        elif dc == '0':
            exit()
        else:
            print()
            print("Please select option: '1' - Fortrust or '2' - Q93' or '0' - Exit")
            print()

    return dc

# declare variables
dc = getDC()
url = credentials['urlDNV'] if dc == '1' else credentials['urlCGY']
hostList = hostListDNV if dc == '1' else hostListCGY
user = credentials['username']
pw = credentials['password']


# log into an APIC and create a directory object
ls = LoginSession(url, user, pw)
md = MoDirectory(ls)
md.login()

# search by Class
# psu = md.lookupByClass("fabricNode", parentDn='topology/pod-1')

def printHeader():
    # print header
    print()
    print("{:<13} {:<8} {:<13} {:<13} {:<20} {:<13} {:<13} {:<13} {:<13} {:<20} {:<20} {:<20} {:<15}"
          .format('DataCenter', 'NodeID', 'Interface', 'Status', 'Status Quality', 'Speed', 'DOM TX', 'DOM RX',
                  'DOM Temp', 'Optic Vendor', 'Optic Type', 'Optic P/N', 'Optic S/N'))
    print("{:<13} {:<8} {:<13} {:<13} {:<20} {:<13} {:<13} {:<13} {:<13} {:<20} {:<20} {:<20} {:<15}"
          .format('__________', '______', '_________', '______', '______________', '_____', '______', '______',
                  '________', '____________', '__________', '__________', '__________'))


def model9348(host):
    # print header
    printHeader()

    for i in range(1, (int(host['numPhyInt']) + 1)):
        phy = '1/' + str(i)
        # print(phy)
        # pprint(host)
        speedDn = md.lookupByDn('topology/pod-1/node-' + host['leaf'] + '/sys/phys-[eth' + str(phy) + ']/phys')
        # pprint(vars(speedDn))

        print('{:<13} {:<8} {:<13} {:<13} {:<20} {:<13}'
              .format(host['dc'], host['leaf'], str(phy), speedDn.operSt, speedDn.operStQual, speedDn.operSpeed))
        continue


def domStatus(hosts):
    for host in hosts:

        # send switch model 9348 to function since it has different DNs than the 93180
        if host['model'] == '9348':
            model9348(host)
            continue

        # print header
        printHeader()

        for i in range(1, (int(host['numPhyInt']) + 1)):
            phy = '1/' + str(i)

            speedDn = md.lookupByDn('topology/pod-1/node-' + host['leaf'] + '/sys/phys-[eth' + str(phy) + ']/phys')
            # pprint(vars(speedDn))
            opticDn = md.lookupByDn('topology/pod-1/node-' + host['leaf'] + '/sys/phys-[eth' + str(phy) + ']/phys/fcot')
            # pprint(vars(opticDn))

            # condition: status interface 'down'
            if speedDn.operSt == 'down':
                print('{:<13} {:<8} {:<13} {:<13} {:<20} {:<13}'
                      .format(host['dc'], host['leaf'], str(phy), speedDn.operSt, speedDn.operStQual, speedDn.operSpeed))
                continue

            # condition: interface is non-optical (twinax or copper SFP)
            elif opticDn.typeName == 'SFP-H10GB-CU1M' \
                or opticDn.typeName == 'SFP-H10GB-CU2M' \
                or opticDn.typeName == 'SFP-H10GB-CU3M' \
                or opticDn.typeName == 'SFP-H10GB-CU5M' \
                or opticDn.typeName == 'SFP-H10GB-CU10M' \
                or opticDn.typeName == 'SFP-H10GB-AOC3M' \
                or opticDn.typeName == 'SFP-H10GB-AOC7M' \
                or opticDn.typeName == 'SFP-H10GB-AOC10M' \
                or opticDn.typeName == '1000base-T' \
                or opticDn.typeName == "QSFP-100G-CR4":

                print('{:<13} {:<8} {:<13} {:<13} {:<20} {:<13} {:<13} {:<13} {:<13} {:<20} {:<20} {:<20} {:<15}'
                      .format(host['dc'], host['leaf'], str(phy), speedDn.operSt, speedDn.operStQual, speedDn.operSpeed,
                              ' ', ' ', ' ', opticDn.guiName, opticDn.typeName, opticDn.guiPN, opticDn.guiSN))
                continue

            # condition: interface is optical (1g/10g/40g/100g SFP)
            else:
                domTXDn = md.lookupByDn('topology/pod-1/node-' + host['leaf'] + '/sys/phys-[eth' + str(phy) + ']/phys/domstats/txpower')
                domRXDn = md.lookupByDn('topology/pod-1/node-' + host['leaf'] + '/sys/phys-[eth' + str(phy) + ']/phys/domstats/rxpower')
                domTempDn = md.lookupByDn('topology/pod-1/node-' + host['leaf'] + '/sys/phys-[eth' + str(phy) + ']/phys/domstats/temperature')

                print('{:<13} {:<8} {:<13} {:<13} {:<20} {:<13} {:<13} {:<13} {:<13} {:<20} {:<20} {:<20} {:<15}'
                      .format(host['dc'], host['leaf'], str(phy), speedDn.operSt, speedDn.operStQual, speedDn.operSpeed,
                              domTXDn.value, domRXDn.value, domTempDn.value, opticDn.guiName, opticDn.typeName,
                              opticDn.guiPN, opticDn.guiSN))
                continue


if __name__ == '__main__':
    # psuStatus(spineList)
    domStatus(hostList)

    # Use the connected moDir queries and configuration...
    md.logout()
