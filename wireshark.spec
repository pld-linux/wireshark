#
# Conditional build:
%bcond_with	gtk1		# builds gtk+1 (not gtk+2) based ethereal binary
%bcond_without	snmp		# builds without snmp support
#
Summary:	Network traffic and protocol analyzer
Summary(es):	Analizador de tr�fico de red
Summary(pl):	Analizator ruchu i protoko��w sieciowych
Summary(pt_BR):	Analisador de tr�fego de rede
Summary(ru):	���������� �������� ��������
Summary(uk):	���̦����� ���������� ���Ʀ��
Name:		ethereal
Version:	0.10.3
Release:	5 
License:	GPL
Group:		Networking
Source0:	http://www.ethereal.com/distribution/all-versions/%{name}-%{version}.tar.bz2
# Source0-md5:	6902272eb5304f57db76bf91abe453d1
Source1:	%{name}.desktop
Source2:	%{name}.su-start-script
URL:		http://www.ethereal.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libelf-devel
BuildRequires:	flex
%if %{with gtk1}
BuildRequires:	gtk+-devel >= 1.2
%else
BuildRequires:	gtk+2-devel
%endif
BuildRequires:	libpcap-devel >= 0.4
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.6m
BuildRequires:	perl-devel
%{!?_without_snmp:BuildRequires:	ucd-snmp-devel}
BuildRequires:	zlib-devel
Requires:	%{name}-common = %{version}-%{release}
Requires:	libpcap >= 0.4
#Requires:	pango-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ethereal-gnome

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define		_desktopdir	%{_applnkdir}/Network/Misc

%description
Ethereal is the name for powerful graphical network sniffer, traffic
and protocol analyzer based on GTK+ and libpcap libraries. It lets you
capture and interactively browse the contents of network frames with
vast knowledge of more than 100 network protocols. Ethereal has
severeal useful features, including a rich display filter language,
the ability to view the ASCII contents of a TCP connection and plug-in
capabilities.

%description -l es
Analizador de tr�fico de red.

%description -l pl
Ethereal jest pot�nym, graficznym snifferem, analizatorem ruchu oraz
protoko��w sieciowych opartym na bibliotekach GTK+ oraz libpcap.
Umo�liwia on przechwytywanie oraz intereaktywn� analiz� zawarto�ci
ramek oraz ponad stu protoko��w sieciowych. Ethereal posiada wiele
u�ytecznych cech, takich jak rozbudowany j�zyk filtr�w wy�wietlania,
mo�liwo�� ogl�dania przebiegu sesji TCP oraz mo�liwo�� do��czania
wtyczek (plug-ins).

%description -l pt_BR
O Ethereal � um analisador de protocolo de rede baseado no GTK+.

%description -l ru
Ethereal - ��� ���������� �������� �������� ��� Unix-�������� ��. ��
���������� �� GTK+ � libpcap.

%description -l uk
Ethereal - �� ���̦����� ���������� ���Ʀ�� ��� Unix-��Ħ���� ��. ���
���դ���� �� GTK+ �� libpcap.

%package common
Summary:	Network traffic and protocol analyzer - common files
Summary(pl):	Analizator ruchu i protoko��w sieciowych - wsp�lne pliki
Group:		Networking
Requires:	libwiretap = %{version}-%{release}

%description common
Ethereal is the name for powerful graphical network sniffer, traffic
and protocol analyzer based on GTK+ and libpcap libraries. It lets you
capture and interactively browse the contents of network frames with
vast knowledge of more than 100 network protocols. Ethereal has
severeal useful features, including a rich display filter language,
the ability to view the ASCII contents of a TCP connection and plug-in
capabilities.

%description common -l es
Analizador de tr�fico de red.

%description common -l pl
Ethereal jest pot�nym, graficznym snifferem, analizatorem ruchu oraz
protoko��w sieciowych opartym na bibliotekach GTK+ oraz libpcap.
Umo�liwia on przechwytywanie oraz intereaktywn� analiz� zawarto�ci
ramek oraz ponad stu protoko��w sieciowych. Ethereal posiada wiele
u�ytecznych cech, takich jak rozbudowany j�zyk filtr�w wy�wietlania,
mo�liwo�� ogl�dania przebiegu sesji TCP oraz mo�liwo�� do��czania
wtyczek (plug-ins).

%description common -l pt_BR
O Ethereal � um analisador de protocolo de rede baseado no GTK+.

%description common -l ru
Ethereal - ��� ���������� �������� �������� ��� Unix-�������� ��. ��
���������� �� GTK+ � libpcap.

%description common -l uk
Ethereal - �� ���̦����� ���������� ���Ʀ�� ��� Unix-��Ħ���� ��. ���
���դ���� �� GTK+ �� libpcap.

%package tools
Summary:	Tools for manipulating capture files
Summary(pl):	Narz�dzia do obr�bki plik�w z przechwyconymi pakietami sieciowymi
Group:		Networking
Requires:	%{name}-common = %{version}-%{release}

%description tools
Set of tools for manipulating capture files. Contains:
- editcap - Edit and/or translate the format of capture files
- mergecap - Merges two capture files into one
- text2cap - Generate a capture file from an ASCII hexdump of packets

%description tools -l pl
Zestaw narz�dzi do obr�bki plik�w z przechwyconymi pakietami. Zawiera:
- editcap - do edycji plik�w i t�umaczenia ich na inne formaty,
- mergecap - do ��czenia dw�ch plik�w w jeden,
- text2cap - do generowania pliku cap z szesnastkowego zrzutu ASCII
  pakiet�w.

