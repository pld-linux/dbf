Summary:	Tool to show and convert dBASE III, IV, and 5.0 files
Summary(pl):	Narzędzie do przeglądania i konwertowania plików dBASE III, IV i 5.0
Name:		dbf
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/System
#Source0-md5:	6048a2c8096e3f4d9a17639a8646b738
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
URL:		http://anubisnet.sourceforge.net/products/dbf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to show and convert the content of dBASE III, IV, and 5.0.

%description -l pl
Narzędzie do przeglądania oraz konwertowania zawartości dBASE III, IV
i 5.0.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG FAQ README
%attr(755,root,root) %{_bindir}/*
