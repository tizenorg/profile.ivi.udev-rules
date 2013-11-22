%define udev_libdir /usr/lib/udev
  
Summary: Tizen IVI udev Rules
Name: udev-rules
Version: 0.11
Release: 1
License: GPL-2.0
Group: Automotive/Hardware Adaptation
BuildArch: noarch
Source0: %{name}-%{version}.tar.bz2

%description
This package includes some profile specific udev rules, which express
some of handles/actions for Tizen-related udev events. 

%package ivi
Summary: IVI udev rules

%description ivi
This package installs udev rules that are specific to IVI profile

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
make -C ivi install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files ivi
%defattr(0644, root, root, 0755)
%attr(0644,root,root) %{udev_libdir}/rules.d/99-atkbd.rules
