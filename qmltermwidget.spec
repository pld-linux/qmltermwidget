#
# Conditional build:
%bcond_with	tests		# build with tests
#
# TODO:
# - runtime Requires if any

%define		qtver		5.15.2
%define		kfname		qmltermwidget
Summary:	Port of qtermwidget
Name:		qmltermwidget
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	https://github.com/Swordfish90/qmltermwidget/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	1a5c76f0af285f1281549498f7e8c2e9
Patch0:		cwctype.patch
URL:		https://github.com/Swordfish90/qmltermwidget
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is a QML port of qtermwidget.

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt5
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%dir %{_libdir}/qt5/qml/QMLTermWidget
%{_libdir}/qt5/qml/QMLTermWidget/QMLTermScrollbar.qml
%dir %{_libdir}/qt5/qml/QMLTermWidget/color-schemes
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/BlackOnLightYellow.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/BlackOnRandomLight.colorscheme
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/BlackOnWhite.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/BreezeModified.colorscheme
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/DarkPastels.colorscheme
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/GreenOnBlack.colorscheme
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/Linux.colorscheme
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/Solarized.colorscheme
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/SolarizedLight.colorscheme
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/Tango.colorscheme
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/Ubuntu.colorscheme
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/WhiteOnBlack.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/cool-retro-term.schema
%dir %{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/BlackOnLightColor.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/DarkPicture.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/Example.Schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/GreenOnBlack.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/GreenTint.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/GreenTint_MC.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/LightPicture.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/Linux.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/README.Schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/README.default.Schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/Transparent.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/Transparent_MC.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/Transparent_darkbg.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/Transparent_lightbg.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/XTerm.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/syscolor.schema
%{_libdir}/qt5/qml/QMLTermWidget/color-schemes/historic/vim.schema
%dir %{_libdir}/qt5/qml/QMLTermWidget/kb-layouts
%{_libdir}/qt5/qml/QMLTermWidget/kb-layouts/README
%{_libdir}/qt5/qml/QMLTermWidget/kb-layouts/default.keytab
%dir %{_libdir}/qt5/qml/QMLTermWidget/kb-layouts/historic
%{_libdir}/qt5/qml/QMLTermWidget/kb-layouts/historic/vt100.keytab
%{_libdir}/qt5/qml/QMLTermWidget/kb-layouts/historic/x11r5.keytab
%{_libdir}/qt5/qml/QMLTermWidget/kb-layouts/linux.keytab
%{_libdir}/qt5/qml/QMLTermWidget/kb-layouts/macbook.keytab
%{_libdir}/qt5/qml/QMLTermWidget/kb-layouts/solaris.keytab
%{_libdir}/qt5/qml/QMLTermWidget/kb-layouts/vt420pc.keytab
%attr(755,root,root) %{_libdir}/qt5/qml/QMLTermWidget/libqmltermwidget.so
%{_libdir}/qt5/qml/QMLTermWidget/qmldir
