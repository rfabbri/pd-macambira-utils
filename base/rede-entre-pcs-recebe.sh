#controla
#sudo ifconfig eth0 192.168.1.10
#sudo route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.11 eth0
#ping 192.168.1.11

#manda
sudo ifconfig eth0 192.168.1.11 up
sudo route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.10 eth0
ping 192.168.1.10


