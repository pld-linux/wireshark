Summary:	Network traffic and protocol analyzer
Summary(es): Analizador de tráfico de red.
Summary(pl):	Analizator ruchu i protoko³ów sieciowych
Summary(pt_BR): Analisador de tráfego de rede
Name:		ethereal
Version:	0.9.5
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.ethereal.com/distribution/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.su-start-script
URL:		http://www.ethereal.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libpcap-devel >= 0.4
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	ucd-snmp-devel >= 4.2.5
BuildRequires:	zlib-devel
Requires:	libpcap >= 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/usr/share/misc

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

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
cd epan
rm -f missing
aclocal
%{__autoconf}
%{__automake}
cd ../wiretap
aclocal
%{__autoconf}
%{__automake}
cd ..
%configure \
	--disable-static \
	--enable-editcap \
	--enable-mergecap \
	--enable-ipv6 \
	--enable-randpkt \
	--enable-text2pcap \
	--enable-zlib \
	--with-pcap \
	--with-plugindir=%{_libdir}/ethereal \
	--with-ssl \
	--with-ucdsnmp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_datadir}/pixmaps}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install image/ethereal48x48-trans.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/ethereal.png
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/ethereal_su

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README* doc/randpkt.txt doc/README.developer
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Misc/ethereal.desktop
%{_sysconfdir}/manuf
%{_mandir}/man1/*
%{_pixmapsdir}/*
%dir %{_libdir}/ethereal
%attr(755,root,root) %{_libdir}/ethereal/*
