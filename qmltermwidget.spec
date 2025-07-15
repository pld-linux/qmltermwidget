%define		qt_ver		5.15.2
Summary:	QML port of qtermwidget
Summary(pl.UTF-8):	Port komponentu qtermwidget do QML
Name:		qmltermwidget
Version:	0.2.0
Release:	2
License:	GPL v2+
Group:		X11/Libraries
#Source0Download: https://github.com/Swordfish90/qmltermwidget/releases
# TODO:
#Source0:	https://github.com/Swordfish90/qmltermwidget/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/Swordfish90/qmltermwidget/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	1a5c76f0af285f1281549498f7e8c2e9
Patch0:		cwctype.patch
URL:		https://github.com/Swordfish90/qmltermwidget
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5Qml >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is a QML port of qtermwidget.

%description -l pl.UTF-8
Ten projekt to port QML komponentu qtermwidget.

%prep
%setup -q
%patch -P0 -p1

%build
%qmake_qt5

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%dir %{_libdir}/qt5/qml/QMLTermWidget
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes
%{_libdir}/qt5/qml/QMLTermWidget/kb-layouts
%attr(755,root,root) %{_libdir}/qt5/qml/QMLTermWidget/libqmltermwidget.so
%{_libdir}/qt5/qml/QMLTermWidget/QMLTermScrollbar.qml
%{_libdir}/qt5/qml/QMLTermWidget/qmldir
