Summary:	Tool to show and convert dBASE III, IV, and 5.0 files
Summary(pl):	Narzędzie do przeglądania i konwertowania plików dBASE III, IV i 5.0
Name:		dbf
Version:	0.8.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
# Source0-md5:	21ed7b9a2f1369776de8131b64a8039d
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
%doc BUGS CREDITS ChangeLog FAQ README
%attr(755,root,root) %{_bindir}/*
