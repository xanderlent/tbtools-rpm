# tbtools-rpm
RPM Package for Intel's tbtools

## Instructions
Install the `tbtools` package to use tbtools. Report issues at the contact link.

Upstream is located on Intel's GitHub: [intel/tbtools](https://github.com/intel/tbtools)

## Dependency tree
Shows only those dependencies not currently packaged in Fedora.

- tbtools
  - rust-cursive ([RHBZ#2302543](https://bugzilla.redhat.com/show_bug.cgi?id=2302543))
    - rust-cursive\_core ([RHBZ#2302544](https://bugzilla.redhat.com/show_bug.cgi?id=2302544))
      - rust-cursive-macros ([RHBZ#2353989](https://bugzilla.redhat.com/show_bug.cgi?id=2353989))
  - rust-include\_dir ([RHBZ#2360035](https://bugzilla.redhat.com/show_bug.cgi?id=2360035))
    - rust-include\_dir\_macros ([RHBZ#2360034](https://bugzilla.redhat.com/show_bug.cgi?id=2360034))

## Commands to regenerate packages

`rust2rpm --no-rpmautospec -C rust2rpm-include_dir_macros.toml include_dir_macros`  
`rust2rpm --no-rpmautospec -C rust2rpm-include_dir.toml include_dir`  
`rust2rpm --no-rpmautospec -C rust2rpm-cursive_macros.toml -r cursive-macros`  
`rust2rpm --no-rpmautospec -C rust2rpm-cursive_core.toml --compat cursive_core`  
``  

## Build Status
### tbtools
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/tbtools/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/tbtools/)
### rust-cursive0.21
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive0.21/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive0.21/)
### rust-cursive\_core0.4
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive_core0.4/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive_core0.4/)
### rust-cursive-macros
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive-macros/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-cursive-macros/)
### rust-include\_dir
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-include_dir/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-include_dir/)
### rust-include\_dir\_macros
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-include_dir_macros/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/tbtools/package/rust-include_dir_macros/)
