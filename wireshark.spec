# TODO
# - use policykit to gain root
# - use %caps when rpm supports it: %attr(750,root,wireshark) %caps(cap_net_raw,cap_net_admin=eip) %{_sbindir}/dumpcap
# - unpackaged files (datadir ?):
# warning: Installed (but unpackaged) file(s) found:
#        /usr/lib64/wireshark/cmake/FindGLIB2.cmake
#        /usr/lib64/wireshark/cmake/FindWSWinLibs.cmake
#        /usr/lib64/wireshark/cmake/LocatePythonModule.cmake
#        /usr/lib64/wireshark/cmake/UseAsn2Wrs.cmake
#        /usr/lib64/wireshark/cmake/UseMakePluginReg.cmake
#        /usr/lib64/wireshark/cmake/WiresharkConfig.cmake
#        /usr/lib64/wireshark/cmake/WiresharkConfigVersion.cmake
#        /usr/lib64/wireshark/cmake/WiresharkTargets-pld.cmake
#        /usr/lib64/wireshark/cmake/WiresharkTargets.cmake
#        /usr/share/AUTHORS-SHORT
#        /usr/share/COPYING
#        /usr/share/androiddump.html
#        /usr/share/asn2deb.html
#	(...)
#
# Conditional build:
%bcond_without	kerberos5	# Kerberos V support
%bcond_without	snmp		# SNMP support
%bcond_without	gui		# without QT GUI

Summary:	Network traffic and protocol analyzer
Summary(es.UTF-8):	Analizador de tráfico de red
Summary(pl.UTF-8):	Analizator ruchu i protokołów sieciowych
Summary(pt_BR.UTF-8):	Analisador de tráfego de rede
Summary(ru.UTF-8):	Анализатор сетевого траффика
Summary(uk.UTF-8):	Аналізатор мережевого трафіку
Name:		wireshark
Version:	3.0.0
Release:	2
License:	GPL v2+
Group:		Networking/Utilities
Source0:	https://www.wireshark.org/download/src/%{name}-%{version}.tar.xz
# Source0-md5:	258d62ac7434d126dc497303c8f7961b
Patch0:		cmake.patch
URL:		https://www.wireshark.org/
BuildRequires:	GeoIP-devel
BuildRequires:	asciidoc
BuildRequires:	bcg729-devel
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	c-ares-devel >= 1.5.0
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	gcc >= 5:3.2
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gnutls-devel >= 3.2.0
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	libcap-devel
BuildRequires:	libgcrypt-devel >= 1.4.2
BuildRequires:	libmaxminddb-devel
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	libpcap-devel >= 2:1.0.0-4
BuildRequires:	libssh-devel >= 0.6.0
BuildRequires:	libsmi-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
BuildRequires:	lua52-devel
BuildRequires:	lz4-devel
%{?with_snmp:BuildRequires:	net-snmp-devel}
BuildRequires:	nghttp2-devel
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig >= 1:0.7
BuildRequires:	python3 >= 1:3.4
BuildRequires:	rpmbuild(macros) >= 1.527
%{?with_gui:BuildRequires:	sbc-devel >= 1.0}
%{?with_gui:BuildRequires:	speexdsp-devel}
BuildRequires:	sed >= 4.0
BuildRequires:	snappy-devel
BuildRequires:	spandsp-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	w3m
BuildRequires:	xz
BuildRequires:	zlib-devel
%if %{with gui}
BuildRequires:	Qt5Core-devel >= 5.2
BuildRequires:	Qt5Multimedia-devel >= 5.2
BuildRequires:	Qt5PrintSupport-devel >= 5.2
BuildRequires:	Qt5Widgets-devel >= 5.2
BuildRequires:	libstdc++-devel >= 5
BuildRequires:	qt5-build >= 5.2
BuildRequires:	qt5-linguist >= 5.2
%endif
Requires:	gdk-pixbuf2 >= 2.26
Suggests:	xdg-utils
Provides:	ethereal
Provides:	ethereal-gnome
Obsoletes:	ethereal
Obsoletes:	ethereal-gnome
Obsoletes:	wireshark-gui-common
Obsoletes:	wireshark-qt
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
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnutls >= 3.1.10
Requires:	libpcap >= 0.4
Requires:	libssh >= 0.6.0
Provides:	ethereal-common
Provides:	group(wireshark)
Provides:	wireshark-tools
Obsoletes:	ethereal-common
Obsoletes:	wireshark-tools
Requires(post,postun):	/sbin/setcap

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

