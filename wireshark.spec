#
# Conditional build:
%bcond_with	gtk1		# build gtk+1 (not gtk+2) based wireshark binary
%bcond_without	krb5		# build without kerberos5 support (via heimdal)
%bcond_without	snmp		# build without snmp support
#
Summary:	Network traffic and protocol analyzer
Summary(es):	Analizador de tr�fico de red
Summary(pl):	Analizator ruchu i protoko��w sieciowych
Summary(pt_BR):	Analisador de tr�fego de rede
Summary(ru):	���������� �������� ��������
Summary(uk):	���̦����� ���������� ���Ʀ��
Name:		wireshark
Version:	1.0.3
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.wireshark.org/download/src/%{name}-%{version}.tar.bz2
# Source0-md5:	1f9bacf6df9150a8dd8fe862a4be27a8
Source1:	%{name}.desktop
Source2:	%{name}.su-start-script
URL:		http://www.wireshark.org/
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
Requires:	%{name}-tools = %{version}-%{release}
Requires:	libpcap >= 0.4
Provides:	ethereal
Provides:	ethereal-gnome
Obsoletes:	ethereal
Obsoletes:	ethereal-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wireshark is the name for powerful graphical network sniffer, traffic
and protocol analyzer based on GTK+ and libpcap libraries. It lets you
capture and interactively browse the contents of network frames with
vast knowledge of more than 100 network protocols. Wireshark has
severeal useful features, including a rich display filter language,
the ability to view the ASCII contents of a TCP connection and plug-in
capabilities.

%description -l es.UTF-8
Analizador de tráfico de red.

%description -l pl.UTF-8
Wireshark jest potężnym, graficznym snifferem, analizatorem ruchu oraz
protokołów sieciowych opartym na bibliotekach GTK+ oraz libpcap.
Umożliwia on przechwytywanie oraz interaktywną analizę zawartości
ramek oraz ponad stu protokołów sieciowych. Wireshark posiada wiele
użytecznych cech, takich jak rozbudowany język filtrów wyświetlania,
możliwość oglądania przebiegu sesji TCP oraz możliwość dołączania
wtyczek (plug-ins).

%description -l pt_BR.UTF-8
O Wireshark é um analisador de protocolo de rede baseado no GTK+.

%description -l ru.UTF-8
Wireshark - это анализатор сетевого траффика для Unix-подобных ОС. Он
базируется на GTK+ и libpcap.

%description -l uk.UTF-8
Wireshark - це аналізатор мережевого трафіку для Unix-подібних ОС. Він
базується на GTK+ та libpcap.

%package common
Summary:	Network traffic and protocol analyzer - common files
Summary(pl.UTF-8):	Analizator ruchu i protokołów sieciowych - wspólne pliki
Group:		Networking
Requires:	libwiretap = %{version}-%{release}
Provides:	ethereal-common
Obsoletes:	ethereal-common

%description common
Wireshark is the name for powerful graphical network sniffer, traffic
and protocol analyzer based on GTK+ and libpcap libraries. It lets you
capture and interactively browse the contents of network frames with
vast knowledge of more than 100 network protocols. Wireshark has
severeal useful features, including a rich display filter language,
the ability to view the ASCII contents of a TCP connection and plug-in
capabilities.

%description common -l es.UTF-8
Analizador de tráfico de red.

%description common -l pl.UTF-8
Wireshark jest potężnym, graficznym snifferem, analizatorem ruchu oraz
protokołów sieciowych opartym na bibliotekach GTK+ oraz libpcap.
Umożliwia on przechwytywanie oraz interaktywną analizę zawartości
ramek oraz ponad stu protokołów sieciowych. Wireshark posiada wiele
użytecznych cech, takich jak rozbudowany język filtrów wyświetlania,
możliwość oglądania przebiegu sesji TCP oraz możliwość dołączania
wtyczek (plug-ins).

%description common -l pt_BR.UTF-8
O Wireshark é um analisador de protocolo de rede baseado no GTK+.

%description common -l ru.UTF-8
Wireshark - это анализатор сетевого траффика для Unix-подобных ОС. Он
базируется на GTK+ и libpcap.

%description common -l uk.UTF-8
Wireshark - це аналізатор мережевого трафіку для Unix-подібних ОС. Він
базується на GTK+ та libpcap.

%package tools
Summary:	Tools for manipulating capture files
Summary(pl.UTF-8):	Narzędzia do obróbki plików z przechwyconymi pakietami sieciowymi
Group:		Networking
Requires:	%{name}-common = %{version}-%{release}
Provides:	ethereal-tools
Obsoletes:	ethereal-tools

%description tools
Set of tools for manipulating capture files. Contains:
- capinfo - prints informatio about binary capture files,
- dftest - shows display filter byte-code,
- editcap - edit and/or translate the format of capture files,
- idl2eth - corba IDL to Wireshark Plugin Generator,
- mergecap - merges two capture files into one,
- text2cap - generate a capture file from an ASCII hexdump of packets.

