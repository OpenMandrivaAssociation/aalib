%define name	aalib
%define version	1.4.0
%define major	1

%define	fname	%{name}-1.4rc5
%define libname	%mklibname aa %major
%define develname %mklibname -d aa
%define staticname %mklibname -s -d aa
%define release	%mkrel 0.rc5.21

Summary:	AA (Ascii Art) library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	LGPLv2+
Group: 		System/Libraries
BuildRequires:	libx11-devel
BuildRequires:  gpm-devel
BuildRequires:	slang-devel
BuildRequires:	texinfo
Source0: 	http://prdownloads.sourceforge.net/aa-project/%{fname}.tar.bz2
Patch0:         %{name}-info.patch
Patch1:		aalib-rpath.patch
Patch2:		aalib-1.4-automake18.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: 		http://aa-project.sourceforge.net/aalib/

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
Obsoletes:	%{name}

%description -n	%{libname}
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!
The AA library is needed for GIMP

%package -n	%develname
Summary:	Header files and libraries for developing apps which will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	libaa-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel
Obsoletes:	%mklibname -d aa 1

%description -n	%develname
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

%package -n	%staticname
Summary:	Static library for developing apps which will use %{name}
Group:		Development/C
Requires:	%develname = %{version}
Provides:	libaa-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%mklibname -d -s aa 1

%description -n	%staticname
Static library for %{name}

%package	progs
Summary:	Tools to %{name}
Group:		Development/C
Requires:	%{libname} = %{version}

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%post -n %develname
%_install_info %{name}.info 

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%preun -n %develname
%_remove_install_info %{name}.info 

%files -n %{libname}
%defattr(-,root,root)
%doc NEWS README
%{_libdir}/libaa.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/aalib-config
%{_libdir}/*.so
%{_libdir}/*.la
%{_infodir}/*.*
%{_includedir}/*
%{_datadir}/aclocal/*
%{_mandir}/man3/*

%files -n %staticname
%defattr(-,root,root)
%doc README
%{_libdir}/*.a

%files progs
%defattr(-,root,root,755)
%doc README
%{_bindir}/aafire
%{_bindir}/aainfo
%{_bindir}/aasavefont
%{_bindir}/aatest
%{_mandir}/man1/*