%package libs
Summary:	Wireshark packet capture and dissection libraries
Summary(pl.UTF-8):	Biblioteki Wiresharka do przechwytywania i sekcji pakietów
Group:		Libraries
Requires:	glib2 >= 1:2.32
Requires:	libgcrypt >= 1.4.2
Requires:	libnl >= 3.2
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
Requires:	glib2-devel >= 1:2.32
Requires:	libgcrypt-devel >= 1.4.2
Requires:	libnl-devel >= 3.2
Obsoletes:	libwiretap-devel < 2.4.0

%description devel
Header files for Wireshark libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Wiresharka.

%prep
%setup -q
%patch0 -p1

%build
%cmake -G "Unix Makefiles" \
  -DDISABLE_WERROR=ON \
  -DBUILD_wireshark=ON \
  -DENABLE_QT5=ON \
  -DENABLE_LUA=ON \
  -DBUILD_mmdbresolve=ON \
  -DBUILD_randpktdump=ON \
  -DBUILD_androiddump=ON \
  -DBUILD_tfshark=OFF \
  -DBUILD_corbaidl2wrs=ON \
  -DBUILD_dcerpcidl2wrs=ON \
  -DBUILD_xxx2deb=ON \
  -DENABLE_SMI=ON \
  -DENABLE_PORTAUDIO=ON \
  -DENABLE_PLUGINS=ON \
  -DENABLE_NETLINK=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_includedir}/wireshark}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p image/wsicon48.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%{?with_gui:cp -p wireshark.desktop $RPM_BUILD_ROOT%{_desktopdir}/wireshark.desktop}

