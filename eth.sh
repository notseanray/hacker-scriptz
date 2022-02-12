#!/bin/bash
if [[ $(expr length "$1") = 0 ]]; then
	interface="enp27s0"
else
	interface=$1
fi

echo "setting up: $interface"
ifconfig $1 up
ifconfig $1 192.168.1.93 broadcast 255.255.255.0 netmask 255.255.255.0 up
route add default gw 192.168.1.254
echo 1 > /proc/sys/net/ipv6/conf/default/disable_ipv6
echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6
notify-send "$interface connected"
