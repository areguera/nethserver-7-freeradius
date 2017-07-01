Name: nethserver-freeradius
Summary: FreeRADIUS integration in NethServer
Version: 0.0.3
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

Requires: freeradius >= 3.0.4
# NethServer dependencies.

%description
This package provides FreeRADIUS integration to NethServer.  The
integration turns NethServer into a MAC-based centralized
authorization server for your network. In normal operation, the system
administrator uses NethServer DHCP module to reserve IP addresses and
so, define what MACs will be authorized to access the network.

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
* Fri 30 Jun 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.3-1
- Add access to radiusd default NethServer config
- Add UDPPorts to radiusd default NethServer config
- Fix pam-related radiusd failure at start-up

* Sat Jun 24 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.2-1
- Update createlinks file to initialize default databases

* Wed Jun 21 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.1-2
- Add makedocs macro to build section

* Mon Jun 19 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.1-1
- Initial commit
