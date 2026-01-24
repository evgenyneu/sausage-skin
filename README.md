# sausage skin music

A web site for sausage skin music:

* [music](music) folder - source files (wav, cover images, videos, etc.)
* [web](web) folder - generated static web site files.

## [music](music) folder structure

Files are stored in year/month/day folders. Each 'day' folder contains original file for a single track. For example, `music/a2024/a11_nov/a05_cloven_hoofed` contains original files for Cloven Hoofed track.

Each day folder contains following files:

* `wav` - original wav files. The `*_mix.wav` is final mastered version, and it also has ISRC code embedded.
* `mp4` - video file for the track, created for the youtube upload.
* `png` - original unedited image used for the cover.
* `pxd` - Pixelmator file for the cover image.
* `jpg` - cover image containing both the image/photo and the overlaid text with artist/title, the `*_cover.jpg` file is the final version.
* `track.yml` - metadata for the track (title, description, links, ISRC code, etc.) that is used for the web site.
* `README.md` - notes about the track.
* Ablton Live project files are stored in a subfolder, which were used to make the mastered `*_mix.wav` file.

## Setup

Install [uv](https://docs.astral.sh/uv/) and install Python dependencies:

```sh
uv sync
```


## Generate web site

Generate the static web site files in the [web](web) folder from the source files in the [music](music) folder.

```sh
uv run python src/generate/main.py
```


## License

All music and code in this repository is in [CC0 Public Domain Dedication](LICENSE).
