=====================
nethserver-freeradius
=====================

This package provides FreeRADIUS integration to NethServer.  The
integration turns NethServer into a MAC-based centralized
authentication server. In normal operation, the system administrator
set IP reservations using NethServer DHCP to define what MAC addresses
will have access to both NethServer hosted services and the network.

This package takes the MACs of reserved IPs in NethServer, builds the
list of MAC addresses authorized to access the network and finally
reloads the FreeRADIUS daemon for changes to take effect.

This package might be useful for wireless communities that need to
control the network access of its users as well as provide mobility to
them.

Installation
============

When installed, the package does the following:

* Install `freeradius` package from CentOS base repository

* Install customized configuration files so to turn NethServer
  into a MAC-based authentication server.

* Add FreeRADIUS entry in NethServer Configuration panel to define
  basic configuration stuff (e.g., NAS)

Configuration
=============

The system administrator must use NethServer configuration tools
(e.g., the `config` command) to set the address and secret of each
Network Access Server (NAS) that will be used in the network. Then
configure the NAS to interact with the FreeRADIUS server. The rest of
this section describes the options used to control FreeRADIUS
configuration and the commands you can run to customize them.

* *radiusd* -- Configuration database under which FreeRADIUS
  configuration is stored in. Use the command `config radiusd keys` to
  print a list of all configuration keys supported.

** *NAS*

Bugs
====


Author
======

* Alain Reguera Delgado <alain.reguera@gmail.com>

References
==========

* https://wiki.freeradius.org/guide/Mac-Auth
* http://freeradius.org/doc/
