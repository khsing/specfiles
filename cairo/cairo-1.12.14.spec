%define name cairo
%define version 1.12.14
%define release k0
%define _without_directfb yes

Summary: Cairo is a 2D graphics library with support for multiple output devices.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://cairographics.org/releases/cairo-%{version}.tar.xz
License: LGPL or MPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
Vendor: Guixing Bai <k@khsing.net>
Url: http://cairographics.org
Packager: Guixing Bai <k@khsing.net>
%description
Cairo is a 2D graphics library with support for multiple output devices.

BuildRequires: pkgconfig, freetype-devel, libpixman-devel
BuildRequires: libpng-devel, gcc-c++


%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
#Requires: libpixman-devel, XFree86-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{version}

#cd %{_builddir}
#rm -rf %{name}-%{version}
#/usr/bin/xz -dc %{_sourcedir}/cairo-%{version}.tar.xz | tar -xvvf -
#if [ $? -ne 0 ]; then
#  exit $?
#fi
#cd %{_builddir}/cairo-%{version}
#chown -R root.root .
#chmod -R a+rX,g-w,o-w .

%build
#export PYTHON=%{_bindir}/python
#export C_INCLUDE_PATH=%{_includedir}
#export CPLUS_INCLUDE_PATH=%{_includedir}
#export CFLAGS="-l%{_includedir}"
#export LDFLAGS="-I%{_includedir} -L%{_libdir}" 

%{?_without_pkgconfig:export png_CFLAGS="$(libpng-config --cflags)"}
%{?_without_pkgconfig:export png_LIBS="$(libpng-config --libs)"}
%{?_without_pkgconfig:export png_REQUIRES=" "}
cd %{_builddir}/cairo-%{version}
./configure \
    --prefix=%{_prefix} \
    --disable-static \
    --enable-shared \
    --enable-xlib=no
make %{?_smp_mflags}

%install
#cd %{_builddir}/cairo-%{version}
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libcairo.so.*
%{_bindir}/cairo-trace
%{_libdir}/cairo
%{_libdir}/libcairo-script-interpreter.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/cairo/
%{_includedir}/cairo/
%{_libdir}/libcairo.so
%{_libdir}/pkgconfig/cairo.pc
%{_libdir}/pkgconfig/cairo-*.pc
%exclude %{_libdir}/libcairo.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig