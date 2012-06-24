#
# Conditional build:
%bcond_with	gtk1		# builds gtk+1 (not gtk+2) based ethereal binary
%bcond_without	krb5		# builds without kerberos5 support (via heimdal)
%bcond_without	snmp		# builds without snmp support
#
Summary:	Network traffic and protocol analyzer
Summary(es):	Analizador de tr�fico de red
Summary(pl):	Analizator ruchu i protoko��w sieciowych
Summary(pt_BR):	Analisador de tr�fego de rede
Summary(ru):	���������� �������� ��������
Summary(uk):	���̦����� ���������� ���Ʀ��
Name:		ethereal
Version:	0.10.13
Release:	1
License:	GPL
Group:		Networking
Source0:	ftp://ftp.ethereal.com/pub/ethereal/all-versions/%{name}-%{version}.tar.bz2
# Source0-md5:	9998cb4907a70925d33292bae89530d4
Source1:	%{name}.desktop
Source2:	%{name}.su-start-script
URL:		http://www.ethereal.com/
BuildRequires:	adns-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	elfutils-devel
BuildRequires:	flex
%if %{with gtk1}
BuildRequires:	gtk+-devel >= 1.2
%else
BuildRequires:	gtk+2-devel >= 1:2.0.0
%endif
%{?with_krb5:BuildRequires:	heimdal-devel >= 0.7}
BuildRequires:	libpcap-devel >= 0.4
BuildRequires:	libtool
%{?with_snmp:BuildRequires:	net-snmp-devel}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	%{name}-common = %{version}-%{release}
Requires:	libpcap >= 0.4
Obsoletes:	ethereal-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Umo�liwia on przechwytywanie oraz interaktywn� analiz� zawarto�ci
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
Umo�liwia on przechwytywanie oraz interaktywn� analiz� zawarto�ci
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
- capinfo - prints informatio about binary capture files,
- dftest - shows display filter byte-code,
- editcap - edit and/or translate the format of capture files,
- idl2eth - corba IDL to Ethereal Plugin Generator,
- mergecap - merges two capture files into one,
- text2cap - generate a capture file from an ASCII hexdump of packets.

%description tools -l pl
Zestaw narz�dzi do obr�bki plik�w z przechwyconymi pakietami. Zawiera:
- capinfo - wy�wietla informacje o binarnych plikach zrzutu,
- dftest - pokazuje byte-code filtr�w wy�wietlania,
- editcap - do edycji plik�w i t�umaczenia ich na inne formaty,
- idl2eth - konwerter Corba IDL do plugin�w Ethereal,
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
Biblioteka Wiretap rozwijana jest jako przysz�y nast�pca biblioteki
libpcap, obecnie standardu przechwytywania pakiet�w w systemach Unix.

%package -n libwiretap-devel
Summary:	Header files for libwiretap packet capture library
Summary(pl):	Pliki nag��wkowe biblioteki libwiretap do przechwytywania pakiet�w
Group:		Development/Libraries
Requires:	libwiretap = %{version}-%{release}
%if %{with gtk1}
Requires:	gtk+-devel >= 1.2
%else
Requires:	gtk+2-devel >= 2.0.0
%endif

%description -n libwiretap-devel
Header files for libwiretap packet capture library.

%description -n libwiretap-devel -l pl
Pliki nag��wkowe biblioteki libwiretap s�u��cej do przechwytywania
pakiet�w.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I aclocal-fallback
%{__autoconf}
%{__automake}
cd wiretap
%{__aclocal} -I ../aclocal-fallback
%{__autoconf}
# don't use --force here
automake -a -c --foreign
cd ..
%configure \
	--enable-randpkt \
	--enable-dftest \
	--enable-threads \
	%{!?with_gtk1:--enable-gtk2} \
%if %{with krb5}
	--with-krb5 \
	--with-ssl \
%endif
	%{!?with_snmp:--without-net-snmp --without-ucdsnmp} \
	--with-plugindir=%{_libdir}/%{name}

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

install wiretap/*.h $RPM_BUILD_ROOT%{_includedir}/wiretap

# plugins *.la are useless - *.so are loaded through gmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/%{version}/*.la

# no headers installed for this library
rm -f $RPM_BUILD_ROOT%{_libdir}/libethereal.{so,la}

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
%attr(755,root,root) %{_bindir}/capinfos
%attr(755,root,root) %{_bindir}/dftest
%attr(755,root,root) %{_bindir}/editcap
%attr(755,root,root) %{_bindir}/idl2eth
%attr(755,root,root) %{_bindir}/mergecap
%attr(755,root,root) %{_bindir}/text2pcap
%attr(755,root,root) %{_bindir}/randpkt
%{_mandir}/man1/capinfo*
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
%attr(755,root,root) %{_libdir}/libwiretap.so
%{_libdir}/libwiretap.la
%{_includedir}/wiretap
