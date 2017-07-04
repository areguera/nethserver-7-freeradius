==========
FreeRADIUS
==========

This module enables a MAC-based centralized authorization server for
you to control network access (i.e., what devices can connect the
network). In order for this to work, you must set and configure one or
more intermediate authenticator device (also known as "Network Access
Server" or simply "NAS") for users (also known as "supplicants") to
connect to.  Finally, the centralized authentication server must be
configured to accept authorization requests sent from authenticators.

This module helps you reduce the configuration the centralized
authentication server needs but it doesn't help you configure
authenticator devices in your network. So you must configure these
devices yourself before enjoy a successful MAC-based centralized
authorization infrastructure.

This module implements MAC-based authorization only. It doesn't
implement authentication, nor accounting.

In normal operation, the system administrator does the following:

1. Configure each authenticator device so as to send authorization
   request to the centralized authentication server (e.g., the system
   administrator must specify the authorization server IP, port number
   and related secret in each device intended to work as
   authenticator).

1. Use NethServer FreeRADIUS module to configure what authenticator
   will be able to interact with the authentication server. See
   `/etc/raddb/clients.conf` file.

1. Use NethServer DHCP module to reserve IP addresses and so, define
   what MAC will be authorized to access the network (i.e., only the
   MAC address that has been reserved in NethServer DHCP module will
   have authorized network access by the authentication server). See
   `/etc/raddb/authorized_macs` file.

Authenticators
==============

This tab controls what devices (e.g., access points, smart switches)
will be used as gateway between the users (supplicants) and the
centralized authentication server.

Name
    The name used to identify the authentication device.

IP Address
    The IP address the authentication device responds to. This is the
    IP address of the access point or smart switch you configured as
    authenticator.

Secret
    An arbitrary text used to secure the authenticator device. This
    information must be the same in both the central authentication
    server and the authenticator device so they can exchange messages.

Description
    An arbitrary text used to describe the authentication device
    (e.g., its purpose).
