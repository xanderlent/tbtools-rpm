# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate cursive-macros

Name:           rust-cursive-macros
Version:        0.1.0
Release:        2%{?dist}
Summary:        Proc-macros for the cursive TUI library

License:        MIT
URL:            https://crates.io/crates/cursive-macros
Source:         %{crates_source}
# * Missing LICENSE file is fixed upstream
# * https://github.com/gyscos/cursive/pull/814
Source2:        https://github.com/gyscos/cursive/raw/main/LICENSE
# Manually created patch for downstream crate metadata changes
# * LICENSE not in sources fixed upstream
# * https://github.com/gyscos/cursive/pull/818
Patch:          cursive-macros-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Proc-macros for the cursive TUI library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/Readme.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+builder-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+builder-devel %{_description}

This package contains library source intended for building other packages which
use the "builder" feature of the "%{crate}" crate.

%files       -n %{name}+builder-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+find-crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+find-crate-devel %{_description}

This package contains library source intended for building other packages which
use the "find-crate" feature of the "%{crate}" crate.

%files       -n %{name}+find-crate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+quote-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quote-devel %{_description}

This package contains library source intended for building other packages which
use the "quote" feature of the "%{crate}" crate.

%files       -n %{name}+quote-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+syn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+syn-devel %{_description}

This package contains library source intended for building other packages which
use the "syn" feature of the "%{crate}" crate.

%files       -n %{name}+syn-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
cp -pav %{SOURCE2} .

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
* Tue Apr 15 2025 Alexander F. Lent <lx@xanderlent.com> - 0.1.0-2
- Initial package
