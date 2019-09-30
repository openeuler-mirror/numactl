Name: numactl
Version: 2.0.12
Release: 2
Summary: Library for tuning for Non Uniform Memory Access machines
License: GPLv2
URL: https://github.com/numactl/numactl
Source0: https://github.com/numactl/numactl/releases/download/v2.0.12/numactl-2.0.12.tar.gz
BuildRequires: libtool automake autoconf git

Patch6000: 0007-Fix-Add-ShmemHugePages-and-ShmemPmdMapped-to-system_.patch
Patch6001: 0008-add-missing-policy.patch
Patch6002: 0013-numactl-add-va_end-to-usage-function.patch
Patch6003: 0014-libnuma-cleanup-node-cpu-mask-in-destructor.patch
Patch6004: 0021-Removed-unnecessary-exit-from-memhog.c.patch
Patch6005: 0022-Correct-sysconf-constants.patch
Patch6006: 0024-numastat-Better-diagnostic-when-find-unknown-string-.patch
Patch6007: 0025-numastat-Add-KReclaimable-to-list-of-known-fields-in.patch

%description
Simple NUMA policy support. It consists of a numactl program to run other
programs with a specific NUMA policy and a libnuma shared library  to set
NUMA policy in applications.

%package libs
Summary: libnuma libraries
License: LGPLv2 and GPLv2

%description libs
Libs for numa policy support

%package devel
Summary: Development package for building Applications that use numa
Requires: %{name}-libs = %{version}-%{release}
License: LGPLv2 and GPLv2

%description devel
Development package for numa library calls

%prep
%autosetup -n %{name}-%{version} -p1 -Sgit

%build
%configure
%disable_rpath
%make_build CFLAGS="$RPM_OPT_FLAGS -I."

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig

%files
%{_bindir}/memhog
%{_bindir}/migspeed
%{_bindir}/migratepages
%{_bindir}/numactl
%{_bindir}/numademo
%{_bindir}/numastat
%{_mandir}/man8/*.8*
%doc README.md
%exclude %{_mandir}/man2/*.2*

%files libs
%{_libdir}/libnuma.so.1
%{_libdir}/libnuma.so.1.0.0
%exclude %{_libdir}/libnuma.a
%exclude %{_libdir}/libnuma.la

%files devel
%{_libdir}/libnuma.so
%{_libdir}/pkgconfig/numa.pc
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_mandir}/man3/*.3*

%changelog
* Thu Mar 21 2019 lihongjiang<lihongjiang6@huawei.com> - 2.0.12-2
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:backport patches

* Mon Sep 10 2018 openEuler Buildteam <buildteam@openeuler.org> - 2.0.12-1
- Package init