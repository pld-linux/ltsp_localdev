%define		_arch	i386
%define		_pver	4.1

Summary:	Linux Terminal Server Project - local device tools
Summary(pl):	Narzêdzia do urz±dzeñ lokalnych dla terminali z Linux Terminal Server Project
Name:		ltsp_localdev
Version:	4.0.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ltsp.org/ltsp-utils-0.11.tgz
# Source0-md5:	b17b350b18b04d769fcadcd12885a573
Source1:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-localdev-1.2-0-i386.tgz
# Source1-md5:	0f2750bfd151a79e9d48e894645b5e5b
Source2:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-samba-1.3-0-i386.tgz
# Source2-md5:	245ec4396b48227d660af33c2e39609c
URL:		http://www.ltsp.org/
Requires:	ltsp_core
AutoProv:	0
AutoReq:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp
#%define		no_install_post_strip	1

%description
LTSP is an add-on package for Linux that allows you to connect lots of
low-powered thin client terminals to a Linux server. Applications
typically run on the server and accept input and display their output
on the thin client display. LTSP is available as a set of packages that
can be installed on any Linux system.

This package contains local device tools for LTSP terminals.

%description -l pl
LTSP to dodatkowy pakiet dla Linuksa pozwalaj±cy na pod³±czenie wielu
cienkich klientów jako terminali do serwera linuksowego. Aplikacje
zwykle dzia³aj± na serwerze i przyjmuj± wej¶cie oraz wy¶wietlaj±
wyj¶cie na wy¶wietlaczach cienkich klientów. LTSP jest dostêpny jako
zestaw pakietów, które mo¿na zainstalowaæ na dowolnym systemie
linuksowym.

Ten pakiet zawiera narzêdzia obs³uguj±ce lokalne urz±dzenia dla
terminali LTSP.

%prep
%setup -q -n ltsp-utils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}
tar zxf %{SOURCE1}
tar zxf %{SOURCE2}
cd i386
cp -r {sbin,etc,usr} $RPM_BUILD_ROOT%{_ltspdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README
%dir %{_ltspdir}
%attr(755,root,root) %{_ltspdir}/sbin
# XXX: fix perms inside!!!
%{_ltspdir}/etc/*
%{_ltspdir}/usr/*
