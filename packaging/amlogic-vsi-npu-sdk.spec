Name:      amlogic-vsi-npu-sdk
Summary:   Amlogic Verisilicon NPU SDK Library
Version:   6.4.0.3
Release:   1
Group:     System/Libraries
License:   Apache-2.0
Source0:   http://developer.samsung.com/%{name}-%{version}.tar.gz
Source1:   %{name}.manifest
ExclusiveArch: %{arm} aarch64

BuildRequires: cmake
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%define _pcdir  %{_libdir}/pkgconfig

%description
AmlogicNPU SDK Library for NN Applications.

%package devel
Summary:   Amlogic NPU SDK Library (development)
Group:    System/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header and Configuration for Amlogic NPU SDK Library.

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
	-DPCDIR=%{_pcdir}

make %{?jobs:-j%jobs}

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%manifest %{name}.manifest
%attr(755, root, root)
%{_libdir}/*.so*

%files devel
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/*.pc

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
