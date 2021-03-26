# ---------------------------------------------------------------------------------------------------------------#
# host[] is a list of dictionaries containing the following key value pairs for each host
    # dc: datacenter identifier
    # leaf: aci fabric node_id
    # ip: ip_address for mgmt access of the given node
    # numPhyInt: number of physical interfaces on the node
# ---------------------------------------------------------------------------------------------------------------#

# Fortrust ACI Node List
hostListDNV = [
    {'dc': 'FTST', 'leaf': '101', 'model': '93180', 'ip': '10.231.201.31', 'numPhyInt': '36'},
    {'dc': 'FTST', 'leaf': '102', 'model': '93180', 'ip': '10.231.201.32', 'numPhyInt': '36'},
    {'dc': 'FTST', 'leaf': '1101', 'model': '93180', 'ip': '10.231.201.41', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1102', 'model': '93180', 'ip': '10.231.201.42', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1103', 'model': '93180', 'ip': '10.231.201.43', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1104', 'model': '93180', 'ip': '10.231.201.44', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1201', 'model': '93180', 'ip': '10.231.201.45', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1202', 'model': '93180', 'ip': '10.231.201.46', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1203', 'model': '93180', 'ip': '10.231.201.47', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1204', 'model': '93180', 'ip': '10.231.201.48', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1205', 'model': '93180', 'ip': '10.231.201.49', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1206', 'model': '93180', 'ip': '10.231.201.50', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1207', 'model': '93180', 'ip': '10.231.201.51', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1208', 'model': '93180', 'ip': '10.231.201.52', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1209', 'model': '93180', 'ip': '10.231.201.53', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1210', 'model': '93180', 'ip': '10.231.201.54', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1298', 'model': '9348', 'ip': '10.231.201.55', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1299', 'model': '9348', 'ip': '10.231.201.56', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1301', 'model': '93180', 'ip': '10.231.201.57', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1302', 'model': '93180', 'ip': '10.231.201.58', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1303', 'model': '93180', 'ip': '10.231.201.61', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1304', 'model': '93180', 'ip': '10.231.201.62', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1401', 'model': '93180', 'ip': '10.231.201.59', 'numPhyInt': '54'},
    {'dc': 'FTST', 'leaf': '1402', 'model': '93180', 'ip': '10.231.201.60', 'numPhyInt': '54'}
]

# Q93 ACI Node List
hostListCGY = [
    {'dc': 'Q93', 'leaf': '101', 'model': '93180', 'ip': '10.54.201.41', 'numPhyInt': '36'},
    {'dc': 'Q93', 'leaf': '102', 'model': '93180', 'ip': '10.54.201.42', 'numPhyInt': '36'},
    {'dc': 'Q93', 'leaf': '1101', 'model': '93180', 'ip': '10.54.201.51', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1102', 'model': '93180', 'ip': '10.54.201.52', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1103', 'model': '9348', 'ip': '10.54.201.53', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1104', 'model': '9348', 'ip': '10.54.201.54', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1105', 'model': '93180', 'ip': '10.54.201.55', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1106', 'model': '93180', 'ip': '10.54.201.56', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1107', 'model': '9348', 'ip': '10.54.201.57', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1108', 'model': '9348', 'ip': '10.54.201.58', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1201', 'model': '93180', 'ip': '10.54.201.77', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1202', 'model': '93180', 'ip': '10.54.201.78', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1301', 'model': '9348', 'ip': '10.54.201.49', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1302', 'model': '9348', 'ip': '10.54.201.50', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1401', 'model': '93180', 'ip': '10.54.201.41', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1402', 'model': '93180', 'ip': '10.54.201.42', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1501', 'model': '93180', 'ip': '10.54.201.47', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1502', 'model': '93180', 'ip': '10.54.201.48', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1601', 'model': '93180', 'ip': '10.54.201.91', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1602', 'model': '93180', 'ip': '10.54.201.92', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1603', 'model': '9348', 'ip': '10.54.201.93', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1604', 'model': '9348', 'ip': '10.54.201.94', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1605', 'model': '9348', 'ip': '10.54.201.95', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1606', 'model': '9348', 'ip': '10.54.201.96', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1607', 'model': '9348', 'ip': '10.54.201.97', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1608', 'model': '9348', 'ip': '10.54.201.98', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1701', 'model': '9348', 'ip': '10.54.201.37', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1702', 'model': '9348', 'ip': '10.54.201.38', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1703', 'model': '9348', 'ip': '10.54.201.39', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1704', 'model': '9348', 'ip': '10.54.201.40', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1705', 'model': '93180', 'ip': '10.54.201.45', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1706', 'model': '93180', 'ip': '10.54.201.46', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1801', 'model': '93180', 'ip': '10.54.201.61', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1802', 'model': '93180', 'ip': '10.54.201.82', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1803', 'model': '9348', 'ip': '10.54.201.83', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '1804', 'model': '9348', 'ip': '10.54.201.84', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '2201', 'model': '93180', 'ip': '10.54.201.59', 'numPhyInt': '54'},
    {'dc': 'Q93', 'leaf': '2202', 'model': '93180', 'ip': '10.54.201.60', 'numPhyInt': '54'}
]
