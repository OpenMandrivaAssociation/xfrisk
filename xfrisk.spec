Summary: A multi-user network version of the classic "Risk"
Name: xfrisk
Version: 1.2
Release: 13
Group: Games/Strategy
Source: http://www.iki.fi/morphy/xfrisk/XFrisk-%{version}.tar.gz
Patch0: XFrisk-mdk.patch
Patch1: XFrisk-1.2-fix-str-fmt.patch
License: GPL
URL: https://www.iki.fi/morphy/xfrisk
BuildRequires: pkgconfig(x11)
BuildRequires: Xaw3d-devel
BuildRequires: pkgconfig(xaw7)
BuildRequires: pkgconfig(xt)
Obsoletes: XFrisk < %{version}-%{release}
Provides: XFrisk = %{version}-%{release}

%description
XFrisk a multi-user network version of the classic "Risk"

%prep
%setup -qn XFrisk
%patch0 -p1 -b .mdk
%patch1 -p0 -b .str

%build
make PREFIX=%{_prefix} CC="gcc %{optflags}" LDFLAGS="%{?ldflags}"

%install
make PREFIX=%{buildroot}%{_prefix} install

mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF >%{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=XFrisk
Comment=A multi-user network version of the classic "Risk"
Exec=%{_bindir}/risk
Icon=strategy_section
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%clean

%files
%defattr(-,games,games,-)
%{_datadir}/xfrisk
%{_bindir}/risk
%{_bindir}/xfrisk
%{_bindir}/friskserver
%{_bindir}/aiDummy
%{_bindir}/aiConway
%{_bindir}/aiColson
%{_datadir}/applications/mandriva-%{name}.desktop
%doc BUGS
%doc ChangeLog
%doc FAQ
%doc README.NEW
%doc TODO


%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.2-10mdv2011.0
+ Revision: 634901
- simplify BR

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 1.2-9mdv2010.0
+ Revision: 446159
- rebuild

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 1.2-8mdv2009.1
+ Revision: 364358
- fix binary name
- add desktop item
- fix str fmt
- unzip the patch
- rename to lowercase

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.2-6mdv2009.0
+ Revision: 262431
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.2-5mdv2009.0
+ Revision: 257063
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.2-3mdv2008.1
+ Revision: 136605
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import XFrisk


* Wed Mar 08 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.2-3mdk
- Fix BuildRequires

* Fri Jul 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.2-2mdk
- Fix BuildRequires

* Wed Mar 16 2005 Bruno Cornec <bcornec@mandrakesoft.org> 1.2-1mdk
- First version
