# tap-canny

`tap-canny` is a Singer tap for Canny.

Build with the [Singer SDK](https://gitlab.com/meltano/singer-sdk).

## Installation

```bash
pipx install tap-canny
```

## Configuration

The following configuration options are available:

- `api_key` (required): User-generated Canny API Key
- `limit` (optional): Max amount of records to grab
- `start_date` (optional): should be used on first sync to indicate how far back to grab records. Start dates should conform to the RFC3339 specification.

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-canny --about
```

## Usage

You can easily run `tap-canny` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-canny --version
tap-canny --help
tap-canny --config CONFIG --discover > ./catalog.json
```
### Create and Run Tests

Create tests within the `tap-canny/tests` subfolder and
  then run:

```bash
pip install pytest
pytest tap_canny/tests
```
### Singer SDK Dev Guide

See the [dev guide](../../docs/dev_guide.md) for more instructions on how to use the Singer SDK to 
develop your own taps and targets.