%include	/usr/lib/rpm/macros.mono
Summary:	-
Summary(pl.UTF-8):	-
Name:		gnome-do
Version:	0.3.0.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://do.davebsd.com/src/%{name}_%{version}.tar.gz
# Source0-md5:	b37928cbad12155e10304a5787e73ca2
URL:		http://do.davebsd.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	dotnet-ndesk-dbus-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	mono-csharp >= 1.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n do-0.3

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/gnome-do.desktop
%{_libdir}/do
%{_pkgconfigdir}/do.*.pc
