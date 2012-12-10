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



%changelog
* Fri Feb 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.5.0-1
+ Revision: 780052
- new version 1.5.0

* Wed Nov 23 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.4.0-1
+ Revision: 732985
- version bump 1.4.0

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1.svn635.3mdv2011.0
+ Revision: 611178
- rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild for new libmirage

* Fri May 21 2010 Anssi Hannula <anssi@mandriva.org> 1.0.0-1.svn635.1mdv2010.1
+ Revision: 545659
- newer snapshot that works with current libmirage

* Thu Jul 09 2009 Anssi Hannula <anssi@mandriva.org> 1.0.0-1.svn303.3mdv2010.0
+ Revision: 394011
- rebuild

* Wed Apr 23 2008 Anssi Hannula <anssi@mandriva.org> 1.0.0-1.svn303.2mdv2009.0
+ Revision: 197033
- fix group

* Wed Apr 23 2008 Anssi Hannula <anssi@mandriva.org> 1.0.0-1.svn303.1mdv2009.0
+ Revision: 196933
- initial Mandriva release

