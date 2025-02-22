# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate cursive

Name:           rust-cursive0.21
Version:        0.21.1
Release:        1%{?dist}
Summary:        TUI (Text User Interface) library focused on ease-of-use

License:        MIT
URL:            https://crates.io/crates/cursive
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A TUI (Text User Interface) library focused on ease-of-use.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crossterm-backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crossterm-backend-devel %{_description}

This package contains library source intended for building other packages which
use the "crossterm-backend" feature of the "%{crate}" crate.

%files       -n %{name}+crossterm-backend-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
