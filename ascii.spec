Name:		ascii
Version:	3.11
Release:	3
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
mkdir -p %buildroot/%{_bindir}
mkdir -p %buildroot/%{_mandir}/man1/
install -m755 ascii -D %{buildroot}%{_bindir}/ascii
install -m644 ascii.1 -D %{buildroot}%{_mandir}/man1/ascii.1


%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README COPYING
%{_mandir}/man1/ascii.1*
%{_bindir}/ascii


%changelog
* Fri Mar 25 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.11-2mdv2011.0
+ Revision: 648529
- really clean %%install (thanks Peroyvind)
- update to 3.11
- fix %%buildroot use

* Mon Dec 06 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.10-1mdv2011.0
+ Revision: 612787
- update to 3.10

* Sun Oct 17 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.9-1mdv2011.0
+ Revision: 586264
- update to 3.9
- fix Source0
- quick spec cleanup
- fix %%buildroot use
- fix rpmlint warnings and licence

* Tue May 19 2009 Jérôme Brenier <incubusss@mandriva.org> 3.8-4mdv2010.0
+ Revision: 377657
- fix license (GPLv2)

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 3.8-3mdv2009.0
+ Revision: 226176
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 3.8-2mdv2008.1
+ Revision: 135823
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 01 2007 Nicolas Lécureuil <neoclust@mandriva.org> 3.8-2mdv2007.0
+ Revision: 115795
- Rebuild
- Import ascii

* Fri May 27 2005 Nicolas L�cureuil <neoclust@mandriva.org> 3.8-1mdk
- New release 3.8
- %%{1}mdv2007.1

* Thu May 12 2005 Lenny Cartier <lenny@mandriva.com> 3.6-3mdk
- rebuild

