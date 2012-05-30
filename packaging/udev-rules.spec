%define udev_libdir /lib/udev
  
Summary: MeeGo udev Rules
Name: udev-rules
Version: 0.11
Release: 1
URL: http://www.meego.com
License: GPLv2
Group: System/Base
BuildArch: noarch
Source0: %{name}-%{version}.tar.bz2
Requires: udev
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd 
Obsoletes: moblin-udev-rules <= 0.1-4.1

%description
This package includes some meego specific udev rules, which express 
some of handles/actions for meego related udev event, such as 
USB aotususpend features from some tested device on top of meego
platform. 


%package netbook
Summary:    Netbook udev rules
Group: System/Base

%description netbook
Netbook udev rules

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
make -C netbook install DESTDIR=%{buildroot}

%post
systemctl daemon-reload
systemctl reload-or-try-restart udev.service
systemctl reload-or-try-restart udev-retry.service
systemctl reload-or-try-restart udev-settle.service

%preun
systemctl stop udev.service
systemctl stop udev-retry.service
systemctl stop udev-settle.service

%postun
systemctl daemon-reload

 
%clean
rm -rf %{buildroot}

%files netbook
%defattr(0644, root, root, 0755)
%attr(0644,root,root) %{udev_libdir}/rules.d/01-netbook.rules

