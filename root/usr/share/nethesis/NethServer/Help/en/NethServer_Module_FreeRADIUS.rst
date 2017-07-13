==========
FreeRADIUS
==========

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

Authentication Server
=====================

The authentication server tab in FreeRADIUS panel implements one of
the following possible configurations:

MAC address::
    Authenticators must verify MAC address before allow network access.

Username and password (IEEE802.1X)::
    Authenticators must verify username and password before alow
    network access.

MAC address + username and password (IEEE802.1X)::
    Authenticators must verify both MAC address and credentials (i.e.,
    username and password) before allow network access.

None::
    Authenticators rejects network access.

The authentication server stores passwords using a clear-text format
in the `/etc/raddb/users` file, so as to validate users requesting
network access through IEEE802.1X protocol.  It is necessary for
supplicants to secure the communication channel before transmitting
their credentials over the wire (e.g., using protocols like EAP-TTLS
and EAP-PEAP). In the authentication server, the `/etc/raddb/users` is
a symbolic link to `/etc/raddb/mods-config/files/authorize` which can
be read only by users in the *radiusd* group and the *root* user
itself.

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

The Supplicants tab in the FreeRADIUS panel defines what devices the
final users can use to access the network. This tab relates the
following information:

MAC address::
    Contains authorized MAC address to access the network.

Username::
    Contains authorized username to access the network.

Password::
    Contains authorized password to access the network.

Description::
    Contains an arbitrary string describing the device used to access
    the network (e.g., its propietary, location, etc.).
