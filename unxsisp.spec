# TODO:
# - allow CC and *FLAGS in makefile
# - FHS: those .cgi are binary, move them to libdir
Summary:	Manage ISP customers, resellers and their resources. Centralize resource and product usage
Name:		unxsisp
Version:	1.0
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://unixservice.com/source/%{name}-%{version}.tar.gz
# Source0-md5:	746038c0509f05d73edb725e0ff3afe3
URL:		http://openisp.net/openisp/unxsVZ
Patch0:		%{name}-include.patch
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	sed >= 4.0
BuildRequires:	ucidr
BuildRequires:	unxstemplate
BuildRequires:	zlib-devel
Requires:	unxsadmin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manage ISP customers, resellers and their resources. Centralize
resource and product usage. This software also centralizes customer
data for all the other Unixservice applications, to avoid unnecessary
data duplication. All Unixservice ISP management applications can be
controlled with this backend.

%prep
%setup -q
%patch0 -p1
%{__sed} -e 's/getline/unx_getline/' -i cgi.c

%build
%{__make} \
	libdir=%{_libdir}

%{__make} -C interfaces/admin/ \
	libdir=%{_libdir}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/unxs/{,cgi-bin}
install -s unxsISP.cgi $RPM_BUILD_ROOT%{_datadir}/unxs/cgi-bin/unxsISP.cgi
install -s interfaces/admin/interface.cgi $RPM_BUILD_ROOT%{_datadir}/unxs/cgi-bin/ispAdmin.cgi
install -d $RPM_BUILD_ROOT%{_datadir}/unxsISP/data
cp data/*.txt $RPM_BUILD_ROOT%{_datadir}/unxsISP/data

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL LICENSE
%{_datadir}/unxs/cgi-bin/unxsISP.cgi
%{_datadir}/unxs/cgi-bin/ispAdmin.cgi
%dir %{_datadir}/unxsISP/data
%{_datadir}/unxsISP/data/*
