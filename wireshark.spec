#
# WARNING: ethereal.spec and tethereal.spec are using the same source
# file, so they should be keeped in sync!
# I found it easier to do it that way (two separate specs)
# If you know how to do it better feel free to do so.
#
# ethereal an ethereal-common are built from this spec
#
# --with gtk1	builds gtk+1 based ethereal binary
#
 
Summary:	Network traffic and protocol analyzer
Summary(es):	Analizador de tr�fico de red
Summary(pl):	Analizator ruchu i protoko��w sieciowych
Summary(pt_BR): Analisador de tr�fego de rede
Name:		ethereal
Version:	0.9.11
Release:	4
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

%package common
Summary:	Network traffic and protocol analyzer - common files
Summary(pl):	Analizator ruchu i protoko��w sieciowych - wsp�lne pliki
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
		--disable-editcap \
		--disable-idl2eth \
		--disable-mergecap \
		--disable-tethereal \
		--disable-text2pcap \
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

%files 
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{version}
%{_libdir}/%{name}/plugins/%{version}/*.la
%attr(755,root,root) %{_libdir}/%{name}/plugins/%{version}/*.so
%{_datadir}/%{name}
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*
%{_mandir}/man1/*
