Summary:	Network traffic and protocol analyzer
Summary(pl):	Analizator ruchu i protoko³ów sieciowych
Name:		ethereal
Version:	0.8.9
Release:	1
License:	GPL
Group:		Networking
Group(pl):	Sieciowe
Source0:	http://ethereal.zing.org/distribution/%{name}-%{version}.tar.gz
Source1:	ethereal.desktop
Patch0:		ethereal-paths.patch
URL:		http://ethereal.zing.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+ >= 1.2
Requires:	libpcap >= 0.4
BuildRequires:	libpcap-devel >= 0.4
BuildRequires:	zlib-devel
BuildRequires:	gtk+-devel >= 1.2

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc

%description
Ethereal is the name for powerful graphical network sniffer, traffic
and protocol analyzer based on GTK+ and libpcap libraries. It lets you
capture and interactively browse the contents of network frames with
vast knowledge of more than 100 network protocols. Ethereal has
severeal useful features, including a rich display filter language,
the ability to view the ASCII contents of a TCP connection and plug-in
capabilities.

%description -l pl
Ethereal jest potê¿nym, graficznym snifferem, analizatorem ruchu oraz
protoko³ów sieciowych opartym na bibliotekach GTK+ oraz libpcap.
Umo¿liwia on przechwytywanie oraz intereaktywn± analizê zawarto¶ci
ramek oraz ponad stu protoko³ów sieciowych. Ethereal posiada wiele
u¿ytecznych cech, takich jak rozbudowany jêzyk filtrów wy¶wietlania,
mo¿liwo¶æ ogl±dania przebiegu sesji TCP oraz mo¿liwo¶æ do³±czania
wtyczek (plug-ins).

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"
# don't remove -DINET6=1 because --enable-ipv6 doesn't work properly
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/pcap -DINET6=1"
export LDFLAGS CFLAGS
%configure \
	--enable-zlib \
	--disable-snmp \
	--enable-pcap \
	--with-gnu-ld \
	--enable-ipv6 \
	--disable-static \
	--with-plugindir=%{_libdir}/ethereal
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

gzip -9nf AUTHORS NEWS README* doc/randpkt.txt \
	doc/README.developer $RPM_BUILD_ROOT%{_mandir}/man1/*

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/ethereal/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Misc/ethereal.desktop
%config %{_sysconfdir}/manuf
%{_mandir}/man1/*
%dir %{_libdir}/ethereal
%attr(755,root,root) %{_libdir}/ethereal/*
