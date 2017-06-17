=====================
nethserver-freeradius
=====================

This package provides FreeRADIUS integration to NethServer.  The
integration turns NethServer into a MAC-based centralized
authentication server, used to control users' network access through
Network Access Server (NAS) devices already configured to do so. No
other authentication is implemented by now.

This package might be useful for system administrators from wireless
communities needing to control the network access of its users as well
as provide mobility to them.

Installation
============

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
=============

In normal operation, the system administrator does the following:

1. Use NethServer FreeRADIUS module to configure what NAS will be able
   to interact with the authentication server. The results is
   reflected in `/etc/raddb/clients.conf` file.

1. Configure each NAS so as to send authorization request to the
   centralized authentication server (e.g., the system administrator
   must specify the central authentication server IP, port and related
   secret in each device intended to work as NAS).

1. Use NethServer DHCP module to reserve IP addresses and so, define
   what MAC will be authorized to access the network (i.e., only the
   MAC address that has been reserved in NethServer DHCP module
   will have authorized network access by the authentication server).

This integration is been tested with friends in a local wireless
community made of Nano Station devices. In this infrastructure, a line
of them is configured as access points and the rest of them as client
stations. The access points were also configured to validate MACs
against a RADIUS authentication server running NethServer with this
module.

Security
========

MAC-based authorization doesn't provide too much security by its own
(e.g., an unauthorized user can clone the MAC address of authorized
users and get network access as such). However, by doing so, the
module provides a start-base code (and, hopefully, needed motivation)
for NethServer community to look forward sophisticated FreeRADIUS
integration features like EAP authentication and accounting.

Bugs
====

Please report bugs to 
https://github.com/areguera/nethserver-freeradius

Author
======

* Alain Reguera Delgado <alain.reguera@gmail.com>

References
==========

* http://freeradius.org/
