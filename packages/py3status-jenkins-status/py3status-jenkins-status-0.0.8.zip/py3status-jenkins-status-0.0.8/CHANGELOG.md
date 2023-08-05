# CHANGELOG

This project uses [semantic versioning](https://semver.org/).

## [0.0.8] - 2021-05-15
### Added

* tests for jenkins_status
* tests for error_response
* format_job parameter

### Changed

* setup use config file

## [0.0.7] - 2021-05-08
### Added

* tests for jenkins
* tests for jenkins job color
* test coverage

## [0.0.6] - 2021-05-08
### Added

* tox configuration
* pre-commit configuration
* tests for credentials and py3status version
* gitlab ci configuration

### Fixed

* Findings of flake8 and pre-commit hooks
* import py3status_jenkins_module in docs/conf.py
* jenkins pakage in setup and gitlab-ci

## [0.0.5] - 2021-05-03
### Fixed

* Remove debug print

## [0.0.4] - 2021-05-01
### Changed

* Refactoring of output and using "format" string

## [0.0.3] - 2021-04-29
### Added

* configuration file for readthedocs
* python requirements for docs
* version python module

## [0.0.2] - 2021-04-29
### Added

* initial documentation (intro and configuration)

## [0.0.1-dev5] - 2021-04-28
### Added

* PyPi documentation url

## [0.0.1-dev4] - 2021-04-28
### Added

* changelog entries
* Initial documentation (sphinx)
* readme file for documentation
* username/password credentials handling

### Fixing

* remove debug pring
* failure status name in description
* version (adjust to semantic versioning)

## [0.1.dev3] - 2021-04-27
### Fixed

* Module name and path

## [0.1.dev2] - 2021-04-26
### Added

* Missing author and athor_email in setup.py
* Main chapter to readme
* MIT license file
* Manifest file

## [0.1] - 2021-04-25
### Added

* Initial implementation of jenkins job status viewer

---

# About this Changelog

https://keepachangelog.com suggests:

Guiding Principles

* Changelogs are for humans, not machines.
* There should be an entry for every single version.
* The same types of changes should be grouped.
* Versions and sections should be linkable.
* The latest version comes first.
* The release date of each version is displayed.
* Mention whether you follow Semantic Versioning.

Types of changes

* **Added for new features.**
* **Changed for changes in existing functionality.**
* **Deprecated for soon-to-be removed features.**
* **Removed for now removed features.**
* **Fixed for any bug fixes.**
* **Security in case of vulnerabilities.**
