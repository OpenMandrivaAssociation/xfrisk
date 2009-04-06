%define    release      %mkrel 6
%define    version      1.2
%define    name         XFrisk
Summary: XFrisk, a multi-user network version of the classic "Risk"
Name: %{name}
Version: %{version}
Release: %{release}
Group: Games/Strategy
Source: http://www.iki.fi/morphy/xfrisk/%{name}-%{version}.tar.gz
Patch: XFrisk-mdk.patch.bz2
License: GPL
URL: http://www.iki.fi/morphy/xfrisk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: X11-devel
BuildRequires: Xaw3d-devel

%description
XFrisk a multi-user network version of the classic "Risk"

%prep
%setup -n XFrisk
%patch -p1 -b .mdk

%build
make PREFIX=/usr

%install
make PREFIX=${RPM_BUILD_ROOT}/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,games,games,-)
/usr/share/xfrisk/*
%{_bindir}/risk
%{_bindir}/xfrisk
%{_bindir}/friskserver
%{_bindir}/aiDummy
%{_bindir}/aiConway
%{_bindir}/aiColson
%doc BUGS
%doc COPYING
%doc ChangeLog
%doc FAQ
%doc README.NEW
%doc TODO


