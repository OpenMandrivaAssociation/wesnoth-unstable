# TODO add a init file for server, if it is worth
# split data if we can force a rpm to be noarch

%define sname wesnoth

Summary:	Fantasy turn-based strategy game
Name:		wesnoth-unstable
Version:	1.9.12
Release:	%mkrel 1
License:	GPLv2+
Group:		Games/Strategy
Url:		http://www.wesnoth.org/
Source0:	http://downloads.sourceforge.net/%{sname}/%{sname}-%{version}.tar.bz2
Source1:	%{sname}-icon.png
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	boost-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	imagemagick
BuildRequires:	python-devel
BuildRequires:	lua-devel >= 5.1.4
BuildRequires:	cmake
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(pango)
BuildRequires:	fontconfig-devel
BuildRequires:	dbus-devel
BuildRequires:	fribidi-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
Conflicts:	%{sname}

%description
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which
have advantages and disadvantages in different types of terrains and
against different types of attacks. Units gain experience and advance
levels, and are carried over from one scenario to the next campaign.

%package -n %{name}-server
Summary:	Server for "Battle fo Wesnoth" game
Group:		Games/Strategy
Conflicts:	%{sname}-server

%description -n	%{name}-server
This package contains "Battle for wesnoth" server, used to play multiplayer
game without needing to install the full client.

%prep
%setup -q -n %{sname}-%{version}

%build
export LDFLAGS="$LDFLAGS -lpthread"
%cmake -DENABLE_STRICT_COMPILATION=OFF \
	-DBINDIR=%{_gamesbindir} \
	-DDATAROOTDIR=%{_gamesdatadir} \
	-DDESKTOPDIR=%{_datadir}/applications \
	-DDOCDIR=%{_datadir}/doc/%{sname} \
	-DMANDIR=%{_mandir} -DICONDIR=%{_iconsdir}
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%find_lang %{sname} --with-man
%find_lang %{sname}d --with-man

%clean
rm -rf %{buildroot}

%files -f %{sname}.lang
%defattr(-,root,root,0755)
%doc README
%exclude %{_gamesbindir}/%{sname}d
%{_gamesbindir}/*
%{_gamesdatadir}/%{sname}
%{_mandir}/*/%{sname}.*
%{_datadir}/applications/*
%{_datadir}/doc/%{sname}/*
%{_iconsdir}/*

%files -n %{name}-server -f %{sname}d.lang
%defattr(-,root,root,0755)
%{_gamesbindir}/%{sname}d
%{_mandir}/*/%{sname}d.*

