http://igoro.com/archive/gallery-of-processor-cache-effects/

this machine has an i7-4600U CPU
the size of the L1 data and instruction caches is 32kB
the size of the L2 and L3 unified caches are 256 and 4096kB respectively

	sudo dmidecode -t cache

	Getting SMBIOS data from sysfs.
	SMBIOS 2.7 present.

	Handle 0x0014, DMI type 7, 19 bytes
	Cache Information
			Socket Designation: L1 Cache
			Configuration: Enabled, Not Socketed, Level 1
			Operational Mode: Write Back
			Location: Internal
			Installed Size: 32 kB
			Maximum Size: 32 kB
			Supported SRAM Types:
					Asynchronous
			Installed SRAM Type: Asynchronous
			Speed: Unknown
			Error Correction Type: Parity
			System Type: Data
			Associativity: 8-way Set-associative

	Handle 0x0016, DMI type 7, 19 bytes
	Cache Information
			Socket Designation: L1 Cache
			Configuration: Enabled, Not Socketed, Level 1
			Operational Mode: Write Back
			Location: Internal
			Installed Size: 32 kB
			Maximum Size: 32 kB
			Supported SRAM Types:
					Asynchronous
			Installed SRAM Type: Asynchronous
			Speed: Unknown
			Error Correction Type: Parity
			System Type: Instruction
			Associativity: 8-way Set-associative

	Handle 0x0017, DMI type 7, 19 bytes
	Cache Information
			Socket Designation: L2 Cache
			Configuration: Enabled, Not Socketed, Level 2
			Operational Mode: Write Back
			Location: Internal
			Installed Size: 256 kB
			Maximum Size: 256 kB
			Supported SRAM Types:
					Asynchronous
			Installed SRAM Type: Asynchronous
			Speed: Unknown
			Error Correction Type: Single-bit ECC
			System Type: Unified
			Associativity: 8-way Set-associative

	Handle 0x0018, DMI type 7, 19 bytes
	Cache Information
			Socket Designation: L3 Cache
			Configuration: Enabled, Not Socketed, Level 3
			Operational Mode: Write Back
			Location: Internal
			Installed Size: 4096 kB
			Maximum Size: 4096 kB
			Supported SRAM Types:
					Asynchronous
			Installed SRAM Type: Asynchronous
			Speed: Unknown
			Error Correction Type: Multi-bit ECC
			System Type: Unified
			Associativity: 16-way Set-associative
