Name:		tbtools
Summary:	Thunderbolt/USB4 debugging tools
Version:	0.5.0
Release:	2%{?dist}
# TODO: Check license of files and deps
# TODO: Rust RPM Macros provide license generation etc...
License:	MIT
URL:		https://github.com/intel/tbtools

Source:		%{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:	make

%description
This is a collection of tools for Linux Thunderbolt/USB4 development, debugging
and validation but may be useful to others as well.

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

%install
# As this package is NOT published to crates.io, we MUST NOT install crate sources for it in the local registry
# Per: https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/#_rust_applications_non_crates_io_crates
%define cargo_install_lib 0
# Since we skip cargo install in the Makefile, use our macro instead
%cargo_install
PREFIX=%{buildroot}/%{_prefix} make install

%files
%license LICENSE
%doc README.md
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
