# Should tests be enabled?
%bcond check 1

# As this package is NOT published to crates.io, we MUST NOT install crate sources for it in the local registry
# Per: https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/#_rust_applications_non_crates_io_crates
%define cargo_install_lib 0

Name:		tbtools
Summary:	Thunderbolt/USB4 debugging tools
Version:	0.6.0
Release:	1%{?dist}
# Most source files lack an explicit license
# The main LICENSE file is MIT
# scripts/verify-sysfs.sh: GPL-2.0-only, but not packaged at all
# TODO: Need to poke upstream to set this in Cargo.toml, ask about license
SourceLicense:	MIT
# License summary of integrated packages:
# 
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:	((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT or Apache-2.0) AND (Unlicense OR MIT)
URL:		https://github.com/intel/%{name}

Source:		%{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:	make

%description
This is a collection of tools for Linux Thunderbolt/USB4 development, debugging
and validation but may be useful to others as well.

%prep
%autosetup -p1 -n %{name}-%{version}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# Skip using the Makefile to call cargo build, since we have a macro for that
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
# Since we skip cargo install in the Makefile, use our macro instead
%cargo_install
# Setting CARGO=/usr/bin/true skips the cargo install in the Makefile without modifying it
PREFIX=%{buildroot}/%{_prefix} make install CARGO=/usr/bin/true

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc src/bin/tbman/tbman.png
%doc SECURITY.md
%doc TODO
%{_bindir}/lstb
%{_bindir}/tbadapters
%{_bindir}/tbauth
%{_bindir}/tbdump
%{_bindir}/tbget
%{_bindir}/tblist
%{_bindir}/tbman
%{_bindir}/tbmargin
%{_bindir}/tbpd
%{_bindir}/tbset
%{_bindir}/tbtrace
%{bash_completions_dir}/tbtools-completion.bash
%{bash_completions_dir}/tbadapters
%{bash_completions_dir}/tbauth
%{bash_completions_dir}/tbdump
%{bash_completions_dir}/tbget
%{bash_completions_dir}/tblist
%{bash_completions_dir}/tbmargin
%{bash_completions_dir}/tbset
%{bash_completions_dir}/tbtrace
%{_datadir}/%{name}

%changelog
%autochangelog
