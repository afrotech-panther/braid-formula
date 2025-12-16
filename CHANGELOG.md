# Changelog

All notable changes to the Braid Formula will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-12-15

### Added
- Initial release of the Braid Formula
- Core `settle()` function for calculating collaborative settlements
- `quick_settle()` helper for simplified usage
- Full input validation with descriptive error messages
- Command-line interface with interactive mode
- Support for:
  - Profitable and loss scenarios
  - Negative payouts (when someone owes money)
  - Unequal splits and expenses
  - Multiple collaborators
  - Fractional percentages
- Comprehensive test suite (31 tests)
- MIT license for open-source use

### Technical
- Pure Python with no external dependencies
- Uses `Decimal` for precise financial calculations
- Automatic rounding adjustment to ensure payouts sum to revenue
- JSON-serializable output via `.to_dict()` method
- Human-readable summaries via `.summary()` method
