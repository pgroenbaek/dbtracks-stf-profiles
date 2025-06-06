
# DBTracks STF Profiles

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/pgroenbaek/dbtracks-stf-profiles?style=flat&label=Latest%20Version)](https://github.com/pgroenbaek/dbtracks-stf-profiles/releases)
[![Open Rails T1.5.1-1390+](https://img.shields.io/badge/Open%20Rails-T1.5.1--1390+-green?style=flat&labelOpen%20Rails&color=%237dc243)](https://openrails.org/)
[![Open Rails NYMG rev. 160.2+](https://img.shields.io/badge/Open%20Rails%20NYMG-rev.%20160.2+-orange?style=flat&labelOpen%20Rails&color=%237dc243)](https://www.interazioni-educative.it/Downloads/index.php)
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

These track profiles allow use of the super-elevation feature in Open Rails together with Norbert Rieger's DBTracks. They mimic the original DBTracks shapes as best as possible.

If you wish to replace dynamic tracks within a route and/or generate new track shapes, you should instead use the DPP profiles provided by Norbert with Dynatrax.


## Installation
This repository only contains the track profiles. The textures can be obtained from the [DBTracks packages](https://dbtracks.com/pages/DownloadDBTracks.html). You most likely have the textures already if you need these profiles for super-elevation.

**NOTE:** Use of multiple profiles is only supported from testing version _T1.5.1-1390_ or _NYMG rev. 160.2_ onwards.


### Steps to install:
1. Download and extract the [latest release](https://github.com/pgroenbaek/dbtracks-stf-profiles/releases).

2. Copy all the track profiles from the `TrackProfiles` folder.

3. Place all of them into the `<route folder>/TrackProfiles` folder.

Open Rails will now automatically generate super-elevated track based on the type of DBTracks sections used in the route.


## Usage
The profiles are already configured to match DBTracks variant based on the `DB` and `V4hs` prefixes of the shape file names.

If you have track shapes named anything else, additional match conditions can be added using the `IncludedShapes` parameter within each track profile file. You can also use the `ExcludedShapes` parameter if necessary.


### About Dynatrax generated track sections:
You can make all Dynatrax track shapes use a profile by default by adding `Dynatrax-*` to the `IncludedShapes` parameter within one of the profiles. For example `IncludedShapes ( "DB2f_*, Dynatrax-*" )`.

If there are Dynatrax track shapes that you want to use other track variants for, you can then rename the shape file names to include the DBTracks prefix. For example from `Dynatrax-40892.s` to `DB2z_Dynatrax-40892.s`.

As with previous versions of Open Rails you can also copy/paste a profile and rename it `TrProfile.stf` to use it for regular dyntrack.


### Further documentation:
More details on how to use these track profiles is available in the [Open Rails documentation](https://open-rails.readthedocs.io/en/latest/options.html#superelevation). 

More information about the technical aspects of STF track profiles in Open Rails is available in [this document](https://static.openrails.org/files/OpenRails-Testing-How%20to%20Provide%20Track%20Profiles%20for%20Open%20Rails%20Dynamic%20Track.pdf).


## Track Variants

| DBTracks package  | Variants to do                                   | Variants done |
|-------------------|--------------------------------------------------|---------------|
| DB1               |                      | DB1, DB1b, DB1f, DB1fb, DB1fw, DB1s, DB1sh, DB1sh_lft, DB1w, DB1z, DB1zw        |
| DB10              |                                     | DB10, DB10f, DB10fb, DB10fw, DB10w          |
| DB11              |                                     | DB11, DB11f, DB11fb          |
| DB2               |                        | DB2, DB2b, DB2br, DB2f, DB2fb, DB2fbr, DB2fw, DB2s, DB2sh, DB2sh_lft, DB2w, DB2z, DB2zw   |
| DB20              |                            | DB20, DB20b, DB20f, DB20fb, DB20fw, DB20w, DB20z         |
| DB21              |                              | DB21, DB21b, DB21f, DB21fb           |
| DB22              |                              | DB22, DB22b, DB22f, DB22fb, DB22fw, DB22w          |
| DB23              |                      | DB23, DB23b, DB23f, DB23fb, DB23sh, DB23sh_lft          |
| DB3               |                   | DB3, DB3b, DB3br, DB3f, DB3fb, DB3fbr, DB3sh, DB3sh_lft           |
| DB30              |                              | DB30, DB30b, DB30f, DB30fb          |
| DB4               |                                 | DB4, DB4b, DB4f, DB4fb           |
| DB40              |                              | DB40, DB40b, DB40f, DB40fb          |
| DB5               |                                 | DB5, DB5b, DB5f, DB5fb           |
| DB50              |                              | DB50, DB50b, DB50f, DB50fb          |
| DB51              |                              | DB51, DB51b, DB51f, DB51fb          |
| DB52              |                              | DB52, DB52b, DB52f, DB52fb          |
| DB501             |                           | DB501, DB501b, DB501f, DB501fb         |
| DB502             |                           | DB502, DB502b, DB502f, DB502fb         |
| DR2               |                                 | DR2, DR2b, DR2br, DR2f, DR2fb           |
| DR20              |                                             | DR20, DR20b, DR20br, DR20f, DR20fb          |
| DR3               |             | DR3, DR3b, DR3h, DR3he, DR3he2, DR3he3, DR3he4, DR3he5, DR3he6          |
| DR30              |             | DR30, DR30b, DR30h, DR30he, DR30he2, DR30he3, DR30he4, DR30he5, DR30he6         |
| DR4               |                                 | DR4br           |
| V4hs              |                      | V4hs_DB1, V4hs_NP1, V4hs_NP2, V4hs_R2k, V4hs_RKL              |

If anything is missing, feel free to suggest more by creating an issue.


## Known issues

- There is no good way to place objects at an interval along the generated track with STF profiles. For example the following is missing from super-elevated track:
	- Connectors between the two overhead wires in f-variants.
	- Supports for the 3rd rail in sh-variants.
- Textures are not yet properly mapped to the 3rd rail in sh variants, this will be fixed eventually. If you want to have a go at doing the texture mapping properly, feel free to do so and submit a pull request with it.

Feel free to create an issue if you find more.


## License

These track profiles were configured by Peter Grønbæk Andersen based on Norbert Rieger's original work on DBTracks.

The profiles are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

## Acknowledgements

In memory of Norbert Rieger.

All credit goes to Norbert as he is the author of the original DBTracks shapes.



## Screenshots

![./Screenshots/DB1s_1.png](./Screenshots/DB1s_1.png)
![./Screenshots/DB1s_2.png](./Screenshots/DB1s_2.png)
![./Screenshots/V4hs_R2k_1.png](./Screenshots/V4hs_R2k_1.png)
![./Screenshots/V4hs_R2k_2.png](./Screenshots/V4hs_R2k_2.png)



[cc-by-nc-sa]: https://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat&logo=creative-commons&logoColor=white