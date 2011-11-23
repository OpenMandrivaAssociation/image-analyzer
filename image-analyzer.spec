Name:		image-analyzer
Version:	1.4.0
Summary:	MIRAGE Image Analyzer
Release:	1
Source:		http://downloads.sourceforge.net/cdemu/%name-%version.tar.gz
Group:		File tools
License:	GPLv2+
URL:		http://cdemu.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	mirage-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk+extra-2-devel

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

install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=MIRAGE Image Analyzer
Comment=Analyze disc images
Exec=%{_bindir}/%{name}
Icon=data_visualization_section
Type=Application
Categories=GTK;DiscBurning;Utility;
EOF

%files
%doc README AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

