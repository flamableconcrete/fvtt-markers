<p float="left">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/upper_m.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/lower_a.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/lower_r.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/lower_k.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/lower_e.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/lower_r.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/lower_s.png" width="48" height="48">
</p>

A simple module that contains 164 markers (1-100, A-Z, a-z, and some symbols) in 4 compendia for a DM to use to mark their maps.

## Installation

Install Markers either directly from your Foundry instance from the Setup's Add-ons page or use this `module.json` link: <https://raw.githubusercontent.com/flamableconcrete/fvtt-markers/main/src/module.json>

## Usage

This add-on consists solely of 4 compendia. No more, no less. They are the following:

* Markers (Numbers): 100 tokens

<p float="left">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/numbers/001.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/numbers/002.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/numbers/003.png" width="48" height="48">
</p>

* Markers (Alphabet lowercase): 26 tokens

<p float="left">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/lower_a.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/lower_b.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/lower_c.png" width="48" height="48">
</p>

* Markers (Alphabet uppercase): 26 tokens

<p float="left">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/upper_a.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/upper_b.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/letters/upper_c.png" width="48" height="48">
</p>

* Markers (Symbols): 12 tokens

<p float="left">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/symbols/symbol_asterisk.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/symbols/symbol_exclamation.png" width="48" height="48">
  <img src="https://github.com/flamableconcrete/fvtt-markers/raw/main/src/assets/images/symbols/symbol_plus.png" width="48" height="48">
</p>

Use these compendia just as you would any other! The tokens themselves are categorized as Actor types. I have found them useful to throw on scenes to cross reference with journal notes.

## Acknowledgements

Big thanks to Paul Umber's article on [Building Compendia for Foundry VTT](https://pumbers.github.io/game-manglement/articles/vtt_compendia_building/) so I didn't have to do most of my editing through Foundry itself.

I created all the images using Gimp and the freely available [Dalelands Uncial font](https://fonts2u.com/dalelands-uncial.font).

## Developer Notes

Mostly a note for future me here, but this repository is interesting for a Foundry VTT add-on because the final zip file that gets used and full structure doesn't show up here directly. It gets generated via GitHub Actions using a combination of `npm install`, `npx gulp build`, and `npx gulp dist`. Then it gets posted as a GitHub Release on the [Releases page](https://github.com/flamableconcrete/fvtt-markers/releases).
