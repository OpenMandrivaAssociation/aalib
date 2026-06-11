%define fname %{name}-1.4rc5

%define major 1
%define libname %mklibname aa %{major}
%define devname %mklibname aa -d

# add workaround for new Clang failures
%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration
%global optflags %{optflags} -std=gnu17

Summary:	AA (Ascii Art) library
Name:		aalib
Version:	1.4.0
Release:	0.rc5.32
License:	LGPLv2+
Group:		System/Libraries
Url:		https://aa-project.sourceforge.net/aalib/
Source0:	http://prdownloads.sourceforge.net/aa-project/%{fname}.tar.bz2
Patch0:		aalib-info.patch
Patch1:		aalib-rpath.patch
Patch2:		aalib-1.4-automake18.patch
Patch3:		aalib-1.4.0-automake-1.13.patch
Patch4:		aalib-1.4.0-texinfo-5.x.patch

Patch5:         aalib-1.4rc5-bug149361.patch
Patch6:         aalib-c99.patch
Patch7:         https://gitweb.gentoo.org/repo/gentoo.git/plain/media-libs/aalib/files/aalib-1.4_rc5-free-offset-pointer.patch
	
Patch8:         https://gitweb.gentoo.org/repo/gentoo.git/plain/media-libs/aalib/files/aalib-1.4_rc5-fix-aarender.patch
# Modern ncurses has an opaque WINDOW structure (you cannot address its members directly)
# Use the getmaxx() and getmaxy() functions provided by ncurses instead.
Patch9:		aalib-1.4rc5-opaque-ncurses-fix.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	texinfo
BuildRequires:	gpm-devel
BuildRequires:	pkgconfig(slang)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(ncurses)

%description
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!
The AA library is needed for GIMP

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	AA (Ascii Art) library
Group:		System/Libraries

%description -n %{libname}
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!
The AA library is needed for GIMP

%files -n %{libname}
%doc NEWS README
%{_libdir}/libaa.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header files and libraries for developing apps which will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	slang-devel
Requires:	gpm-devel
Provides:	libaa-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}aa-static-devel < 1.4.0-0.rc5.27

%description -n %{devname}
Install this package if you want to develop applications that
will use the %{name} library.

%files -n %{devname}
%doc README ChangeLog
%{_bindir}/aalib-config
%{_libdir}/*.so
%{_infodir}/*.*
%{_includedir}/*
%{_datadir}/aclocal/*
%{_mandir}/man3/*

#----------------------------------------------------------------------------

%package progs
Summary:	Tools to %{name}
Group:		Development/C

%description progs
AA-lib tools.

%files progs
%doc README
%{_bindir}/aafire
%{_bindir}/aainfo
%{_bindir}/aasavefont
%{_bindir}/aatest
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
export CC=gcc
ln -sf %{_bindir}/libtoolize slibtoolize
export PATH=$PWD:$PATH
export LIBTOOLIZE=%{_bindir}/libtoolize
export LIBTOOL=%{_bindir}/libtool
autoreconf -fi
ln -sf %{_bindir}/libtoolize slibtoolize
export PATH=$PWD:$PATH
export LIBTOOLIZE=%{_bindir}/libtoolize
export LIBTOOL=%{_bindir}/libtool
%configure \
	--disable-static \
	--with-curses-driver=yes \
	--with-ncurses

%make_build

%install
%make_install

