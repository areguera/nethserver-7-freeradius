==========
FreeRADIUS
==========

This module enables a MAC-based centralized authorization server for
you to control network access (i.e., what devices can connect the
network). In order for this to work, you must set and configure one or
more intermediate devices known as Network Access Server (NAS) for
users (also known as "supplicants") to connect to. Finally, you must
configure configure the centralized authorization server to accept
authorization requests sent from these devices (e.g., access points,
smart switches, etc.).

This module helps you reduce the configuration the centralized
authorization server needs but it doesn't help you configure NAS
devices in your network. So you must configure these devices yourself
before enjoy a successful centralized authorization infrastructure.

This module implements MAC-based authorization only. It doesn't
implement authentication, nor accounting.

In normal operation, the system administrator does the following:

1. Use NethServer FreeRADIUS module to configure what NAS will be able
   to interact with the authorization server. See
   `/etc/raddb/clients.conf` file.

1. Configure each NAS so as to send authorization request to the
   centralized authorization server (e.g., the system administrator
   must specify the authorization server IP, port number and related
   secret in each device intended to work as NAS).

1. Use NethServer DHCP module to reserve IP addresses and so, define
   what MAC will be authorized to access the network as well (i.e.,
   only the MAC address that has been reserved in NethServer DHCP
   module will have authorized network access by the authorization
   server). See `/etc/raddb/authorized_macs` file.

For example, consider local wireless communities made of Nano Station
devices in which one line of these devices is configured as access
points and the rest of them as client stations. The access points are
also configured to validate MAC addresses against a RADIUS
authorization server running NethServer, FreeRADIUS and this module.

NAS
===

This tab controls what NAS (e.g., access points, smart switches) are
allowed to communicate with the central authorization server.

Name
    The name used to identify the NAS.

IP Address
    The IP address the NAS responds to. This is the IP address of the
    access point or smart switch you configured as NAS.

Secret
    An arbitrary text used to secure the NAS. This information must be
    the same in both the central authorization server and the NAS so
    they can exchange messages.

Description
    An arbitrary text used to describe the NAS (e.g., its purpose).
