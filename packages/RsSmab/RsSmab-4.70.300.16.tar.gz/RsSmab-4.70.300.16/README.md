Rohde & Schwarz SMA100B Microwave Signal Generator RsSmab instrument driver.

Supported instruments: SMA100B

The package is hosted here: https://pypi.org/project/RsSmab/

Documentation: https://RsSmab.readthedocs.io/

Examples: https://github.com/Rohde-Schwarz/Examples/tree/main/SignalGenerators/Python/RsSmab_ScpiPackage

----------------------------------------------------------------------------------

Release Notes:

Latest release notes summary: Fixed several misspelled arguments and command headers

Version 4.70.300.16

- Fixed several misspelled arguments and command headers

Version 4.70.300.15

- Complete rework of the Repeated capabilities. Before, the driver used extensively the RepCaps Channel, Stream, Subframe, User, Group. Now, they have more fitting names, and also proper ranges and default values.
All the repcaps ending with Null have ranges starting with 0. 0 is also their default value.
For example, ChannelNull starts from 0, while Channel starts from 1. Since this is a breaking change, please make sure your code written in the previous version of the driver is compatible with this new version.
This change was necessary in order to assure all the possible settings.

Version 4.70.205.9

- Added Documentation
- Added method RsSmab.list_resources()

Version 4.70.205.8

- Default HwInterface repcap is 0 (empty command suffix)

Version 4.70.205.7

- Second build, fixed enum names

Version 4.70.205.1

- First released version