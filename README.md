
# DBTracks STF Profiles

This is an attempt to mimic DBTracks as best as possible using the Open Rails STF track profile format.

These track profiles enable use of the superelevation feature in Open Rails together with Norbert Rieger's DBTracks.

If you want to generate track pieces to place in a route you are better off using the DPP profiles provided by Norbert with Dynatrax.

## Installation

TODO how and where to add them

This repository only contains the STF track profiles. The textures needed can be obtained from the [DBTracks package](https://the-train.de/downloads/entry/11252-dbtracks/). You probably have the textures already if you ever need these profiles for superelevation.

## Usage

A guide on how to use these track profiles is available in the [Open Rails documentation](https://open-rails.readthedocs.io/en/latest/options.html#superelevation). 

More information about the technical aspects of STF track profiles in Open Rails is available in [this document](https://static.openrails.org/files/OpenRails-Testing-How%20to%20Provide%20Track%20Profiles%20for%20Open%20Rails%20Dynamic%20Track.pdf).


## Roadmap

The plan is to add STF profiles for all DBTracks variants.

| DBTracks package  | Variants to do                                   | Variants done |
|-------------------|--------------------------------------------------|---------------|
| DB1               | DB1b, DB1f, DB1fb, DB1s, DB1sh, DB1z             | DB1           |
| DB10              | DB10f, DB10fb, DB11, DB11f, DB11fb               | DB10          |
| DB11              | DB11, DB11f, DB11fb                              |               |
| DB2               | DB2b, DB2br, DB2f, DB2fb, DB2s, DB2sh, DB2z      | DB2           |
| DB20              | DB20b, DB20f, DB20fb, DB20z                      | DB20          |
| DB21              | DB21, DB21b, DB21f, DB21fb                       |               |
| DB22              | DB22b, DB22f, DB22fb                             | DB22          |
| DB23              | DB23, DB23b, DB23f, DB23fb, DB23sh               |               |
| DB3               | DB3, DB3b, DB3br, DB3f, DB3fb, DB3sh             |               |
| DB30              | DB30, DB30b, DB30f, DB30fb                       |               |
| DB4               | DB4, DB4b, DB4f, DB4fb                           |               |
| DB40              | DB40, DB40b, DB40f, DB40fb                       |               |
| DB5               | DB5, DB5b, DB5f, DB5fb                           |               |
| DB50              | DB50, DB50b, DB50f, DB50fb                       |               |
| DB51              | DB51, DB51b, DB51f, DB51fb                       |               |
| DB52              | DB52, DB52b, DB52f, DB52fb                       |               |
| DB501             | DB501, DB501b, DB501f, DB501fb                   |               |
| DB502             | DB502, DB502b, DB502f, DB502fb                   |               |
| DR2               | DR2, DR2b, DR2f, DR2fb                           |               |
| DR20              | DR20, DR20f                                      |               |
| V4hs              | V4hs_DB1, V4hs_R2k, V4hs_RKL                     |               |

Feel free to suggest more by creating an issue or submitting a pull request if you want more added.

## Known issues

- Have yet to find a good way to place objects at an interval along the generated track. For example connectors between the two overhead wires for f-variants and supports for the 3rd rail in sh-variants.
- When superelevation is enabled Open Rails will generally remove the existing curved track sections. But this does not happen for Dynatrax pieces that have both curved and straight sections. If such Dynatrax pieces exist in a route you will find that the superelevated sections overlap with those Dynatrax pieces (at least in Open Rails 1.5.1).


## License:

These STF track profiles are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Acknowledgements

All credit goes to Norbert Rieger who is the author of the original DBTracks shapes.