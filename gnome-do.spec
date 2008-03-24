%include	/usr/lib/rpm/macros.mono
Summary:	A powerful, speedy, and sexy remote control for your GNOME Desktop
Summary(pl.UTF-8):	Potężne, szybkie i seksowne zdalne sterowanie pulpitem GNOME
Name:		gnome-do
Version:	0.4.0.1
Release:	3
License:	GPL v3
Group:		X11/Applications
Source0:	https://launchpad.net/do/trunk/0.4/+download/%{name}-%{version}.tar.gz
# Source0-md5:	ff3a5d225fd0f23d1357a1e0e461fded
URL:		http://do.davebsd.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	dotnet-ndesk-dbus-sharp-devel
BuildRequires:	mono-csharp >= 1.1.13
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

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/gnome-do/plugins

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	linuxpkgconfigdir=%{_pkgconfigdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gnome-do
%{_libdir}/gnome-do/Do.exe
%{_libdir}/gnome-do/Do.exe.config
%{_libdir}/gnome-do/Do.*.dll
%{_libdir}/gnome-do/Do.*.dll.mdb
%{_libdir}/gnome-do/*.so
%dir %{_datadir}/gnome-do
%dir %{_datadir}/gnome-do/plugins
%{_desktopdir}/gnome-do.desktop
%{_pkgconfigdir}/do.addins.pc
%{_pkgconfigdir}/do.dbus.pc
