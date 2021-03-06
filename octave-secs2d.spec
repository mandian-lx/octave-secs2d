%define octpkg secs2d

# fix debuginfo-without-sources
%define debug_package %{nil}

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	A Drift-Diffusion simulator for 2d semiconductor devices with Octave
Name:		octave-%{octpkg}
Version:	0.0.8
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/support/download.php?file_id=33676
Patch0:		%{name}-0.0.8-port-to-octave-4.2.1.patch
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 2.9.17

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A Drift-Diffusion simulator for 2d semiconductor devices with Octave.

This package is part of external Octave-Forge collection.

%prep
%setup -q -c %{octpkg}-%{version}
cp %SOURCE0 .

# Apply patch
pushd %{octpkg}-%{version}
%patch0 -p0
popd

%build
%octave_pkg_build #-T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
#%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

