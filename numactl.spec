Name: numactl
Version: 2.0.14
Release: 1
Summary: Library for tuning for Non Uniform Memory Access machines
License: GPLv2
URL: https://github.com/numactl/numactl
Source0: https://github.com/numactl/numactl/releases/download/v%{version}/numactl-%{version}.tar.gz
BuildRequires: libtool automake autoconf 

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
%autosetup -n %{name}-%{version} -p1

%build
%configure
%disable_rpath
%make_build CFLAGS="$RPM_OPT_FLAGS -I."

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%check
# test-suites need current-build dynamic libray,
# so we export LD_LIBRARY_PATH for find it.
LD_LIBRARY_PATH=$(pwd)/.libs make check

%ldconfig_scriptlets
%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

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
* Tue Nov 30 2021 zhouwenpei<zhouwenpei1@huawei.com> - 2.0.14-1
- upgrade version to 2.0.14

* Thu Aug 26 2021 Chunsheng Luo <luochunsheng@huawei.com> - 2.0.13-6
- DESC: enable make check

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 2.0.13-5
- DESC: delete -Sgit from %autosetup, and delete BuildRequires git

* Fri Jan 10 2020 yuxiangyang<yuxiangyang4@huawei.com> - 2.0.13-4
- upgrade version to 2.0.13

* Fri Dec 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.0.12-3
- Fix ldconfig scriptlets

* Thu Mar 21 2019 lihongjiang<lihongjiang6@huawei.com> - 2.0.12-2
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:backport patches

* Mon Sep 10 2018 openEuler Buildteam <buildteam@openeuler.org> - 2.0.12-1
- Package init
