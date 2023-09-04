# #!/bin/bash

# # set the MAC address of the device to search for
# DEVICE_MAC_ADDRESS="04:29:2E:B7:7E:50"

# # run bluetoothctl in the background and connect to its standard input/output
# bluetoothctl &>/dev/null << EOF
# # enter the bluetoothctl interactive prompt
#   connect $DEVICE_MAC_ADDRESS
#   # wait for the device to be found
#   wait $DEVICE_MAC_ADDRESS
#   # pair with the device
#   pair $DEVICE_MAC_ADDRESS
#   # trust the device
#   trust $DEVICE_MAC_ADDRESS
#   # connect to the device
#   connect $DEVICE_MAC_ADDRESS
# EOF

#!/usr/bin/expect -f
# Bluetooth seems to get messed up after dual booting
# Winblows for gaming... This script resets my bluetooth

set prompt "#"
set address [lindex $argv 0]

spawn bluetoothctl
expect -re $prompt
send "scan on\r"
send_user "\nWaiting for device.\r"
# I thought I could rely on this expect to make sure the device is discovered and ready
# It finds it, but this still isn't good enough... I still need a sleep
expect -re "\\\[NEW\\\] Device $address"
send_user "\nFound deivce.\r"
sleep 5
send "remove $address\r"
sleep 2
expect -re $prompt
send "pair $address\r"
sleep 2
send "connect $address\r"
sleep 3
send "trust $address\r"
sleep 2
send_user "\n$address should be paired now.\r"
send "scan off\r"
send "quit\r"
expect eof