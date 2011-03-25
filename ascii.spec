Name:		ascii
Version:	3.11
Release:	%mkrel 1
URL:		http://www.catb.org/~esr/ascii/
Source0:	http://www.catb.org/~esr/ascii/%name-%version.tar.gz
License:	GPLv2+
Group:		Text tools
Summary:	Interactive ASCII name and synonym chart
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
mkdir -p %buildroot/%{_bindir}
mkdir -p %buildroot/%{_mandir}/man1/
cp ascii %buildroot/%{_bindir}
cp ascii.1 %buildroot/%{_mandir}/man1/

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README COPYING
%{_mandir}/man1/ascii.1*
%{_bindir}/ascii
