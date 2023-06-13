# TODO
# - use policykit to gain root
# - use %caps when rpm supports it: %attr(750,root,wireshark) %caps(cap_net_raw,cap_net_admin=eip) %{_sbindir}/dumpcap
#
# Conditional build:
%bcond_without	kerberos5	# Kerberos V support
%bcond_without	snmp		# SNMP support
%bcond_without	gui		# without QT GUI

%define		branch_ver	4.0
%define		qt_ver		5.12
Summary:	Network traffic and protocol analyzer
Summary(es.UTF-8):	Analizador de tráfico de red
Summary(pl.UTF-8):	Analizator ruchu i protokołów sieciowych
Summary(pt_BR.UTF-8):	Analisador de tráfego de rede
Summary(ru.UTF-8):	Анализатор сетевого траффика
Summary(uk.UTF-8):	Аналізатор мережевого трафіку
Name:		wireshark
Version:	4.0.6
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	https://2.na.dl.wireshark.org/src/%{name}-%{version}.tar.xz
# Source0-md5:	0994f7f327e0562f7a69bb4fa956dc7f
URL:		https://www.wireshark.org/
BuildRequires:	bcg729-devel
BuildRequires:	bison
BuildRequires:	c-ares-devel >= 1.13.0
BuildRequires:	cmake >= 3.10
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gnutls-devel >= 3.5.8
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	libbrotli-devel
# libcap-devel doesn't pull libcap, but only libcap-libs
BuildRequires:	libcap
BuildRequires:	libcap-devel
BuildRequires:	libgcrypt-devel >= 1.8.0
BuildRequires:	libmaxminddb-devel
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	libpcap-devel >= 2:1.0.0-4
BuildRequires:	libsmi-devel
BuildRequires:	libssh-devel >= 0.6.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.2.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
BuildRequires:	lua52-devel
BuildRequires:	lz4-devel
BuildRequires:	minizip-devel
%{?with_snmp:BuildRequires:	net-snmp-devel}
BuildRequires:	nghttp2-devel >= 1.11.0
BuildRequires:	opus-devel
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig >= 1:0.7
BuildRequires:	python3 >= 1:3.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	ruby-asciidoctor >= 1.5
%{?with_gui:BuildRequires:	sbc-devel >= 1.0}
BuildRequires:	sed >= 4.0
BuildRequires:	snappy-devel
BuildRequires:	spandsp-devel
%{?with_gui:BuildRequires:	speexdsp-devel}
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	webrtc-libilbc-devel
BuildRequires:	w3m
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel >= 1.0.0
%if %{with gui}
BuildRequires:	Qt5Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-linguist >= %{qt_ver}
%endif
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Multimedia >= %{qt_ver}
Requires:	Qt5PrintSupport >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	gdk-pixbuf2 >= 2.26
Requires:	hicolor-icon-theme
Suggests:	xdg-utils
Provides:	ethereal
Provides:	ethereal-gnome
Obsoletes:	ethereal < 1
Obsoletes:	ethereal-gnome < 1
Obsoletes:	wireshark-gui-common < 3
Obsoletes:	wireshark-qt < 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wireshark is the name for powerful graphical network sniffer, traffic
and protocol analyzer based on QT and libpcap libraries. It lets you
capture and interactively browse the contents of network frames with
vast knowledge of more than 100 network protocols. Wireshark has
severeal useful features, including a rich display filter language,
the ability to view the ASCII contents of a TCP connection and plug-in
capabilities.

%description -l es.UTF-8
Analizador de tráfico de red.

%description -l pl.UTF-8
Wireshark jest potężnym, graficznym snifferem, analizatorem ruchu oraz
protokołów sieciowych opartym na bibliotekach QT oraz libpcap.
Umożliwia on przechwytywanie oraz interaktywną analizę zawartości
ramek oraz ponad stu protokołów sieciowych. Wireshark posiada wiele
użytecznych cech, takich jak rozbudowany język filtrów wyświetlania,
możliwość oglądania przebiegu sesji TCP oraz możliwość dołączania
wtyczek (plug-ins).

%description -l pt_BR.UTF-8
O Wireshark é um analisador de protocolo de rede baseado no QT.

%description -l ru.UTF-8
Wireshark - это анализатор сетевого траффика для Unix-подобных ОС. Он
базируется на QT и libpcap.

%description -l uk.UTF-8
Wireshark - це аналізатор мережевого трафіку для Unix-подібних ОС. Він
базується на QT та libpcap.

%package common
Summary:	Network traffic and protocol analyzer - common files
Summary(pl.UTF-8):	Analizator ruchu i protokołów sieciowych - wspólne pliki
Group:		Networking
Requires(post,postun):	/sbin/setcap
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnutls >= 3.5.8
Requires:	libpcap >= 0.4
Requires:	libssh >= 0.6.0
Provides:	ethereal-common
Provides:	group(wireshark)
Provides:	wireshark-tools
Obsoletes:	ethereal-common < 1
Obsoletes:	wireshark-tools < 1.0.3-3

