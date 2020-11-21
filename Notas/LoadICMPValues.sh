#!/bin/bash


parsed=$(cat PortalVPN.txt | awk '{print $4,$6,$8}' | awk -F'icmp_seq=' '{print $1,$2,$3}' | awk -F'time=' '{print $1,$2}' | grep -vi of | grep -vi "^ " )
host=$(($parsed | head -n1 | awk '{print \t$1}' ))
seq=$(($parsed | head -n1 | awk '{print \t$2}' ))

while [[ $seq -gt 0 ]]
do
	RTT=$(($parsed | awk '{ if (\t$2 == $seq) print \t$3}'))

	mysql -A -uroot --password='Claro123!' -DICMP -e "INSERT INTO VPNSSL VALUES ($host,$seq,$RTT)"

	seq=$(($seq+ 1))

done


	
