%include	/usr/lib/rpm/macros.mono
Summary:	A powerful, speedy, and sexy remote control for your GNOME Desktop
Summary(pl.UTF-8):	Potężne, szybkie i seksowne zdalne sterowanie pulpitem GNOME
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
%setup -q -n do-0.3

# rewrite script: kill build paths, use proper libdir, avoid . in library path
cat > Do/gnome-do.in <<'EOF'
#!/bin/sh

export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}%{_libdir}/tomboy"
exec mono "%{_libdir}/do/Do.exe" "$@"
EOF

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

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
%dir %{_libdir}/do
%{_libdir}/do/Do.exe
%{_libdir}/do/Do.*.dll
%{_desktopdir}/gnome-do.desktop
%{_pkgconfigdir}/do.addins.pc
%{_pkgconfigdir}/do.dbus.pc
