Summary:	An application that displays tree structure of disc image
Name:		image-analyzer
Version:	2.1.1
Release:	1
Group:		File tools
License:	GPLv2+
Url:		http://cdemu.sourceforge.net
Source0:	http://downloads.sourceforge.net/cdemu/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libmirage) >= %{version}
Requires:	gnuplot

%description
Image Analyzer is a simple Gtk+ application that displays tree structure
of disc image created by libMirage.

It is mostly intended as a demonstration of libMirage API use, although it
can be also used to verify that an image is correctly handled by libMirage.

%files
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DPOST_INSTALL_HOOKS:BOOL=OFF
%make

%install
%makeinstall_std -C build


