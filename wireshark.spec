#
# --with gtk1	builds gtk+1 based ethereal binary
#
 
Summary:	Network traffic and protocol analyzer
Summary(es):	Analizador de tráfico de red
Summary(pl):	Analizator ruchu i protoko³ów sieciowych
Summary(pt_BR): Analisador de tráfego de rede
Name:		ethereal
Version:	0.9.11
Release:	4.1
License:	GPL
Group:		Networking
Source0:	http://www.ethereal.com/distribution/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.su-start-script
Patch0:		%{name}-distcc.patch
URL:		http://www.ethereal.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
%if %{?_with_gtk1:1}0
BuildRequires:	gtk+-devel >= 1.2
%else
BuildRequires:	gtk+2-devel
%endif
BuildRequires:	libelf-devel
BuildRequires:	libpcap-devel >= 0.4
BuildRequires:	libtool
%{!?_without_snmp:BuildRequires:	net-snmp-devel}
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	perl-devel
BuildRequires:	zlib-devel
Requires:	libpcap >= 0.4
Requires:	%{name}-common
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
Analizador de tráfico de red.

%description -l pl
Ethereal jest potê¿nym, graficznym snifferem, analizatorem ruchu oraz
protoko³ów sieciowych opartym na bibliotekach GTK+ oraz libpcap.
Umo¿liwia on przechwytywanie oraz intereaktywn± analizê zawarto¶ci
ramek oraz ponad stu protoko³ów sieciowych. Ethereal posiada wiele
u¿ytecznych cech, takich jak rozbudowany jêzyk filtrów wy¶wietlania,
mo¿liwo¶æ ogl±dania przebiegu sesji TCP oraz mo¿liwo¶æ do³±czania
wtyczek (plug-ins).

%description -l pt_BR
O Ethereal é um analisador de protocolo de rede baseado no GTK+.

%package common
Summary:	Network traffic and protocol analyzer - common files
Summary(pl):	Analizator ruchu i protoko³ów sieciowych - wspólne pliki
Group:		Networking

%description common
Ethereal is the name for powerful graphical network sniffer, traffic
and protocol analyzer based on GTK+ and libpcap libraries. It lets you
capture and interactively browse the contents of network frames with
vast knowledge of more than 100 network protocols. Ethereal has
severeal useful features, including a rich display filter language,
the ability to view the ASCII contents of a TCP connection and plug-in
capabilities.

%description common -l es
Analizador de tráfico de red.

%description common -l pl
Ethereal jest potê¿nym, graficznym snifferem, analizatorem ruchu oraz
protoko³ów sieciowych opartym na bibliotekach GTK+ oraz libpcap.
Umo¿liwia on przechwytywanie oraz intereaktywn± analizê zawarto¶ci
ramek oraz ponad stu protoko³ów sieciowych. Ethereal posiada wiele
u¿ytecznych cech, takich jak rozbudowany jêzyk filtrów wy¶wietlania,
mo¿liwo¶æ ogl±dania przebiegu sesji TCP oraz mo¿liwo¶æ do³±czania
wtyczek (plug-ins).

%description common -l pt_BR
O Ethereal é um analisador de protocolo de rede baseado no GTK+.


%package -n ethereal-tools
Summary:        Tools for manipulating capture files
Summary(pl):    Narzêdzia do obróbki plików z przechwyconymi pakietami sieciowymi
Group:          Networking
Requires:       ethereal-common = %{version}

%description -n ethereal-tools
Set of tools for manipulating capture files. Contains:
- editcap - Edit and/or translate the format of capture files
- mergecap - Merges two capture files into one
- text2cap - Generate a capture file from an ASCII hexdump of packets

%description -n ethereal-tools -l pl
Zestaw narzêdzi do obróbki plików z przechwyconymi pakietami. Zawiera:
- editcap - do edycji plików i t³umaczenia ich na inne formaty,
- mergecap - do ³±czenia dwóch plików w jeden,
- text2cap - do generowania pliku cap z szesnastkowego zrzutu ASCII
  pakietów.
  

%package -n tethereal
Summary:        Text-mode network traffic and protocol analyzer
Summary(pl):    Tekstowy analizator ruchu i protoko³ów sieciowych
Group:		Networking
Requires:	ethereal-common = %{version}
Requires:	libpcap >= 0.4

%description -n tethereal
Tethereal is a network protocol analyzer.  It lets you capture packet
data from a live network, or read packets from a previously saved
capture file, either printing a decoded form of those packets to the
standard output or writing the packets to a file.  Tethereal's native
capture file format is libpcap format, which is also the format used
by tcpdump and various other tools.

%description -n tethereal -l pl
Tethereal jest analizatorem protoko³ów sieciowych. Pozwala na
przechwytywanie pakietów z sieci lub wczytywanie danych z pliku.
Zdekodowany wynik (a tethereal zna ponad 100 rozmaitych protoko³ów
sieciowych!) jest wy¶wietlony na ekranie. Natywnym formatem plików
tetherala jest format libpcap, tak wiêc jest on kompatybilny
z tcpdumpem i innymi podobnymi narzêdziami.


%prep
%setup -q

%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd epan
rm -f missing
%{__aclocal}
%{__autoconf}
automake -a -c --foreign
cd ../wiretap
%{__aclocal}
%{__autoconf}
automake -a -c --foreign
cd ..
%configure \
		--enable-editcap \
		--enable-idl2eth \
		--enable-mergecap \
		--enable-tethereal \
		--enable-editcap \
		--enable-mergecap \
		--enable-ipv6 \
		--enable-randpkt \
		--enable-text2pcap \
		--enable-zlib \
		--with-pcap \
		--with-ssl \
%{!?_with_gtk1:	--enable-gtk2} \
		--with-plugindir=%{_libdir}/%{name} \
%{!?_without_snmp: --without-snmp}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}_su
install image/ethereal48x48-trans.png \
    $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README{,.[lv]*} doc/{randpkt.txt,README.*}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/editcap
%attr(755,root,root) %{_bindir}/mergecap
%attr(755,root,root) %{_bindir}/randpkt
%attr(755,root,root) %{_bindir}/text2pcap
%{_mandir}/man1/editcap*
%{_mandir}/man1/mergecap*
%{_mandir}/man1/text2pcap*

%files -n tethereal
%attr(755,root,root) %{_bindir}/tethereal
%{_mandir}/man1/tethereal*


%files 
%attr(755,root,root) %{_bindir}/ethereal
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{version}
%{_libdir}/%{name}/plugins/%{version}/*.la
%attr(755,root,root) %{_libdir}/%{name}/plugins/%{version}/*.so
%{_datadir}/%{name}
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*
%{_mandir}/man1/ethereal.1*
