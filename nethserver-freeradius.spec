Name: nethserver-freeradius
Summary: FreeRADIUS integration in NethServer
Version: 0.0.5
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

Requires: freeradius >= 3.0.4
# NethServer dependencies.

%description
This package provides integration for FreeRADIUS in NethServer. It
turns your server into a centralized network authentication server, so
you can easily control what devices can access the network. The
authentication server is prepared to control network access using MAC
address, IEEE802.1X or both.

The authentication server provided by this package is only one
component of the three elements a RADIUS infrastructure is made of.
The other two elements (the authenticator and the supplicant) are not
configured by this package.  That is something you must do first,
before you can enjoy a successful RADIUS infrastructure.

%prep
%setup


%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist


%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc LICENSE README.rst
%dir %{_nseventsdir}/%{name}-update


%changelog
* Sat Jul 22 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.5-1
- Fix radiusd (authorized_macs) start-up issue
- Add credit to Davide Principi as author
- Update online documentation (small fixes)
- Fix contradiction in README.rst

* Sun Jul 9 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.4-1
- Add new tab dedicated to authentication server
- Add new tab dedicated to supplicants
- Update radiusd configuration based on supplicants database
- Update authorized_macs based on supplicants database instead of hosts database
- Update online documentation
- Update configuration file permissions
- Update header using lower-case words
- Update server authentication to use both MAC address and IEEE802.1X
- Use Authenticators tab name instead of just NAS

* Fri Jun 30 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.3-1
- Add access to radiusd default NethServer config
- Add UDPPorts to radiusd default NethServer config
- Fix pam-related radiusd failure at start-up

* Sat Jun 24 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.2-1
- Update createlinks file to initialize default databases

* Wed Jun 21 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.1-2
- Add makedocs macro to build section

* Mon Jun 19 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.1-1
- Initial build
