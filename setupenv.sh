#!/bin/sh
CURR_DIR=$(cd $(dirname "$0") && pwd)
TMP_DIR=/var/tmp

mkdir -p ${CURR_DIR}/{RPMS,SOURCES,SPECS,SRPMS}
mkdir -p ${TMP_DIR}/{BUILD,BUILDROOT}

cat << EOF > ~/.rpmmacros 
%__xz  /usr/bin/xz
%debug_package %{nil}
%_topdir            ${CURR_DIR}
%_builddir          ${TMP_DIR}/BUILD
%_rpmdir            %{_topdir}/RPMS
%_sourcedir         %{_topdir}/SOURCES
%_specdir           %{_topdir}/SPECS
%_srcrpmdir         %{_topdir}/SRPMS
%_buildrootdir      ${TMP_DIR}/BUILDROOT

%_prefix            /opt
%_exec_prefix		%{_prefix}
%_bindir			%{_exec_prefix}/bin
%_sbindir			%{_exec_prefix}/sbin
%_libexecdir		%{_exec_prefix}/libexec
%_datadir			%{_prefix}/share
%_sysconfdir		/etc
%_sharedstatedir	%{_prefix}/com
%_localstatedir		%{_prefix}/var
%_libdir			%{_exec_prefix}/lib
%_includedir		%{_prefix}/include
%_oldincludedir		/usr/include
%_infodir			%{_prefix}/info
%_mandir			%{_prefix}/man
EOF
