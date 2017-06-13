Name: nethserver-freeradius
Summary: FreeRADIUS integration in NethServer
Version: 0.0.1
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
authentication server. In normal operation, the system administrator
set IP reservations using NethServer DHCP to define what MAC addresses
will have access to both NethServer hosted services and the network.


%prep
%setup


%build
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
* Mon 12 Jun 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.1-1
- Initial commit 
