Summary:	Tool to show and convert dBASE III, IV, and 5.0 files
Summary(pl):	Narzêdzie do przegl±dania i konwertowania plików dBASE III, IV i 5.0
Name:		dbf
Version:	0.8.3.1
Release:	1
License:	BSD-like
Group:		Applications/System
Source0:	http://download.berlios.de/%{name}/%{name}-%{version}.src.tar.gz
# Source0-md5:	d3e4d93ce6c956e52d12c92fba29c376
URL:		http://www.anubisnet.de/products/dbf
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
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS ChangeLog FAQ README
%attr(755,root,root) %{_bindir}/*
