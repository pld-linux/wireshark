# TODO
# - gtk+3 bcond?
# - use policykit to gain root
# - use %caps when rpm supports it: %attr(750,root,wireshark) %caps(cap_net_raw,cap_net_admin=eip) %{_sbindir}/dumpcap
#
# Conditional build:
%bcond_without	gui		# build without any GUI support
%bcond_without	gtk3		# build without GTK+3 support
%bcond_without	kerberos5	# build without Kerberos V support
%bcond_without	snmp		# build without snmp support
%bcond_without	qt		# build without Qt support

%if %{without gui}
%undefine with_qt
%endif

Summary:	Network traffic and protocol analyzer
Summary(es.UTF-8):	Analizador de tráfico de red
Summary(pl.UTF-8):	Analizator ruchu i protokołów sieciowych
Summary(pt_BR.UTF-8):	Analisador de tráfego de rede
Summary(ru.UTF-8):	Анализатор сетевого траффика
Summary(uk.UTF-8):	Аналізатор мережевого трафіку
Name:		wireshark
Version:	1.12.4
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	http://www.wireshark.org/download/src/%{name}-%{version}.tar.bz2
# Source0-md5:	acfa156fd35cb66c867b1ace992e4b5b
Patch0:		%{name}-Werror.patch
Patch1:		%{name}-gcc43.patch
Patch2:		%{name}-ac.patch
Patch3:		%{name}-desktop.patch
URL:		http://www.wireshark.org/
BuildRequires:	GeoIP-devel
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison
BuildRequires:	c-ares-devel
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gnutls-devel >= 1.2.0
%if %{with gui}
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
%endif
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	libcap-devel
BuildRequires:	libgcrypt-devel >= 1.1.92
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	libpcap-devel >= 2:1.0.0-4
BuildRequires:	libsmi-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	lua52-devel
%{?with_snmp:BuildRequires:	net-snmp-devel}
%{?with_kerberos5:BuildRequires:	openssl-devel}
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
%{?with_gui:BuildRequires:	portaudio-devel}
BuildRequires:	rpmbuild(macros) >= 1.527
%if %{with qt}
BuildRequires:	QtCore-devel >= 4.6.0
BuildRequires:	qt4-build
%endif
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Requires:	%{name}-common = %{version}-%{release}
%if %{with gui}
Requires:	gtk+2 >= 2:2.12.0
%endif
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
Provides:	%{name}-tools
Provides:	ethereal-common
Provides:	group(wireshark)
Obsoletes:	ethereal-common
Obsoletes:	wireshark-tools
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	/sbin/setcap

%description common
Wireshark is the name for powerful graphical network sniffer, traffic
and protocol analyzer based on GTK+ and libpcap libraries. It lets you
capture and interactively browse the contents of network frames with
vast knowledge of more than 100 network protocols. Wireshark has
severeal useful features, including a rich display filter language,
the ability to view the ASCII contents of a TCP connection and plug-in
capabilities.

This package provides set of tools for manipulating capture files. It
contains:
- capinfos - prints informatio about binary capture files,
- captype - prints the file types of capture files,
- dftest - shows display filter byte-code,
- dumpcap - dumps network traffic to a file,
- editcap - edit and/or translate the format of capture files,
- mergecap - merges two capture files into one,
- randpkt - generates libpcap trace file full of random packets,
- rawshark - dumps and analyzes raw libpcap data,
- text2cap - generate a capture file from an ASCII hexdump of packets.

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

Pakiet ten dostarcza także zestaw narzędzi do obróbki plików z
przechwyconymi pakietami, obejmujący:
- capinfos - do wyświetlania informacji o binarnych plikach zrzutu,
- captype - do wyświetlania rodzaju plików zrzutu,
- dftest - do pokazywania bajtkodu filtrów wyświetlania,
- dumpcap - do zrzucania ruchu sieciowego do pliku,
- editcap - do edycji plików i tłumaczenia ich na inne formaty,
- mergecap - do łączenia dwóch plików w jeden,
- randpkt - do generowania plikow cap z losowymi danymi,
- rawshark - do obróbki plików cap,
- text2cap - do generowania pliku cap z szesnastkowego zrzutu ASCII
  pakietów.

%description common -l pt_BR.UTF-8
O Wireshark é um analisador de protocolo de rede baseado no GTK+.

%description common -l ru.UTF-8
Wireshark - это анализатор сетевого траффика для Unix-подобных ОС. Он
базируется на GTK+ и libpcap.

%description common -l uk.UTF-8
Wireshark - це аналізатор мережевого трафіку для Unix-подібних ОС. Він
базується на GTK+ та libpcap.

