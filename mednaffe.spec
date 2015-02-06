# Seems to have issues when built with optflags, so we don't use them here
%global optflags %{nil}
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A front-end (GUI) for Mednafen emulator
Name:		mednaffe
Version:	0.6
Release:	2
License:	GPLv3+
Group:		Emulators
Url:		https://code.google.com/p/mednaffe/
Source0:	https://sites.google.com/site/amatcoder/mednaffe/downloads/%{name}-%{version}.tar.gz
Patch0:		mednaffe-0.6-error-message.patch
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	mednafen

%description
Mednaffe is a front-end (GUI) for Mednafen emulator.

For now Mednaffe only works with 0.9.3x-WIP versions of mednafen emulator.

%files
%doc COPYING ChangeLog README AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

