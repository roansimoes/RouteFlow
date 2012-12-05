MONGO_ADDRESS = "192.169.1.1:27017"
MONGO_DB_NAME = "db"

RFCLIENT_RFSERVER_CHANNEL = "rfclient<->rfserver"
RFSERVER_RFPROXY_CHANNEL = "rfserver<->rfproxy"

RFTABLE_NAME = "rftable"
RFCONFIG_NAME = "rfconfig"

RFSERVER_ID = "rfserver"
RFPROXY_ID = "rfproxy"

DEFAULT_RFCLIENT_INTERFACE = "eth0"

RFVS_DPID = 0x7266767372667673

RF_ETH_PROTO = 0x0A0A # RF ethernet protocol

VLAN_HEADER_LEN = 4
ETH_HEADER_LEN = 14
ETH_CRC_LEN = 4
ETH_PAYLOAD_MAX = 1500
ETH_TOTAL_MAX = (ETH_HEADER_LEN + ETH_PAYLOAD_MAX + ETH_CRC_LEN)
RF_MAX_PACKET_SIZE = (VLAN_HEADER_LEN + ETH_TOTAL_MAX)

MATCH_L2 = True

DC_DROP_ALL = 0			# Drop all incoming packets
DC_CLEAR_FLOW_TABLE = 1 # Clear flow table
DC_VM_INFO = 2			# Flow to communicate two linked VMs
DC_RIPV2 = 3			# RIPv2 protocol
DC_OSPF = 4			# OSPF protocol
DC_BGP_PASSIVE = 5		# BGP protocol
DC_BGP_ACTIVE = 6		# BGP protocol
DC_ARP = 7			# ARP protocol
DC_ICMP = 8			# ICMP protocol
DC_ALL = 9				# Send all traffic to the controller

PC_MAP = 0
PC_RESET = 1

# Format 12-digit hex ID
format_id = lambda dp_id: hex(dp_id).rstrip("L")