%package qt
Summary:	Qt-based network traffic and protocol analyzer
Summary(pl.UTF-8):	Analizator ruchu i protokołów sieciowych oparty na Qt
Group:		Networking

%description qt
An initial port to Qt (aka QtShark).

%description qt -l pl.UTF-8
Wstępna wersja analizatora wireshark oparta na Qt (znana też pod nazwą
QtShark).

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
Requires:	glib2 >= 1:2.22.0
Requires:	libnl >= 3.2

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
Requires:	glib2-devel >= 1:2.14.0
Requires:	libnl-devel >= 3.2
Requires:	libwiretap = %{version}-%{release}

%description -n libwiretap-devel
Header files for libwiretap packet capture library.

%description -n libwiretap-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libwiretap służącej do przechwytywania
pakietów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
find -name Makefile.am | xargs sed -i -e 's/-Werror//g'

%build
%{__libtoolize}
%{__aclocal} -I aclocal-fallback
%{__autoconf}
%{__automake}
%configure \
	--enable-dftest \
	--enable-packet-editor \
	--enable-randpkt \
	--disable-silent-rules \
	--disable-usr-local \
%if %{with gui}
	%{?with_gtk3:--with-gtk3 --without-gtk2}%{!?with_gtk3:--with-gtk2 --without-gtk3} \
%endif
	%{__with_without qt} \
	%{__enable_disable gui wireshark} \
	--with-lua \
%if %{with kerberos5}
	--with-krb5 \
	--with-ssl \
%endif
	%{!?with_snmp:--without-net-snmp --without-ucdsnmp}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_includedir}/wiretap}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p image/hi48-app-wireshark.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
cp -p wireshark.desktop $RPM_BUILD_ROOT%{_desktopdir}

cp -a wiretap/*.h $RPM_BUILD_ROOT%{_includedir}/wiretap

# plugins *.la are useless - *.so are loaded through gmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/%{version}*/*.la

# no headers installed for this library
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwireshark.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%pre	common
%groupadd -P %{name}-common -g 104 wireshark

%post	common
/sbin/ldconfig
/sbin/setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' %{_bindir}/dumpcap
exit 0

%postun	common
/sbin/ldconfig
if [ "$1" = "0" ]; then
	%groupremove wireshark
fi

%post	-n libwiretap -p /sbin/ldconfig
%postun	-n libwiretap -p /sbin/ldconfig

%if %{with gui}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wireshark
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/wireshark.1*
%endif

%files common
%defattr(644,root,root,755)
%doc AUTHORS* ChangeLog NEWS README{,.[lv]*} doc/{randpkt.txt,README.*}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{version}*
%attr(755,root,root) %{_libdir}/%{name}/plugins/%{version}*/*.so
%attr(755,root,root) %{_bindir}/capinfos
%attr(755,root,root) %{_bindir}/captype
%attr(755,root,root) %{_bindir}/dftest
%attr(750,root,wireshark) %{_bindir}/dumpcap
%attr(755,root,root) %{_bindir}/editcap
%attr(755,root,root) %{_bindir}/mergecap
%attr(755,root,root) %{_bindir}/randpkt
%attr(755,root,root) %{_bindir}/rawshark
%attr(755,root,root) %{_bindir}/reordercap
%attr(755,root,root) %{_bindir}/text2pcap
%attr(755,root,root) %{_libdir}/libwireshark.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwireshark.so.5
%{_mandir}/man1/capinfos.1*
%{_mandir}/man1/dftest.1*
%{_mandir}/man1/dumpcap.1*
%{_mandir}/man1/editcap.1*
%{_mandir}/man1/mergecap.1*
%{_mandir}/man1/rawshark.1*
%{_mandir}/man1/randpkt.1*
%{_mandir}/man1/reordercap.1*
%{_mandir}/man1/text2pcap.1*
%{_mandir}/man4/wireshark-filter.4*

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wireshark-qt
%endif

%files -n twireshark
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tshark
%{_mandir}/man1/tshark*.1*

%files -n libwiretap
%defattr(644,root,root,755)
%doc wiretap/{README*,AUTHORS}
%attr(755,root,root) %{_libdir}/libfiletap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfiletap.so.0
%attr(755,root,root) %{_libdir}/libwiretap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwiretap.so.4
%attr(755,root,root) %{_libdir}/libwsutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwsutil.so.4

%files -n libwiretap-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfiletap.so
%attr(755,root,root) %{_libdir}/libwiretap.so
%attr(755,root,root) %{_libdir}/libwsutil.so
%{_libdir}/libfiletap.la
%{_libdir}/libwiretap.la
%{_libdir}/libwsutil.la
%{_includedir}/wiretap
