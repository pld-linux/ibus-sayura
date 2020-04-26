Summary:	The Sinhala engine for IBus input platform
Summary(pl.UTF-8):	Silnik metody Sinhala dla platformy wprowadzania IBus
Name:		ibus-sayura
Version:	1.3.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://releases.pagure.org/ibus-sayura/%{name}-%{version}.tar.gz
# Source0-md5:	a35b3da5f973164d85d3498d29ad3650
URL:		https://pagure.io/ibus-sayura
BuildRequires:	gettext-tools >= 0.16.1
BuildRequires:	ibus-devel >= 1.2.99
BuildRequires:	pkgconfig
Requires:	ibus >= 1.2.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Sayura engine for IBus platform. It provides Sinhala input method.

%description -l pl.UTF-8
Silnik Sayura dla platformy IBus. Udostępnia metodę wprowadzania
Sinhala.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# only single empty translation (zh_CN) exists
#find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libexecdir}/ibus-engine-sayura
%{_datadir}/ibus-sayura
%{_datadir}/ibus/component/sayura.xml
