%define name py27-cairo
%define version 1.10.0
%define release k1

Summary: Python Bindings for Cairo
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://cairographics.org/releases/py2cairo-%{version}.tar.bz2
License: LGPL or MPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
#BuildArchitectures: noarch
Vendor: Guixing Bai <k@khsing.net>
Url: http://cairographics.org/pycairo
Packager: Guixing Bai <k@khsing.net>
BuildRequires: python27-devel
BuildRequires: glibc-devel
BuildRequires: cairo-devel

%description
Python bindings for cairo.

%prep
%setup -n py2cairo-%{version}
%build
export PYTHON=%{_bindir}/python
export C_INCLUDE_PATH=%{_includedir}
export CPLUS_INCLUDE_PATH=%{_includedir}
#export CFLAGS="-l%{_includedir}"
export LDFLAGS="-I%{_includedir} -L%{_libdir} -lm -ldl -lutil" 

./waf --prefix=%{_prefix} --libdir=%{_libdir} configure 
./waf %{?_smp_mflags} build

%install
./waf install --destdir=$RPM_BUILD_ROOT

# rm -f $RPM_BUILD_ROOT/usr/bin/easy_install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc
%{_libdir}/python2.7/site-packages/cairo/__init__.py
%{_libdir}/python2.7/site-packages/cairo/__init__.pyc
%{_libdir}/python2.7/site-packages/cairo/__init__.pyo
%{_libdir}/python2.7/site-packages/cairo/_cairo.so

