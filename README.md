
# DBTracks STF Profiles
These track profiles mimic DBTracks as best as possible to allow use of the super-elevation feature in Open Rails with Norbert Rieger's DBTracks.

If you wish to replace dynamic tracks within a route and/or generate new track shapes, you should instead use the DPP profiles provided by Norbert with Dynatrax.


## Installation
This repository only contains the track profiles. The textures can be obtained from the [DBTracks package](https://the-train.de/downloads/entry/11252-dbtracks/).

If you ever need these profiles for super-elevation the textures required most likely are in your route already.

**NOTE:** Use of multiple profiles is only supported from testing version _T1.5.1-1390_ onwards.


### Open Rails testing version _T1.5.1-1390_ onwards:
1. Download and extract the [latest release](https://github.com/pgroenbaek/dbtracks-stf-profiles/releases).

2. Copy all the track profiles from either the `TrackProfiles` or `TrackProfiles_h` folder. The latter adds extra trackbed similar to the h variants in USTracks and often looks better when super-elevated. See the [Usage section](#version-with-extra-embankment) for an example.

3. Place all of them into the `<route folder>/TrackProfiles` folder.

Open Rails will now select track profile automatically based on the type of DBTracks sections used in the route.


## Usage
The profiles are already configured to match DBTracks variant based on the `DB*_` prefix in the name of shape files.

If you have track shapes named anything else, additional match conditions can be added using the `IncludeShapes` parameter within each track profile file. You can also add and use the `ExcludedShapes` parameter if necessary.

### Version with extra embankment.

TODO [./TrackProfiles](./TrackProfiles) vs [./TrackProfiles_h](./TrackProfiles_h)

### Fixing Dynatrax generated track sections:
TODO about Dynatrax generated dyntrack replacements
TODO workaround, with link to example script
TODO renaming dynatrax shapes or adding Dynatrax to Included shapes

### Further documentation:
More details on how to use these track profiles is available in the [Open Rails documentation](https://open-rails.readthedocs.io/en/latest/options.html#superelevation). 

More information about the technical aspects of STF track profiles in Open Rails is available in [this document](https://static.openrails.org/files/OpenRails-Testing-How%20to%20Provide%20Track%20Profiles%20for%20Open%20Rails%20Dynamic%20Track.pdf).


## Track Variants

| DBTracks package  | Variants to do                                   | Variants done |
|-------------------|--------------------------------------------------|---------------|
| DB1               | DB1sh, DB1sh_lft                     | DB1, DB1b, DB1f, DB1fb, DB1s, DB1z        |
| DB10              |                                     | DB10, DB10f, DB10fb          |
| DB11              |                                     | DB11, DB11f, DB11fb          |
| DB2               | DB2fbr, DB2br, DB2sh, DB2sh_lft                        | DB2, DB2b, DB2f, DB2fb, DB2s, DB2z   |
| DB20              |                            | DB20, DB20b, DB20f, DB20fb, DB20z         |
| DB21              |                              | DB21, DB21b, DB21f, DB21fb           |
| DB22              |                              | DB22, DB22b, DB22f, DB22fb          |
| DB23              | DB23sh, DB23sh_lft                     | DB23, DB23b, DB23f, DB23fb          |
| DB3               | DB3fbr, DB3br, DB3sh, DB3sh_lft                  | DB3, DB3b, DB3f, DB3fb           |
| DB30              |                              | DB30, DB30b, DB30f, DB30fb          |
| DB4               |                                 | DB4, DB4b, DB4f, DB4fb           |
| DB40              |                              | DB40, DB40b, DB40f, DB40fb          |
| DB5               |                                 | DB5, DB5b, DB5f, DB5fb           |
| DB50              |                              | DB50, DB50b, DB50f, DB50fb          |
| DB51              |                              | DB51, DB51b, DB51f, DB51fb          |
| DB52              |                              | DB52, DB52b, DB52f, DB52fb          |
| DB501             |                           | DB501, DB501b, DB501f, DB501fb         |
| DB502             |                           | DB502, DB502b, DB502f, DB502fb         |
| DR2               |                                 | DR2, DR2b, DR2f, DR2fb           |
| DR20              |                                             | DR20, DR20b, DR20f, DR20fb          |
| V4hs              | V4hs_DB1, V4hs_R2k, V4hs_RKL                     |               |

Feel free to suggest more by creating an issue if anything is missing.


## Known issues

- There is no good way to place objects at an interval along the generated track with STF profiles. For example the following is missing from super-elevated track:
	- Connectors between the two overhead wires in f-variants.
	- Supports for the 3rd rail in sh-variants.
- Dynatrax generated track sections are not super-elevated properly as of testing version T1.5.1-1390. There is a dirty workaround for this that involves modifying the global tsection.dat. This is discussed in the [Usage section](#fixing-dynatrax-generated-track-sections).

Please create an issue or pull request if you find more.

## License

These track profiles were configured by Peter Grønbæk Andersen based on Norbert Rieger's original work on DBTracks.

The profiles are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).


## Acknowledgements

In memory of Norbert Rieger.

All credit goes to Norbert as he is the author of the original DBTracks shapes.