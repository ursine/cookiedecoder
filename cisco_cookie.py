#!/usr/bin/env python

import fileinput
from collections import deque

# Decode a cookie passed in via stdin
sjoin = ''.join([''.join(x.split()) for x in fileinput.input()])
thout = deque([int(sjoin[i:i+2],16) for i in xrange(0,len(sjoin),2)])

print "ID PROM Version    (0x04): 0x%x" % thout.popleft()
print "Compatibility Byte (0xff): 0x%x" % thout.popleft()
print "MAC Address Type   (0xc3): 0x%x" % thout.popleft()

maclen = thout.popleft()
print "MAC Address Length (0x06): 0x%x" % maclen

#bytes 0x04-0x09 MAC Address: 00 18 73 6d ad db
#bytes 0x0a MAC Address Block Size Type (0x43): 43
#bytes 0x0b-0x0c MAC Address Block Size: 00 0a
#bytes 0x0d PCB Serial Number Type (0xc1): c1
#bytes 0x0e PCB Serial Number Length (0x8b): 8b
#bytes 0x0f-0x19 PCB Serial Number: 46 4f 43 30 39 34 38 31 34 4c 53 > Label SN: FOC094814LS
#byte 0x1a Controller Type Type (0x40): 40
#byte 0x1b Controller Type High Byte: 04
#byte 0x1c Controller Type Low Byte: b5
#byte 0x1d Hardware Version Type (0x41): 41
#byte 0x1e Hardware Version High Byte (0x01): 01
#byte 0x1f Hardware Version Low Byte (0x00): 00
#byte 0x20 73-level PCB PN Type (0x82): 82
#byte 0x21-0x24 73-level PCB PN: 4a 0d ad 02
#bytes 0x25 PCB Revision Type (0x42): 42
#bytes 0x26-0x27 PCB Revision (0x3031): 30 31
#bytes 0x28 800 Level PCB PN Type (0xc0): c0
#bytes 0x29 800 Level PCB PN Length (0x46): 46
#bytes 0x2a-0x2f 800 Level PCB PN (0x032000303901): 03 20 00 30 39 01
#bytes 0x30 Deviation Number Type (0x88): 88
#bytes 0x31-0x34 Deviation Number (0x00000000): 00 00 00 00
#bytes 0x35 PCB Fab Version type (0x02): 02
#bytes 0x36 PCB Fab Version (0x01): 01
#bytes 0x37 CLEI Code Type (0xc6): c6
#bytes 0x38 CLEI Code Length (0x8a): 8a
#bytes 0x39-0x42 CLEI Code (0x49504d45443030425241): 49 50 4d 45 44 30 30 42 52 41
#bytes 0x43 RMA Test History Type (0x03): 03
#bytes 0x44 RMA Test History (0x00): 00
#bytes 0x45 RMA Number Type (0x81): 81
#bytes 0x46-0x49 RMA Number (0x00000000): 00 00 00 00
#bytes 0x4a RMA History Type (0x04): 04
#bytes 0x4b RMA History (0x00): 00
#bytes 0x4c Product Identifier PID Type (0xcb): cb
#bytes 0x4d Product Identifier PID Length (0x94): 94
#bytes 0x4e-0x61 Product Identifier PID: 43 49 53 43 4f 38 37 37 2d 4b 39 20 20 20 20 20 20 20 20 20
#bytes 0x62 Version Identifier VID Type (0x89): 89
#bytes 0x63-0x66 Version Identifier VID: 56 30 31 20
#bytes 0x67 Digital Signature List Type: d9
#bytes 0x68 Digital Signature List Length: 02
#bytes 0x69-0x6a Digital Signature List: 40 c1
#bytes 0x6b processor type type (0x09): 09
#bytes 0x6c processor type cpu id: 94
#bytes 0x6d Chassis Serial Number Type (0xc2): c2
#bytes 0x6e Chassis Serial Number Length (0x8b): 8b
#bytes 0x6f-0x79 Chassis Serial Number: 46 48 4b 30 39 35 31 32 30 42 55 > Label FHK095120BU at the router back.
#bytes 0x7a Radio Country Code Type (0x4a): 4a
#bytes 0x7b-0x7c Radio Country Code: ff ff
#bytes 0x7d-0x7f: ff ff ff


