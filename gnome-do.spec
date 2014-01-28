%include	/usr/lib/rpm/macros.mono
Summary:	A powerful, speedy, and sexy remote control for your GNOME Desktop
Summary(pl.UTF-8):	Potężne, szybkie i seksowne zdalne sterowanie pulpitem GNOME
Name:		gnome-do
Version:	0.95.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://edge.launchpad.net/do/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	1f61376718d75d3defcdf81958754296
URL:		http://do.davebsd.com/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	dotnet-gio-sharp-devel
BuildRequires:	dotnet-gkeyfile-sharp-devel
BuildRequires:	dotnet-gnome-desktop-sharp-devel
BuildRequires:	dotnet-gnome-keyring-sharp-devel
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	dotnet-ndesk-dbus-sharp-devel
BuildRequires:	dotnet-notify-sharp-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	intltool
BuildRequires:	librsvg
BuildRequires:	libtool
BuildRequires:	mono-addins-devel
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xdg-utils
Suggests:	gnome-do-docklets
Suggests:	gnome-do-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Do allows you to quickly search for many items present in your
GNOME desktop environment (applications, Evolution contacts, Firefox
bookmarks, files, artists and albums in Rhythmbox, Pidgin buddies,
etc.) and perform commonly used actions on those items (Run, Open,
Email, Chat, Play, etc.).

%description -l pl.UTF-8
GNOME Do pozwala szybko przeszukać wiele elementów obecnych w
środowisku GNOME (aplikacje, kontakty w Evolution, zakładki w
Firefoksie, pliki, wykonawców i albumy w Rhythmboksie, osoby w
Pidginie itp.) i wykonywać na nich popularne czynności (uruchamiać,
otwierać, wysyłać e-maile, rozmawiać, odtwarzać...).

%package devel
Summary:	Development information for GNOME Do plugins
Summary(pl.UTF-8):	Informacje programistyczne dla wtyczek GNOME Do
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development information for GNOME Do plugins.

%description devel -l pl.UTF-8
Informacje programistyczne dla wtyczek GNOME Do.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4/shamrock
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	linuxpkgconfigdir=%{_pkgconfigdir}

for s in 16 24 32 48 64 128 ; do
	rsvg-convert -w $s -h $s -f png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/${s}x${s}/apps/gnome-do.svg \
		>$RPM_BUILD_ROOT%{_iconsdir}/hicolor/${s}x${s}/apps/gnome-do.png
	%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/${s}x${s}/apps/gnome-do.svg
done

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-do/*.la

%find_lang %{name} --with-gnome

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gnome-do
%attr(755,root,root) %{_libdir}/gnome-do/*.so
%attr(755,root,root) %{_libdir}/gnome-do/Do.exe
%{_libdir}/gnome-do/Do.addins
%{_libdir}/gnome-do/Do.exe.mdb
%{_libdir}/gnome-do/Do.*.dll
%{_libdir}/gnome-do/Do.*.dll.config
%{_libdir}/gnome-do/Do.*.dll.mdb
%{_libdir}/gnome-do/gio-sharp.dll
%{_libdir}/gnome-do/gio-sharp.dll.config
%{_sysconfdir}/xdg/autostart/gnome-do.desktop
%{_desktopdir}/gnome-do.desktop
%{_sysconfdir}/gconf/schemas/gnome-do.schemas
%{_iconsdir}/hicolor/*/apps/gnome-do.png
%{_iconsdir}/hicolor/*/apps/gnome-do.svg

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/do.platform.pc
%{_pkgconfigdir}/do.platform.linux.pc
%{_pkgconfigdir}/do.interface.linux.pc
%{_pkgconfigdir}/do.interface.linux.animationbase.pc
%{_pkgconfigdir}/do.universe.pc