%description common
Wireshark is the name for powerful graphical network sniffer, traffic
and protocol analyzer based on QT and libpcap libraries. It lets you
capture and interactively browse the contents of network frames with
vast knowledge of more than 100 network protocols. Wireshark has
severeal useful features, including a rich display filter language,
the ability to view the ASCII contents of a TCP connection and plug-in
capabilities.

This package provides the shared library, plugins, data and a set of
tools for manipulating capture files. It contains:
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
protokołów sieciowych opartym na bibliotekach QT oraz libpcap.
Umożliwia on przechwytywanie oraz interaktywną analizę zawartości
ramek oraz ponad stu protokołów sieciowych. Wireshark posiada wiele
użytecznych cech, takich jak rozbudowany język filtrów wyświetlania,
możliwość oglądania przebiegu sesji TCP oraz możliwość dołączania
wtyczek (plug-ins).

Ten pakiet ten zawiera bibliotekę współdzieloną, wtyczki, dane oraz
zestaw narzędzi do obróbki plików z przechwyconymi pakietami,
obejmujący:
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
O Wireshark é um analisador de protocolo de rede baseado no QT.

%description common -l ru.UTF-8
Wireshark - это анализатор сетевого траффика для Unix-подобных ОС. Он
базируется на QT и libpcap.

%description common -l uk.UTF-8
Wireshark - це аналізатор мережевого трафіку для Unix-подібних ОС. Він
базується на QT та libpcap.

%package -n twireshark
Summary:	Text-mode network traffic and protocol analyzer
Summary(pl.UTF-8):	Tekstowy analizator ruchu i protokołów sieciowych
Summary(pt_BR.UTF-8):	Analisador modo texto de tráfego de rede (sniffer)
Group:		Networking
Requires:	%{name}-common = %{version}-%{release}
Requires:	libpcap >= 0.4
Provides:	tethereal
Obsoletes:	tethereal < 1

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

%package libs
Summary:	Wireshark packet capture and dissection libraries
Summary(pl.UTF-8):	Biblioteki Wiresharka do przechwytywania i sekcji pakietów
Group:		Libraries
Requires:	c-ares >= 1.13.0
Requires:	glib2 >= 1:2.50.0
Requires:	libgcrypt >= 1.8.0
Requires:	libnl >= 3.2
Requires:	zstd >= 1.0.0
Obsoletes:	libwiretap < 2.4.0

%description libs
Wireshark packet capture and dissection libraries.

%description libs -l pl.UTF-8
Biblioteki Wiresharka do przechwytywania i sekcji pakietów.

%package devel
Summary:	Header files for Wireshark libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Wiresharka
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.50.0
Requires:	libgcrypt-devel >= 1.8.0
Requires:	libnl-devel >= 3.2
Obsoletes:	libwiretap-devel < 2.4.0

%description devel
Header files for Wireshark libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Wiresharka.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DBUILD_androiddump=ON \
	-DBUILD_corbaidl2wrs=ON \
	-DBUILD_dcerpcidl2wrs=ON \
	-DBUILD_mmdbresolve=ON \
	-DBUILD_randpktdump=ON \
	-DBUILD_tfshark=OFF \
	-DBUILD_wireshark=ON \
	-DCMAKE_INSTALL_DATADIR:PATH=share/wireshark \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
	-DDISABLE_WERROR=ON \
	-DENABLE_LUA=ON \
	-DENABLE_NETLINK=ON \
	-DENABLE_PLUGINS=ON \
	-DENABLE_PORTAUDIO=ON \
	-DENABLE_QT5=ON \
	-DENABLE_SMI=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# used by installed headers, but not installed by cmake
cp -p build/config.h $RPM_BUILD_ROOT%{_includedir}/wireshark

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%update_icon_cache hicolor
%update_desktop_database
%update_mime_database

%postun
%update_icon_cache hicolor
%update_desktop_database
%update_mime_database

%pre	common
%groupadd -P %{name}-common -g 104 wireshark

%post	common
/sbin/setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' %{_bindir}/dumpcap
exit 0

