nethserver-freeradius
=====================

The FreeRADIUS panel allows you to control the network access (i.e.,
what devices can access the network). In order for this to work, you
must set and configure one or more intermediate authenticator devices
(also known as "Network Access Server" or simply "NAS") so for users
(also known as "supplicants") to connect to.  Finally, the centralized
"authentication server" must be configured to process access requests
sent from Authenticators. The correct coordination of all these
elements is also know as "RADIUS infrastructure."

The FreeRADIUS panel helps you to configure the authentication server
in an already running NethServer computer but it doesn't help you to
configure the authenticators devices nor the supplicants in your
network. That is something you must do first, before you can enjoy a
successful RADIUS infrastructure.

In normal operation, the system administrator does the following:

1. Use the authentication server tab in FreeRADIUS panel to configure
   how authenticators will allow supplicants to access the network.
   Possible options include MAC address, IEEE802.1X or a combination
   of them both. See `/etc/raddb/sites-available/default` file.

2. Use the authenticator tab in FreeRADIUS panel to define what
   authenticator devices (e.g., access points, smart switches) can
   send access requests to the authentication server. See
   `/etc/raddb/clients.conf` file.

3. Use the supplicants tab in FreeRADIUS panel to define the MAC
   address and credentials (i.e., username and password) final users
   must set in their devices (e.g., wireless stations) to access the
   network. See `/etc/raddb/authorized_macs` and `/etc/raddb/users`
   files.

In addition to these basic steps, the system administrator might also
do the following:

1. Configure authenticator devices (e.g., access points, smart
   switches) as authenticator of the authentication server (i.e., to
   accept authentication requests from supplicants and request access
   to the centralized authentication server based on them).

2. Configure supplicant devices (e.g., wireless stations) to send
   authentication requests to authenticator devices.

3. Communicate final users (e.g., using the e-mail system) the
   credentials they must use in order to access the network.

Installation
============

To install nethserver-freeradius package, run the following command
(as the root user):

```
yum --enablerepo=nethforge-testing install nethserver-freeradius
```

Use Case
========

This package might be useful for system administrators needing to
control the network access of its users as well as provide mobility to
them.  For example, consider local wireless communities made of
NanoStation devices in which one line of these devices is configured
as access points and the rest of them as client stations. The access
points, here, are configured as authenticators of a central
authentication server (running nethserver-freeradius).  The client
stations (supplicants) are configured to send access requests to the
authenticators using IEEE802.1X.

In this infrastructure:

1. The supplicant sends an Access-Request to the authenticator it
   connects to, using IEEE802.1X (e.g., EAP-MD5 or EAP-TTLS). The
   Access-Request includes the supplicant's MAC address as well as
   the "User-Name" and "User-Password" attributes.

2. The authenticator sends the Access-Request to the centralized
   authentication server.
   
3. The authentication server decides whether or not to accept the
   supplicant Access-Request and responds to the authenticator
   accordingly.
   
4. The authenticator enforces the authentication server decision to
   supplicant.

Bugs
====

https://github.com/areguera/nethserver-freeradius/issues

Author
======

* Alain Reguera Delgado <alain.reguera@gmail.com>

References
==========

* http://freeradius.org/
* http://networkradius.com/doc/FreeRADIUS-Technical-Guide.pdf
* https://wiki.freeradius.org/guide/Mac-Auth
