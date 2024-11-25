
# DBTracks STF Profiles

This is an attempt to mimic DBTracks as best as possible using the STF track profile format.

These track profiles enable use of the super-elevation feature in Open Rails together with Norbert Rieger's DBTracks.

If you wish to replace dynamic tracks within a route and/or generate new track shapes, you should instead use the DPP profiles provided by Norbert with Dynatrax.


## Installation
This repository only contains the STF track profiles. The textures can be obtained from the [DBTracks package](https://the-train.de/downloads/entry/11252-dbtracks/).

You more than likely have the textures in the route already if you ever need these profiles for super-elevation.


### Open Rails _1.5.1_ (stable version):
Pick whichever of the .stf files from [./TrackProfiles](./TrackProfiles) you want into the `<route folder>/TrackProfiles` folder.

Rename the profile to `TrProfile.stf`.

If you have super-elevation enabled in the settings Open Rails will now generate super-elevated track in curves based on this profile.

Open Rails 1.5.1 stable version only supports using one track profile for super-elevation.

Using multiple profiles is supported from testing version _T1.5.1-1390_ onwards (see below).


### Open Rails _T1.5.1-1390_ onwards (testing version):
Copy all the .stf files from [./TrackProfiles](./TrackProfiles) into the `<route folder>/TrackProfiles` folder.

Open Rails will now select track profile automatically based on the DBTracks types used in the route.

TODO about Dynatrax generated dyntrack replacements


## Usage
A more detailed guide on how to use these track profiles is available in the [Open Rails documentation](https://open-rails.readthedocs.io/en/latest/options.html#superelevation). 

More information about the technical aspects of STF track profiles in Open Rails is available in [this document](https://static.openrails.org/files/OpenRails-Testing-How%20to%20Provide%20Track%20Profiles%20for%20Open%20Rails%20Dynamic%20Track.pdf).


## Roadmap

The plan is to add STF profiles for all DBTracks variants.

| DBTracks package  | Variants to do                                   | Variants done |
|-------------------|--------------------------------------------------|---------------|
| DB1               | DB1fb, DB1sh                     | DB1, DB1b, DB1f, DB1s, DB1z        |
| DB10              | DB10fb                                    | DB10, DB10f          |
| DB11              | DB11fb                                    | DB11, DB11f          |
| DB2               | DB2br, DB2fb, DB2sh                        | DB2, DB2b, DB2f, DB2s, DB2z   |
| DB20              | DB20fb                           | DB20, DB20b, DB20f, DB20z         |
| DB21              | DB21fb                             | DB21, DB21b, DB21f           |
| DB22              | DB22fb                             | DB22, DB22b, DB22f          |
| DB23              | DB23fb, DB23sh                     | DB23, DB23b, DB23f          |
| DB3               | DB3br, DB3fb, DB3sh                  | DB3, DB3b, DB3f           |
| DB30              | DB30fb                             | DB30, DB30b, DB30f          |
| DB4               | DB4fb                                | DB4, DB4b, DB4f           |
| DB40              | DB40fb                             | DB40, DB40b, DB40f          |
| DB5               | DB5fb                                | DB5, DB5b, DB5f           |
| DB50              | DB50fb                             | DB50, DB50b, DB50f          |
| DB51              | DB51fb                             | DB51, DB51b, DB51f          |
| DB52              | DB52fb                             | DB52, DB52b, DB52f          |
| DB501             | DB501fb                          | DB501, DB501b, DB501f         |
| DB502             | DB502fb                          | DB502, DB502b, DB502f         |
| DR2               | DR2fb                                | DR2, DR2b, DR2f           |
| DR20              |                                             | DR20, DR20b, DR20f          |
| V4hs              | V4hs_DB1, V4hs_R2k, V4hs_RKL                     |               |

Feel free to suggest more by creating an issue, or by submitting a pull request with more profiles.


## Known issues

- Have yet to find a good way to place objects at an interval along the generated track. For example:
	- Connectors between the two overhead wires in f-variants are missing.
	- Supports for the 3rd rail in sh-variants are missing.


## License

These STF track profiles were created by Peter Grønbæk Andersen based on Norbert Rieger's work on DBTracks.

The profiles are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).


## Acknowledgements

In memory of Norbert Rieger.

All credit goes to Norbert as he is the author of the original DBTracks shapes.