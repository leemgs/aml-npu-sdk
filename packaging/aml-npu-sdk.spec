Name:      aml-npu-sdk
Summary:   Amlogic VeriSilicon NPU SDK Library
Version:   6.4.0.10
Release:   0
Group:     System/Libraries
License:   GPLv2
URL:       https://www.khadas.com/post/npu-toolkit-v6-4-0-10-for-vim3---vim3l-released
Source0:   %{name}-%{version}.tar.gz
Source1:   %{name}.manifest

BuildRequires: cmake

ExclusiveArch: %{arm} aarch64

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
Amlogic VeriSilicon NPU SDK Library to run neural network applications.

%package devel
Summary:   Amlogic VeriSilicon NPU SDK Library (development)
Group:    System/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header and Configuration for Amlogic VeriSilicon NPU SDK Library.

%prep
%setup -q

%build
cp %{SOURCE1} .
cmake \
	-DCMAKE_INSTALL_PREFIX=/usr \
%ifarch aarch64
	-DARCH=arm64 \
%else
	-DARCH=arm \
%endif
	-DBINDIR=%{_bindir} \
	-DLIBDIR=%{_libdir} \
	-DINCDIR=%{_includedir}/%{name} \
	-DPCDIR=%{_libdir}/pkgconfig

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest %{name}.manifest
%license LICENSE
%attr(0755, root, root)
%{_libdir}/*.so*

%files devel
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/*.pc

%changelog

* Fri Aug 14 2020 Geunsik Lim <geunsik.lim@samsung.com>
- Added the spec file to generate a Tizen RPM package

