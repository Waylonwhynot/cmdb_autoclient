res = """
SMBIOS 2.7 present.

Handle 0x0001, DMI type 1, 27 bytes
System Information
	Manufacturer: Parallels Software International Inc.
	Product Name: Parallels Virtual Platform
	Version: None
	Serial Number: Parallels-1A 1B CB 3B 64 66 4B 13 86 B0 86 FF 7E 2B 20 30
	UUID: 3BCB1B1A-6664-134B-86B0-86FF7E2B2030
	Wake-up Type: Power Switch
	SKU Number: Undefined
	Family: Parallels VM
"""
"""
result = {
  'manufacturer': 'Parallels Software International Inc.',
  'product_name': 'Parallels Virtual Platform',
  'sn': 'Parallels-1A 1B CB 3B 64 66 4B 13 86 B0 86 FF 7E 2B 20 30'
}
"""

key_map = {
    "Manufacturer": 'manufacturer',
    "Product Name": 'product_name',
    "Serial Number": 'sn'
}

result = {}

data = res.strip().split('\n')

for k in data:
    v = k.strip().split(':')
    if len(v) == 2:
        if v[0] in key_map:
            result[key_map[v[0]]] = v[1].strip()
print(result)