%description tools -l pl.UTF-8
Zestaw narzędzi do obróbki plików z przechwyconymi pakietami. Zawiera:
- capinfo - wyświetla informacje o binarnych plikach zrzutu,
- dftest - pokazuje byte-code filtrów wyświetlania,
- editcap - do edycji plików i tłumaczenia ich na inne formaty,
- idl2eth - konwerter Corba IDL do pluginów Wireshark,
- mergecap - do łączenia dwóch plików w jeden,
- text2cap - do generowania pliku cap z szesnastkowego zrzutu ASCII
  pakietów.

%package -n twireshark
Summary:	Text-mode network traffic and protocol analyzer
Summary(pl.UTF-8):	Tekstowy analizator ruchu i protokołów sieciowych
Summary(pt_BR.UTF-8):	Analisador modo texto de tráfego de rede (sniffer)
Group:		Networking
Requires:	%{name}-common = %{version}-%{release}
Requires:	libpcap >= 0.4
Provides:	tethereal
Obsoletes:	tethereal

%description -n twireshark
Twireshark is a network protocol analyzer. It lets you capture packet
data from a live network, or read packets from a previously saved
capture file, either printing a decoded form of those packets to the
standard output or writing the packets to a file. Twireshark's native
capture file format is libpcap format, which is also the format used
by tcpdump and various other tools.

%description -n twireshark -l pl.UTF-8
Twireshark jest analizatorem protokołów sieciowych. Pozwala na
przechwytywanie pakietów z sieci lub wczytywanie danych z pliku.
Zdekodowany wynik (a twireshark zna ponad 100 rozmaitych protokołów
sieciowych!) jest wyświetlony na ekranie. Natywnym formatem plików
tetherala jest format libpcap, tak więc jest on kompatybilny z
tcpdumpem i innymi podobnymi narzędziami.

%description -n twireshark -l pt_BR.UTF-8
Esta é uma versão para modo texto do analisador de tráfego de rede
Wireshark.

%package -n libwiretap
Summary:	Packet capture and analysis library
Summary(pl.UTF-8):	Biblioteka do przechwytywania i analizy pakietów
Group:		Libraries

%description -n libwiretap
Wiretap is a library that is being developed as a future replacement
for libpcap, the current standard Unix library for packet capturing.

%description -n libwiretap -l pl.UTF-8
Biblioteka Wiretap rozwijana jest jako przyszły następca biblioteki
libpcap, obecnie standardu przechwytywania pakietów w systemach Unix.

%package -n libwiretap-devel
Summary:	Header files for libwiretap packet capture library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwiretap do przechwytywania pakietów
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
install image/hi48-app-wireshark.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

install wiretap/*.h $RPM_BUILD_ROOT%{_includedir}/wiretap

# plugins *.la are useless - *.so are loaded through gmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/%{version}*/*.la

# no headers installed for this library
rm -f $RPM_BUILD_ROOT%{_libdir}/libwireshark.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	common -p /sbin/ldconfig
%postun	common -p /sbin/ldconfig

%post	-n libwiretap -p /sbin/ldconfig
%postun	-n libwiretap -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wireshark
%attr(755,root,root) %{_bindir}/%{name}_su
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{version}*
%attr(755,root,root) %{_libdir}/%{name}/plugins/%{version}*/*.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/wireshark.1*

%files common
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README{,.[lv]*} doc/{randpkt.txt,README.*}
%attr(755,root,root) %{_libdir}/libwireshark.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwireshark.so.0
%{_mandir}/man4/wireshark-filter.4*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/capinfos
%attr(755,root,root) %{_bindir}/dftest
%attr(755,root,root) %{_bindir}/dumpcap
%attr(755,root,root) %{_bindir}/editcap
%attr(755,root,root) %{_bindir}/idl2wrs
%attr(755,root,root) %{_bindir}/mergecap
%attr(755,root,root) %{_bindir}/randpkt
%attr(755,root,root) %{_bindir}/rawshark
%attr(755,root,root) %{_bindir}/text2pcap
%{_mandir}/man1/capinfos.1*
%{_mandir}/man1/dumpcap.1*
%{_mandir}/man1/editcap.1*
%{_mandir}/man1/idl2wrs.1*
%{_mandir}/man1/mergecap.1*
%{_mandir}/man1/rawshark.1*
%{_mandir}/man1/text2pcap.1*

%files -n twireshark
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tshark
%{_mandir}/man1/tshark*

%files -n libwiretap
%defattr(644,root,root,755)
%doc wiretap/{README*,AUTHORS}
%attr(755,root,root) %{_libdir}/libwiretap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwiretap.so.0

%files -n libwiretap-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwiretap.so
%{_libdir}/libwiretap.la
%{_includedir}/wiretap
