%define major 1

%define fname %{name}-1.4rc5
%define libname %mklibname aa %{major}
%define develname %mklibname -d aa
%define staticname %mklibname -s -d aa

Summary:	AA (Ascii Art) library
Name:		aalib
Version:	1.4.0
Release:	0.rc5.25
License:	LGPLv2+
Group:		System/Libraries
Url:		http://aa-project.sourceforge.net/aalib/
Source0:	http://prdownloads.sourceforge.net/aa-project/%{fname}.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		aalib-rpath.patch
Patch2:		aalib-1.4-automake18.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	gpm-devel
BuildRequires:	pkgconfig(slang)
BuildRequires:	texinfo

%description
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!
The AA library is needed for GIMP

%package -n	%{libname}
Summary:	AA (Ascii Art) library
Group:		System/Libraries
Provides:	%{name}

%description -n	%{libname}
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!
The AA library is needed for GIMP

%package -n	%{develname}
Summary:	Header files and libraries for developing apps which will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	libaa-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d aa 1} < 1.4.0-0.rc5.25

%description -n	%{develname}
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!
The AA library is needed for GIMP

Install this package if you want to develop applications that
will use the %{name} library.

%package -n	%{staticname}
Summary:	Static library for developing apps which will use %{name}
Group:		Development/C
Requires:	%{develname} = %{version}
Provides:	libaa-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d -s aa 1} < 1.4.0-0.rc5.25

%description -n	%{staticname}
Static library for %{name}

%package	progs
Summary:	Tools to %{name}
Group:		Development/C

%description progs
AA-lib tools.

%prep
%setup -q
%patch0 -p1 -b .info
%patch1 -p0 -b .rpath
%patch2 -p1 -b .automake18

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%doc NEWS README
%{_libdir}/libaa.so.%{major}*

%files -n %{develname}
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/aalib-config
%{_libdir}/*.so
%{_infodir}/*.*
%{_includedir}/*
%{_datadir}/aclocal/*
%{_mandir}/man3/*

%files -n %{staticname}
%doc README
%{_libdir}/*.a

%files progs
%doc README
%{_bindir}/aafire
%{_bindir}/aainfo
%{_bindir}/aasavefont
%{_bindir}/aatest
%{_mandir}/man1/*

%changelog
* Wed Dec 28 2011 Andrey Bondrov <abondrov@mandriva.org> 1.4.0-0.rc5.23mdv2012.0
+ Revision: 745922
- Rebuild for .la files issue

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-0.rc5.22
+ Revision: 662748
- mass rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - drop multiarch stuff as aalib-config no longer contains arch specific flags

* Wed Jan 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-0.rc5.21mdv2011.0
+ Revision: 628709
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - tighten BR

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-0.rc5.20mdv2011.0
+ Revision: 603166
- rebuild

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 1.4.0-0.rc5.19mdv2010.1
+ Revision: 506947
- rebuild for missing SRPM

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-0.rc5.18mdv2010.0
+ Revision: 413018
- rebuild

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 1.4.0-0.rc5.17mdv2009.0
+ Revision: 217182
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Wed Oct 24 2007 Götz Waschk <waschk@mandriva.org> 1.4.0-0.rc5.17mdv2008.1
+ Revision: 101718
- new devel name
- update license tag

* Fri Jun 01 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.4.0-0.rc5.17mdv2008.0
+ Revision: 34287
- Rebuild with libslang2.


* Mon Aug 21 2006 Emmanuel Andry <eandry@mandriva.org> 1.4.0-0.rc5.16mdv2007.0
- %%mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.4.0-0.rc5.15mdk
- Rebuild

* Wed Feb 09 2005 Abel Cheung <deaddog@mandrake.org> 1.4.0-0.rc5.14mdk
- Use automake 1.9
- P2: compatibility with automake >= 1.8

* Tue Feb 01 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4.0-0.rc5.13mdk
- multiarch
- fix summary-ended-with-dot

* Fri Jul 23 2004 Marcel Pol <mpol@mandrake.org> 1.4.0-0.rc5.12mdk
- ouch, need coffee

* Fri Jul 23 2004 Marcel Pol <mpol@mandrake.org> 1.4.0-0.rc5.11mdk
- again build against new slang

* Wed Jul 21 2004 Marcel Pol <mpol@mandrake.org> 1.4.0-0.rc5.10mdk
- build against new slang

* Mon Jun 07 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4.0-0.rc5.9mdk
- force use of automake1.7 and autoconf2.5
- wipe out buildroot before installing
- cosmetics

