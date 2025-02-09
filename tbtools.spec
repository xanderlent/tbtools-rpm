Name:		tbtools
Summary:	Thunderbolt/USB4 debugging tools
Version:	0.5.0
Release:	%autorelease
# TODO: Check license of files and deps
License:	MIT
URL:		https://github.com/intel/tbtools

Source:		%{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24

%description
This is a collection of tools for Linux Thunderbolt/USB4 development, debugging
and validation but may be useful to others as well.

%prep
%autosetup -p1 -n tbtools-%{version}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
PREFIX=%{_prefix} make install


%autochangelog
