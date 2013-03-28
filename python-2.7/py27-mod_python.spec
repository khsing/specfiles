%define name py27-mod_python
%define version 3.3.1
%define release k0

Summary: Python Module for Apache
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://archive.apache.org/dist/httpd/modpython/mod_python-%{version}.tgz
License: Apache License, Version 2.0 
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
#BuildArchitectures: noarch
Vendor: Guixing Bai <k@khsing.net>
Url: http://www.modpython.org/
Packager: Guixing Bai <k@khsing.net>
BuildRequires: python27-devel
BuildRequires: httpd-devel
Conflicts: mod_python
%description
mod_python for Apache

%prep
%setup -n mod_python-%{version}
%build
export PYTHON=%{_bindir}/python
export C_INCLUDE_PATH=%{_includedir}
export CPLUS_INCLUDE_PATH=%{_includedir}
export LDFLAGS="-I%{_includedir} -L%{_libdir} -lm -ldl -lutil" 

./configure --with-apxs=/usr/sbin/apxs --with-python=%{_bindir}/python
make %{_smp_mflags}

%install
[ -d "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

#mkdir -p $RPM_BUILD_ROOT%{_libdir}/httpd/modules
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_libdir}/python2.7/site-packages/mod_python
%{_libdir}/python2.7/site-packages/mod_python-3.3.1-py2.7.egg-info
/usr/lib64/httpd/modules/mod_python.so
