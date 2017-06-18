nethserver-freeradius
=====================

This module enables a MAC-based centralized authorization server for
you to control network access (i.e., what devices can connect the
network). In order for this to work, you must set and configure one or
more intermediate devices known as Network Access Server (NAS), then
connect users (also known as "supplicants") through them. Finally, you
must configure the centralized authorization server to accept
authorization requests sent from these NAS devices (e.g., access
points, smart switches, etc.). See [FreeRADIUS Technical
Guide](http://networkradius.com/doc/FreeRADIUS-Technical-Guide.pdf).

This module doesn't implement authentication, nor accounting right
now.

This module helps you reduce the configuration the centralized
authorization server needs but it doesn't help you configure NAS
devices in your network. So you must configure these devices yourself
before enjoy a successful centralized authorization infrastructure.

This package might be useful for system administrators from wireless
communities needing to control the network access of its users as well
as provide mobility to them.  For example, consider local wireless
communities made of Nano Station devices in which one line of these
devices is configured as access points and the rest of them as client
stations. The access points are also configured to validate MAC
addresses against a RADIUS authorization server running NethServer,
FreeRADIUS and this module.

Installation
------------

When installed, this package does the following:

* Install package dependencies (e.g., `freeradius`).

* Customize FreeRADIUS default configuration files (e.g.,
  `/etc/raddb/sites-available/default` and
  `/etc/raddb/mods-available/files`) so to turn it into a MAC-based
  authentication server, as described in
  https://wiki.freeradius.org/guide/Mac-Auth.

* Create FreeRADIUS link to NethServer configuration panel to manage
  NAS information (e.g., name, address, secret and desciption). Only
  NAS configured here will be able to send authorization request to
  the authentication sever.

* Create `radiusd` at configuration's default databases.

Configuration
-------------

In normal operation, the system administrator does the following:

1. Use NethServer FreeRADIUS module to configure what NAS will be able
   to interact with the authorization server. See
   `/etc/raddb/clients.conf` file.

2. Configure each NAS so as to send authorization request to the
   centralized authorization server (e.g., the system administrator
   must specify the authorization server IP, port number and related
   secret in each device intended to work as NAS).

3. Use NethServer DHCP module to reserve IP addresses and so, define
   what MAC will be authorized to access the network as well (i.e.,
   only the MAC address that has been reserved in NethServer DHCP
   module will have authorized network access by the authorization
   server). See `/etc/raddb/authorized_macs` file.

Bugs
----

This module is in a very raw stage and might sure have issues. One of
them is that MAC-based authorization doesn't provide too much security
by its own (e.g., unauthorized users can clone the MAC address of
authorized users and get network access as such). However, by doing
so, the module provides a start-base code (and, hopefully, some
motivation) for NethServer community to look forward sophisticated
FreeRADIUS integration features like EAP authentication and
accounting.

Please report your issues at
https://github.com/areguera/nethserver-freeradius/issues

Author
------

* Alain Reguera Delgado <alain.reguera@gmail.com>

References
----------

* http://freeradius.org/
