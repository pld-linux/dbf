Summary:	Tool to show and convert dBASE III, IV, and 5.0 files
Summary(pl):	Narzêdzie do przegl±dania i konwertowania plików dBASE III, IV i 5.0
Name:		dbf
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
# Source0-md5:	048ac02835d73d845d4d547351924394
URL:		http://anubisnet.sourceforge.net/products/dbf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to show and convert the content of dBASE III, IV, and 5.0.

%description -l pl
Narzêdzie do przegl±dania oraz konwertowania zawarto¶ci dBASE III, IV
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
