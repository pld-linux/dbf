Summary:	Tool to show and convert the content of dBASE III, IV, and 5.0 files.
Summary(pl):	Narzędzie do przeglądania, convertowania zawartości plików dBASE III, IV oraz 5.0
Name:		dbf
Version:	0.6
Release:	0.1
License:	GPL
Group:		Applications/System
#Source0-md5:	6048a2c8096e3f4d9a17639a8646b738
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.src.tar.gz
# Source0-md5: 
URL:		http://anubisnet.sourceforge.net/products/dbf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to show and convert the content of dBASE III, IV, and 5.0

%description -l pl
Narzędzie do przeglądania, convertowania zawartości dBASE III, IV, and
5.0

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}"

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
