# Should cargo tests be enabled?
%bcond check 1

Name:		tbtools
Summary:	Thunderbolt/USB4 debugging tools
Version:	0.5.0
Release:	3%{?dist}
# TODO: Need to poke upstream to set this in Cargo.toml
# TODO: Need to manually check all upstream files for potential license issues!
SourceLicense:	MIT
# TODO: This will NOT be correct until all dependencies have correct license metadata!
# License summary of integrated packages:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:	MIT AND Apache-2.0 AND Unicode-DFS-2016
URL:		https://github.com/intel/tbtools

Source:		%{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:	make

%description
This is a collection of tools for Linux Thunderbolt/USB4 development, debugging
and validation but may be useful to others as well.

# As this package is NOT published to crates.io, we MUST NOT install crate sources for it in the local registry
# Per: https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/#_rust_applications_non_crates_io_crates
%define cargo_install_lib 0

%prep
%autosetup -p1 -n tbtools-%{version}
# Modify the Makefile to skip cargo install, since we have a macro for that
sed -e 's/$(CARGO) install $(IFLAGS) --path . --root $(PREFIX)/# skipping built-in cargo install/' -i Makefile
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
PREFIX=%{buildroot}/%{_prefix} make install

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
%{_datadir}/tbtools

%changelog
%autochangelog