%postun	common
if [ "$1" = "0" ]; then
	%groupremove wireshark
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%if %{with gui}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wireshark
%{_desktopdir}/org.wireshark.Wireshark.desktop
%{_datadir}/%{name}
%{_datadir}/metainfo/org.wireshark.Wireshark.metainfo.xml
%{_datadir}/mime/packages/org.wireshark.Wireshark.xml
%{_iconsdir}/hicolor/16x16/apps/org.wireshark.Wireshark.png
%{_iconsdir}/hicolor/16x16/mimetypes/org.wireshark.Wireshark-mimetype.png
%{_iconsdir}/hicolor/24x24/apps/org.wireshark.Wireshark.png
%{_iconsdir}/hicolor/24x24/mimetypes/org.wireshark.Wireshark-mimetype.png
%{_iconsdir}/hicolor/32x32/apps/org.wireshark.Wireshark.png
%{_iconsdir}/hicolor/32x32/mimetypes/org.wireshark.Wireshark-mimetype.png
%{_iconsdir}/hicolor/48x48/apps/org.wireshark.Wireshark.png
%{_iconsdir}/hicolor/48x48/mimetypes/org.wireshark.Wireshark-mimetype.png
%{_iconsdir}/hicolor/64x64/apps/org.wireshark.Wireshark.png
%{_iconsdir}/hicolor/64x64/mimetypes/org.wireshark.Wireshark-mimetype.png
%{_iconsdir}/hicolor/128x128/apps/org.wireshark.Wireshark.png
%{_iconsdir}/hicolor/128x128/mimetypes/org.wireshark.Wireshark-mimetype.png
%{_iconsdir}/hicolor/256x256/apps/org.wireshark.Wireshark.png
%{_iconsdir}/hicolor/256x256/mimetypes/org.wireshark.Wireshark-mimetype.png
%{_iconsdir}/hicolor/scalable/apps/org.wireshark.Wireshark.svg
%{_mandir}/man1/wireshark.1*
%endif

%files common
%defattr(644,root,root,755)
%doc AUTHORS* ChangeLog NEWS README.md README.linux doc/README.*
%dir %{_libdir}/%{name}/extcap
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{branch_ver}
%dir %{_libdir}/%{name}/plugins/%{branch_ver}/codecs
%dir %{_libdir}/%{name}/plugins/%{branch_ver}/epan
%dir %{_libdir}/%{name}/plugins/%{branch_ver}/wiretap
%attr(755,root,root) %{_libdir}/%{name}/extcap/androiddump
%attr(755,root,root) %{_libdir}/%{name}/extcap/ciscodump
%attr(755,root,root) %{_libdir}/%{name}/extcap/dpauxmon
%attr(755,root,root) %{_libdir}/%{name}/extcap/randpktdump
%attr(755,root,root) %{_libdir}/%{name}/extcap/sshdump
%attr(755,root,root) %{_libdir}/%{name}/extcap/sdjournal
%attr(755,root,root) %{_libdir}/%{name}/extcap/udpdump
%attr(755,root,root) %{_libdir}/%{name}/extcap/wifidump
%attr(755,root,root) %{_libdir}/%{name}/plugins/%{branch_ver}/codecs/*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/%{branch_ver}/epan/*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/%{branch_ver}/wiretap/*.so
%attr(755,root,root) %{_bindir}/capinfos
%attr(755,root,root) %{_bindir}/captype
%attr(750,root,wireshark) %{_bindir}/dumpcap
%attr(755,root,root) %{_bindir}/editcap
%attr(755,root,root) %{_bindir}/idl2wrs
%attr(755,root,root) %{_bindir}/mergecap
%attr(755,root,root) %{_bindir}/mmdbresolve
%attr(755,root,root) %{_bindir}/randpkt
%attr(755,root,root) %{_bindir}/rawshark
%attr(755,root,root) %{_bindir}/reordercap
%attr(755,root,root) %{_bindir}/sharkd
%attr(755,root,root) %{_bindir}/text2pcap
%{_mandir}/man1/androiddump.1*
%{_mandir}/man1/capinfos.1*
%{_mandir}/man1/captype.1*
%{_mandir}/man1/ciscodump.1*
%{_mandir}/man1/dftest.1*
%{_mandir}/man1/dpauxmon.1*
%{_mandir}/man1/dumpcap.1*
%{_mandir}/man1/editcap.1*
%{_mandir}/man1/etwdump.1.*
%{_mandir}/man1/idl2wrs.1*
%{_mandir}/man1/mergecap.1*
%{_mandir}/man1/mmdbresolve.1*
%{_mandir}/man1/rawshark.1*
%{_mandir}/man1/randpkt.1*
%{_mandir}/man1/randpktdump.1*
%{_mandir}/man1/reordercap.1*
%{_mandir}/man1/sdjournal.1*
%{_mandir}/man1/sshdump.1*
%{_mandir}/man1/text2pcap.1*
%{_mandir}/man1/udpdump.1*
%{_mandir}/man1/wifidump.1*
%{_mandir}/man4/extcap.4*
%{_mandir}/man4/wireshark-filter.4*

%files -n twireshark
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tshark
%{_mandir}/man1/tshark*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwireshark.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwireshark.so.16
%attr(755,root,root) %{_libdir}/libwiretap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwiretap.so.13
%attr(755,root,root) %{_libdir}/libwsutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwsutil.so.14
%dir %{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc wiretap/{README,README.airmagnet}
%attr(755,root,root) %{_libdir}/libwireshark.so
%attr(755,root,root) %{_libdir}/libwiretap.so
%attr(755,root,root) %{_libdir}/libwsutil.so
%{_includedir}/wireshark
%{_pkgconfigdir}/wireshark.pc
%{_libdir}/%{name}/cmake