# headers (from Fedora, inspired by debian/wireshark-dev.header-files)
install -d $RPM_BUILD_ROOT%{_includedir}/wireshark/{epan/{crypt,ftypes,dfilter,dissectors,wmem},wiretap,wsutil}
install config.h            $RPM_BUILD_ROOT%{_includedir}/wireshark
install cfile.h file.h      $RPM_BUILD_ROOT%{_includedir}/wireshark
install ws_diag_control.h   $RPM_BUILD_ROOT%{_includedir}/wireshark
install ws_symbol_export.h  $RPM_BUILD_ROOT%{_includedir}/wireshark
install epan/*.h            $RPM_BUILD_ROOT%{_includedir}/wireshark/epan
install epan/crypt/*.h      $RPM_BUILD_ROOT%{_includedir}/wireshark/epan/crypt
install epan/ftypes/*.h     $RPM_BUILD_ROOT%{_includedir}/wireshark/epan/ftypes
install epan/dfilter/*.h    $RPM_BUILD_ROOT%{_includedir}/wireshark/epan/dfilter
install epan/dissectors/*.h $RPM_BUILD_ROOT%{_includedir}/wireshark/epan/dissectors
install epan/wmem/*.h       $RPM_BUILD_ROOT%{_includedir}/wireshark/epan/wmem
install wiretap/*.h         $RPM_BUILD_ROOT%{_includedir}/wireshark/wiretap
install wsutil/*.h          $RPM_BUILD_ROOT%{_includedir}/wireshark/wsutil

# plugins *.la are useless - *.so are loaded through gmodule
#%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%update_mime_database

%postun
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
%{_desktopdir}/wireshark.desktop
#%{_datadir}/%{name}
%{_datadir}/appdata/wireshark.appdata.xml
%{_datadir}/mime/packages/wireshark.xml
%{_pixmapsdir}/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/mimetypes/application-%{name}-doc.png
%{_iconsdir}/hicolor/24x24/apps/%{name}.png
%{_iconsdir}/hicolor/24x24/mimetypes/application-%{name}-doc.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/mimetypes/application-%{name}-doc.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/mimetypes/application-%{name}-doc.png
%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/mimetypes/application-%{name}-doc.png
%{_iconsdir}/hicolor/128x128/apps/%{name}.png
%{_iconsdir}/hicolor/128x128/mimetypes/application-%{name}-doc.png
%{_iconsdir}/hicolor/256x256/apps/%{name}.png
%{_iconsdir}/hicolor/256x256/mimetypes/application-%{name}-doc.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/wireshark.1*
%endif

%files common
%defattr(644,root,root,755)
%doc AUTHORS* ChangeLog NEWS README.md README.linux doc/README.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/extcap
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/3.0
%dir %{_libdir}/%{name}/plugins/3.0/codecs
%dir %{_libdir}/%{name}/plugins/3.0/epan
%dir %{_libdir}/%{name}/plugins/3.0/wiretap
%attr(755,root,root) %{_libdir}/%{name}/extcap/androiddump
%attr(755,root,root) %{_libdir}/%{name}/extcap/ciscodump
%attr(755,root,root) %{_libdir}/%{name}/extcap/dpauxmon
%attr(755,root,root) %{_libdir}/%{name}/extcap/randpktdump
%attr(755,root,root) %{_libdir}/%{name}/extcap/sshdump
%attr(755,root,root) %{_libdir}/%{name}/extcap/sdjournal
%attr(755,root,root) %{_libdir}/%{name}/extcap/udpdump
%attr(755,root,root) %{_libdir}/%{name}/plugins/3.0/codecs/*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/3.0/epan/*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/3.0/wiretap/*.so
%attr(755,root,root) %{_bindir}/capinfos
%attr(755,root,root) %{_bindir}/captype
#%attr(755,root,root) %{_bindir}/dftest
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
#%attr(755,root,root) %{_bindir}/tfshark
%{_mandir}/man1/androiddump.1*
%{_mandir}/man1/capinfos.1*
%{_mandir}/man1/captype.1*
%{_mandir}/man1/ciscodump.1*
%{_mandir}/man1/dftest.1*
%{_mandir}/man1/dumpcap.1*
%{_mandir}/man1/editcap.1*
%{_mandir}/man1/mergecap.1*
%{_mandir}/man1/mmdbresolve.1*
%{_mandir}/man1/rawshark.1*
%{_mandir}/man1/randpkt.1*
%{_mandir}/man1/randpktdump.1*
%{_mandir}/man1/reordercap.1*
%{_mandir}/man1/sshdump.1*
%{_mandir}/man1/text2pcap.1*
%{_mandir}/man1/udpdump.1*
%{_mandir}/man4/extcap.4*
%{_mandir}/man4/wireshark-filter.4*

%files -n twireshark
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tshark
%{_mandir}/man1/tshark*.1*

%files libs
%defattr(644,root,root,755)
#%doc wiretap/README*
%attr(755,root,root) %{_libdir}/libwireshark.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwireshark.so.12
%attr(755,root,root) %{_libdir}/libwiretap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwiretap.so.9
%attr(755,root,root) %{_libdir}/libwscodecs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwscodecs.so.2
%attr(755,root,root) %{_libdir}/libwsutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwsutil.so.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwireshark.so
%attr(755,root,root) %{_libdir}/libwiretap.so
%attr(755,root,root) %{_libdir}/libwscodecs.so
%attr(755,root,root) %{_libdir}/libwsutil.so
#%{_libdir}/libwireshark.la
#%{_libdir}/libwiretap.la
#%{_libdir}/libwscodecs.la
#%{_libdir}/libwsutil.la
%{_includedir}/wireshark
%{_pkgconfigdir}/wireshark.pc
