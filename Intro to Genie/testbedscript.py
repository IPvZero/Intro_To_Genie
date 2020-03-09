# Python Script to Generate a Genie Testbed file for IOS VIRL images
# Substitute your own username and password
# Modify IP addresses and loop range as required

print("---")
print("testbed:")
print("\n  credentials:")
print("    default:")
print("      username: \"cisco\"")
print("      password: \"cisco\"")

print("\ndevices:")

for i in range(101, 108):
  print("  R" + str(i) + ":")
  print("    alias: R" + str(i))
  print("    os: iosxe")
  print("    type: csr1000v")
  print("    connections:")

  print("\n      defaults:")
  print("        class: unicon.Unicon")
  print("      console:")
  print("        protocol: ssh")
  print("        ip: 172.16.30." + str(i))
  print("\n    custom:")
  print("      abstraction:")
  print("         order: [os, type]\n")
