Summary: XFrisk, a multi-user network version of the classic "Risk"
Name: xfrisk
Version: 1.2
Release: %mkrel 7
Group: Games/Strategy
Source: http://www.iki.fi/morphy/xfrisk/XFrisk-%{version}.tar.gz
Patch0: XFrisk-mdk.patch
Patch1: XFrisk-1.2-fix-str-fmt.patch
License: GPL
URL: http://www.iki.fi/morphy/xfrisk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: X11-devel
BuildRequires: Xaw3d-devel
Obsoletes: XFrisk < %version-%release
Provides: XFrisk = %version-%release

%description
XFrisk a multi-user network version of the classic "Risk"

%prep
%setup -qn XFrisk
%patch0 -p1 -b .mdk
%patch1 -p0 -b .str

%build
make PREFIX=%_prefix CC="gcc %{optflags}" LDFLAGS="%{?ldflags}"

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=%buildroot%_prefix install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,games,games,-)
%{_datadir}/xfrisk
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


