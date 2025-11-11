# Streamlit SeqViz

**Streamlit SeqViz** 🧬 brings the powerful [SeqViz](https://github.com/Lattice-Automation/seqviz) DNA/RNA/protein viewer to [Streamlit](https://github.com/streamlit/streamlit). It allows you to visualize and explore biological sequences interactively inside your Streamlit apps with support for annotations, primers, restriction sites, translations, and more.

## Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://seqviz.streamlit.app/)

![SeqViz demo](https://github.com/ghilesmeddour/st-seqviz/blob/main/res/streamlit-seqviz-demo.gif)

## Installation

```bash
pip install st-seqviz
```

## Usage

```python
import streamlit as st

from st_seqviz import SeqViz

sv = SeqViz(
    seq="TTGACGGCTAGCTCAGTCCTAGGTACAGTGCTAGC",
    name="J23100",
    annotations=[
        {"name": "promoter", "start": 0, "end": 34, "direction": 1, "color": "blue"}
    ],
)

st.json(sv)
```

➡️ See the `/demo` folder for more complex examples (annotations, enzymes, translations, highlights, etc.).

## API Reference

### Parameters

| Name                     | Type                                              | Default                               | Description                                                 |
| ------------------------ | ------------------------------------------------- | ------------------------------------- | ----------------------------------------------------------- |
| `seq`                    | `str`                                             | —                                     | DNA, RNA, or amino acid sequence to render.                 |
| `viewer`                 | `"linear"`, `"circular"`, `"both"`, `"both_flip"` | `"both"`                              | Viewer layout and orientation.                              |
| `name`                   | `str`                                             | `""`                                  | Name of the sequence or plasmid.                            |
| `annotations`            | `list[dict]`                                      | `[]`                                  | Sequence annotations (`start`, `end`, `name`, `direction`). |
| `primers`                | `list[dict]`                                      | `[]`                                  | Primer regions (same structure as annotations).             |
| `translations`           | `list[dict]`                                      | `[]`                                  | Sequence ranges to translate and display as amino acids.    |
| `enzymes`                | `list[str \| dict]`                               | `[]`                                  | Restriction enzymes or custom recognition sites.            |
| `highlights`             | `list[dict]`                                      | `[]`                                  | Sequence ranges to visually highlight.                      |
| `zoom_linear`            | `int`                                             | `50`                                  | Linear viewer zoom level (0–100).                           |
| `colors`                 | `list`                                            | `[]`                                  | Custom color palette.                                       |
| `bp_colors`              | `dict`                                            | `{}`                                  | Map of base pairs (A/T/G/C or index) to colors.             |
| `style`                  | `dict`                                            | `{"height": "70vh", "width": "100%"}` | Custom CSS sizing and layout.                               |
| `search`                 | `dict`                                            | `{}`                                  | Predefined search query.                                    |
| `show_complement`        | `bool`                                            | `True`                                | Display complement strand.                                  |
| `rotate_on_scroll`       | `bool`                                            | `True`                                | Enable circular rotation on scroll.                         |
| `disable_external_fonts` | `bool`                                            | `False`                               | Disable loading of external fonts.                          |
| `show_index`             | `bool`                                            | `True`                                | Show sequence index ticks.                                  |
| `key`                    | `str or None`                                     | `None`                                | Unique Streamlit key.                                       |

### Returns

A `dict` containing:

- `selection`: the current selected sequence region (if any)
- `search`: the current search matches and metadata
