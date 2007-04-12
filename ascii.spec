%define release %mkrel 2
%define version 3.8

Name: ascii
Version: %version
Release: %release
URL: http://www.catb.org/~esr/ascii/
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Text tools
Summary: Interactive ASCII name and synonym chart
BuildRoot: %{_tmppath}/%{name}-root

%description
The ascii utility provides easy conversion between various byte representations
and the American Standard Code for Information Interchange (ASCII) character
table.  It knows about a wide variety of hex, binary, octal, Teletype mnemonic,
ISO/ECMA code point, slang names, XML entity names, and other representations.
Given any one on the command line, it will try to display all others.  Called
with no arguments it displays a handy small ASCII chart.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS" ascii ascii.1

%install
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"%{_bindir}
mkdir -p "$RPM_BUILD_ROOT"%{_mandir}/man1/
cp ascii "$RPM_BUILD_ROOT"%{_bindir}
cp ascii.1 "$RPM_BUILD_ROOT"%{_mandir}/man1/

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README COPYING
%{_mandir}/man1/ascii.1*
%{_bindir}/ascii


