Summary:	Network traffic and protocol analyzer
Summary(pl):	Analizator ruchu i protoko³ów sieciowych
Name:		ethereal
Version:	0.8.3
Release:	1
License:	GPL
Group:		Networking
Group(pl):	Sieciowe
Source0:	http://ethereal.zing.org/distribution/%{name}-%{version}.tar.gz
Source1:	ethereal.desktop
Patch0:		ethereal-paths.patch
Url:		http://ethereal.zing.org
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	gtk+ >= 1.2
Requires:	libpcap >= 0.4
BuildRequires:	libpcap-devel >= 0.4
BuildRequires:	zlib-devel

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Ethereal is the name for powerful graphical network sniffer, traffic 
and protocol analyzer based on GTK+ and libpcap libraries. It lets you 
capture and interactively browse the contents of network frames with 
vast knowledge of more than 100 network protocols. Ethereal has severeal 
useful features, including a rich display filter language, the ability
to view the ASCII contents of a TCP connection and plug-in capabilities.


%description -l pl
Ethereal jest potê¿nym, graficznym, snifferem, analizatorem ruchu oraz 
protoko³ów sieciowych opartym na bibliotekach GTK+ oraz libpcap. Umo¿liwia
on przechwytywanie oraz intereaktywne analizowanie zawarto¶ci ramek oraz
ponad stu protoko³ów sieciowych. Ethereal posiada wiele u¿ytecznych cech,
takich jak rozbudowany jêzyk filtrów wy¶wietlania, mo¿liwo¶æ ogl±dania
przebiegu sesji TCP oraz mo¿liwo¶æ do³¶czania wtyczek (plug-ins).

 
%prep
%setup -q
%patch -p0

%build

LDFLAGS="-s"; export LDFLAGS

CC="gcc -I%{_includedir}/pcap" CFLAGS="$RPM_OPT_FLAGS" \
./configure \
   --prefix=%{_prefix} \
   --bindir=%{_bindir} \
   --mandir=%{_mandir} \
   --sysconfdir=/etc \
   --enable-zlib \
   --disable-snmp \
   --enable-pcap \
   --with-gnu-ld \
   --with-plugin=%{_libdir}/ethereal/plugins \
   --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_datadir}/applnk/Networking
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Networking/
install -d $RPM_BUILD_ROOT/usr/share/doc

gzip -9nf AUTHORS ChangeLog INSTALL NEWS README* doc/randpkt.txt  
gzip -9nf doc/proto_tree $RPM_BUILD_ROOT%{_mandir}/man1/*

find $RPM_BUILD_ROOT%{_libdir}/ethereal/plugins -type f -name "*.so" \
| xargs -n1 strip -s


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applnk/Networking/ethereal.desktop
%config /etc/manuf
%{_mandir}/man1/*
%dir %{_libdir}/ethereal
%dir %{_libdir}/ethereal/plugins/0.8/
%{_libdir}/ethereal/plugins/0.8/*
%doc AUTHORS.gz ChangeLog.gz INSTALL.gz NEWS.gz README*.gz doc/*.gz
