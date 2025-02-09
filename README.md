# tbtools-rpm
RPM Package for Intel's tbtools

## Instructions
Install the `tbtools` package to use tbtools. Report issues at the contact link.

Upstream is located on Intel's GitHub: [intel/tbtools](https://github.com/intel/tbtools)

## Dependency tree
Shows only those dependencies not currently packaged in Fedora.

- tbtools
  - rust-cursive (version 0.21 - Fedora packages 0.20)
    - rust-cursive\_core (version 0.4 - Fedora packages 0.3)
      - rust-cursive-macros (would need a new package for Fedora)
  - rust-include\_dir (would need a new package for Fedora)
    - rust-include\_dir\_macros (would need a new package for Fedora)

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
