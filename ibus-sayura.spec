Summary:	The Sinhala engine for IBus input platform
Name:		ibus-sayura
Version:	1.3.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://fedorahosted.org/releases/i/b/ibus-sayura/%{name}-%{version}.tar.gz
# Source0-md5:	97074cccdaad1332d470aee92fac645e
URL:		https://fedorahosted.org/ibus-sayura
BuildRequires:	ibus-devel
BuildRequires:	pkgconfig
Requires:	ibus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Sayura engine for IBus platform. It provides Sinhala input method.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-sayura
%{_datadir}/ibus-sayura
%{_datadir}/ibus/component/sayura.xml
