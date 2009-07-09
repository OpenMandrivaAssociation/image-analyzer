
%define version 1.0.0
%define snapshot 303
%define rel	3

%if 0
# Update commands:
REV=$(svn info https://cdemu.svn.sourceforge.net/svnroot/cdemu/trunk/image-analyzer| sed -ne 's/^Last Changed Rev: //p')
svn export -r $REV https://cdemu.svn.sourceforge.net/svnroot/cdemu/trunk/image-analyzer image-analyzer-$REV
tar -cjf image-analyzer-$REV.tar.bz2 image-analyzer-$REV
%endif

Name:		image-analyzer
Version:	%version
Summary:	MIRAGE Image Analyzer
%if %snapshot
Release:	%mkrel 1.svn%snapshot.%rel
Source:		%name-%snapshot.tar.bz2
%else
Release:	%mkrel %rel
Source:		http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2
%endif
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
%if %snapshot
%setup -q -n %name-%snapshot
%else
%setup -q
%endif

%build
%if %snapshot
./autogen.sh
%endif
%configure2_5x
%make

%install
rm -rf %buildroot
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

