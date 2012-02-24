Name:		image-analyzer
Version:	1.5.0
Summary:	MIRAGE Image Analyzer
Release:	1
Group:		File tools
License:	GPLv2+
URL:		http://cdemu.sourceforge.net/
Source0:	http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libmirage)

%description
This is MIRAGE Image Analyzer, a simple Gtk+ application that
displays tree structure of disc image created by libMirage. It is
mostly intended as a demonstration of libMirage API use, although it
can be also used to verify that an image is correctly handled by
libMirage.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

