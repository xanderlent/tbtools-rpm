# tbtools-rpm
RPM Package for Intel's tbtools

## Instructions
Install the `tbtools` package to use tbtools. Report issues at the contact link.

Upstream is located on Intel's GitHub: [intel/tbtools](https://github.com/intel/tbtools)

## Dependency tree
Shows only those dependencies not currently packaged in Fedora.

- tbtools ([RHBZ#2363587](https://bugzilla.redhat.com/show_bug.cgi?id=2363587))
  - rust-cursive (upstream in F41+, COPR build for F40)
    - rust-cursive\_core (upstream in F41+, COPR build for F40)
  - rust-include\_dir ([RHBZ#2360035](https://bugzilla.redhat.com/show_bug.cgi?id=2360035))
    - rust-include\_dir\_macros ([RHBZ#2360034](https://bugzilla.redhat.com/show_bug.cgi?id=2360034))

## Commands to regenerate packages

`rust2rpm --no-rpmautospec -C rust2rpm-include_dir_macros.toml include_dir_macros`  
`rust2rpm --no-rpmautospec -C rust2rpm-include_dir.toml include_dir`  

## Build Status
### tbtools
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/tbtools/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/tbtools/)
### rust-cursive (for Fedora 40)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive/)
### rust-cursive\_core (for Fedora 40)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive_core/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive_core/)
### rust-include\_dir
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-include_dir/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-include_dir/)
### rust-include\_dir\_macros
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-include_dir_macros/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-include_dir_macros/)
