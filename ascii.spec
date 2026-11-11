Name:		ascii
Version:	3.33
Release:	1
URL:		https://gitlab.com/esr/ascii
Source0:	%{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
License:	BSD-2-Clause
Group:		Text tools
Summary:	Interactive ASCII name and synonym chart
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:	asciidoctor
BuildRequires:	make
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
%make_build CFLAGS="$RPM_OPT_FLAGS" ascii ascii.1

%install
mkdir -p %buildroot/%{_bindir}
mkdir -p %buildroot/%{_mandir}/man1/
install -m755 ascii -D %{buildroot}%{_bindir}/ascii
install -m644 ascii.1 -D %{buildroot}%{_mandir}/man1/ascii.1

%files
%defattr(-,root,root)
%doc README.adoc
%license COPYING
%{_mandir}/man1/ascii.1*
%{_bindir}/ascii
