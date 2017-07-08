==========
FreeRADIUS
==========

The FreeRADIUS panel allows you to control network access (i.e., what
devices can access the network). In order for this to work, you must
set and configure one or more intermediate authenticator devices (also
known as "Network Access Server" or simply "NAS") so for users (also
known as "supplicants") to connect to.  Finally, the centralized
authentication server must be configured to process access requests
sent from Authenticators.

The FreeRADIUS panel helps you to configure the authentication server
but it doesn't help you to configure the authenticator devices nor the
supplicants in your network. So you must configure these devices
yourself before enjoy a successful RADIUS infrastructure.

In normal operation, the system administrator does the following:

1. Use the authentication server tab in FreeRADIUS panel to configure
   how users devices get network access. Possible options include MAC
   address, IEEE802.1X or a combination of them both. See
   `/etc/raddb/sites-available/default` file.

2. Use the authenticator tab in FreeRADIUS panel to define what
   devices (e.g., access points, smart switches) can send access
   requests to the authentication server. See
   `/etc/raddb/clients.conf` file.

3. Configure network devices (e.g., access points, smart switches) as
   authenticator of the authentication server.

Based on the type of network access chosen, the system administrator
also does the following complementary tasks:

1. Manage MAC reservation in "DHCP" panel. Only reserved MAC address
   can access the network. See `/etc/raddb/authorized_macs` file.

2. Manage user credentials (i.e., username and passwords) in "User and
   Groups" panel. Only active users can access the network.  See
   `/etc/raddb/users` file.

Authentication Server
=====================

The authentication server tab in FreeRADIUS panel implements one of
the following possible configurations:

MAC address::
    Authenticators must verify MAC address before allow network access.

Username and password (IEEE802.1X)::
    Authenticators must verify username and password before alow
    network access.

MAC address and username and password (IEEE802.1X)::
    Authenticators must verify both MAC address and credentials (i.e.,
    username and password) before allow network access.

None::
    Authenticators must reject network access.

The authentication server uses the Pluggable Authentication Modules
(PAM) internally (see `/etc/raddb/users`) to validate the users
requesting network access.

Authenticators
==============

The Authenticators tab in FreeRADIUS panel defines what devices (e.g.,
access points, smart switches) will be Authenticators in the RADIUS
infrastructure (i.e., intermediate devices between Supplicant and
Authentication Server). The Authenticator requires authentication from
Supplicant and communicate with Authentication Server to determine
whether to accept or reject the network access to Supplicant.

Name::
    Contains a string identifying the Authenticator originating the
    access request. It MUST NOT be used to select the shared
    secret used to authenticate the request.

IP Address::
    Indicates the identifying IP Address of the Authenticator which is
    requesting authentication of the user, and SHOULD be unique to the
    Authenticator within the scope of the Authentication Server. Note
    that IP Address MUST NOT be used to select the shared secret used
    to authenticate the request.

Secret::
    Password shared between the Authenticator and the Authentication
    Server. It should be at least as large and unguessable as a well
    chosen password.  It is preferred that the secret be at least 16
    octets.  This is to ensure a sufficiently large range for the
    secret to provide protection against exhaustive search attacks.
    The secret MUST NOT be empty (length 0) since this would allow
    packets to be trivially forged.

Description::
    Contains an arbitrary string describing the Authenticator (e.g.,
    its purpose).

Supplicant
==========

...

Report Bugs
===========

Please report bugs to
https://github.com/areguera/nethserver-freeradius/issues/