%package -n tethereal
Summary:	Text-mode network traffic and protocol analyzer
Summary(pl):	Tekstowy analizator ruchu i protoko��w sieciowych
Summary(pt_BR):	Analisador modo texto de tr�fego de rede (sniffer)
Group:		Networking
Requires:	%{name}-common = %{version}-%{release}
Requires:	libpcap >= 0.4

%description -n tethereal
Tethereal is a network protocol analyzer. It lets you capture packet
data from a live network, or read packets from a previously saved
capture file, either printing a decoded form of those packets to the
standard output or writing the packets to a file. Tethereal's native
capture file format is libpcap format, which is also the format used
by tcpdump and various other tools.

%description -n tethereal -l pl
Tethereal jest analizatorem protoko��w sieciowych. Pozwala na
przechwytywanie pakiet�w z sieci lub wczytywanie danych z pliku.
Zdekodowany wynik (a tethereal zna ponad 100 rozmaitych protoko��w
sieciowych!) jest wy�wietlony na ekranie. Natywnym formatem plik�w
tetherala jest format libpcap, tak wi�c jest on kompatybilny z
tcpdumpem i innymi podobnymi narz�dziami.

%description -n tethereal -l pt_BR
Esta � uma vers�o para modo texto do analisador de tr�fego de rede
Ethereal.

%package -n libwiretap
Summary:	Packet capture and analysis library
Summary(pl):	Biblioteka do przechwytywania i analizy pakiet�w
Group:		Libraries

%description -n libwiretap
Wiretap is a library that is being developed as a future replacement
for libpcap, the current standard Unix library for packet capturing.

%description -n libwiretap -l pl
Biblioteka Wiretap rozwijana jest jako przysz�y nastepca biblioteki
libpcap, obecnie standardu przechwytywania pakiet�w w systemach Unix.

%package -n libwiretap-devel
Summary:	Header files for libwiretap packet capture library
Summary(pl):	Pliki nag��wkowe biblioteki libwiretap do przechwytywania pakiet�w
Group:		Development/Libraries
%if %{with gtk1}
Requires:	gtk+-devel >= 1.2
%else
Requires:	gtk+2-devel
%endif
Requires:	libwiretap = %{version}-%{release}

%description -n libwiretap-devel
Wiretap is a library that is being developed as a future replacement
for libpcap, the current standard Unix library for packet capturing.
Thos package contains files necessary for programming using Wiretap
library.

%description -n libwiretap-devel -l pl
Biblioteka Wiretap rozwijana jest jako przysz�y nastepca biblioteki
libpcap, obecnie standardu przechwytywania pakiet�w w systemach Unix.
Pakiet zawiera pliki dla programist�w korzystaj�cych z tej biblioteki.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I aclocal-fallback
%{__autoconf}
%{__automake}
cd epan
rm -f missing
%{__aclocal} -I ../aclocal-fallback
%{__autoconf}
# don't use --force here
automake -a -c --foreign
cd ../wiretap
%{__aclocal} -I ../aclocal-fallback
%{__autoconf}
# don't use --force here
automake -a -c --foreign
cd ..
%configure \
	--enable-randpkt \
	--enable-dftest \
	%{!?with_gtk1:--enable-gtk2} \
	--with-plugindir=%{_libdir}/%{name} \
	%{!?with_snmp:--without-net-snmp --without-ucdsnmp}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_includedir}/wiretap}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}_su
install image/ethereal48x48-trans.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

# plugins *.la are useless - *.so are loaded through gmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/%{version}/*.la

install wiretap/*.h $RPM_BUILD_ROOT%{_includedir}/wiretap

%clean
rm -rf $RPM_BUILD_ROOT

%post	common -p /sbin/ldconfig
%postun	common -p /sbin/ldconfig

%post	-n libwiretap -p /sbin/ldconfig
%postun	-n libwiretap -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ethereal
%attr(755,root,root) %{_bindir}/%{name}_su
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{version}
%attr(755,root,root) %{_libdir}/%{name}/plugins/%{version}/*.so
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/ethereal.1*

%files common
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README{,.[lv]*} doc/{randpkt.txt,README.*}
%attr(755,root,root) %{_libdir}/libethereal.so.*.*.*
%{_mandir}/man4/ethereal-filter.4*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dftest
%attr(755,root,root) %{_bindir}/editcap
%attr(755,root,root) %{_bindir}/idl2eth
%attr(755,root,root) %{_bindir}/mergecap
%attr(755,root,root) %{_bindir}/text2pcap
%attr(755,root,root) %{_bindir}/randpkt
%{_mandir}/man1/editcap*
%{_mandir}/man1/idl2eth*
%{_mandir}/man1/mergecap*
%{_mandir}/man1/text2pcap*

%files -n tethereal
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tethereal
%{_mandir}/man1/tethereal*

%files -n libwiretap
%defattr(644,root,root,755)
%doc wiretap/{README*,AUTHORS,NEWS,ChangeLog}
%attr(755,root,root) %{_libdir}/libwiretap.so.*.*.*

%files -n libwiretap-devel
%defattr(644,root,root,755)
%{_includedir}/wiretap
%{_libdir}/libwiretap.so
%{_libdir}/libwiretap.la
