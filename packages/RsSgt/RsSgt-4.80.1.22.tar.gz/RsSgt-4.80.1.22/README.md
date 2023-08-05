Rohde & Schwarz SGT100A SIGMA Vector Signal Generator RsSgt instrument driver.

Supported instruments: SGT100A

The package is hosted here: https://pypi.org/project/RsSgt/

Documentation: https://RsSgt.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/tree/main/SignalGenerators/Python/RsSgt_ScpiPackage

----------------------------------------------------------------------------------

Release Notes:

Latest release notes summary: Fixed several misspelled arguments and command headers

Version 4.80.1.22

- Fixed several misspelled arguments and command headers

Version 4.80.1.19

- Complete rework of the Repeated capabilities. Before, the driver used extensively the RepCaps Channel, Stream, Subframe, User, Group. Now, they have more fitting names, and also proper ranges and default values.
All the repcaps ending with Null have ranges starting with 0. 0 is also their default value.
For example, ChannelNull starts from 0, while Channel starts from 1. Since this is a breaking change, please make sure your code written in the previous version of the driver is compatible with this new version.
This change was necessary in order to assure all the possible settings.

Version 4.80.0.16

- Added arb_files interface
- Default HwInterface repcap is 0 (empty command suffix)

Version 4.80.0.5

- First released version