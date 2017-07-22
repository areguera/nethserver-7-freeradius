Name: nethserver-freeradius
Summary: FreeRADIUS integration in NethServer
Version: 0.0.6
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

Requires: freeradius >= 2.2.6


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
* Sat Jul 22 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.6-1
- Update README.rst
- Add authorized_macs configuration file
- Add configuration templates metadata
- Add PolicyMAC and PolicyIEEE8021X default config
- Add raddb users configuration template
- Update NethServer module, help, language, template
- Update raddb configuration templates
- Remove host create, delete and modify events

* Sat Jul 1 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.5-1
- Fix radiusd network service availability

* Sun Jun 25 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.4-1
- Fix path in createlinks files

* Sun Jun 25 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.3-1
- Fix call to rewrite.calling_station_id

* Sat Jun 24 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.2-1
- Update createlinks file to initialize default databases

* Wed Jun 21 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.1-2
- Add makedocs macro to build section

* Mon Jun 19 2017 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.1-1
- Initial commit
