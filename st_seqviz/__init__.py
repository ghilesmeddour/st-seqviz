from typing import Literal

import streamlit as st

out = st.components.v2.component(
    "st-seqviz.st_seqviz",
    js="index-*.js",
    html='<div class="react-root"></div>',
)


def SeqViz(
    seq: str,
    viewer: Literal["linear", "circular", "both", "both_flip"] = "both",
    name: str = "",
    annotations: list[dict] = [],
    primers: list[dict] = [],
    translations: list[dict] = [],
    enzymes: list[str | dict] = [],
    highlights: list[dict] = [],
    zoom_linear: int = 50,
    colors: list = [],
    bp_colors: dict = {},
    style: dict = {"height": "70vh", "width": "100%"},
    search: dict = {},
    show_complement: bool = True,
    rotate_on_scroll: bool = True,
    disable_external_fonts: bool = False,
    show_index: bool = True,
    key: str | None = None,
) -> dict:
    """
    Display an interactive SeqViz viewer inside a Streamlit app.

    This component embeds the [SeqViz](https://github.com/Lattice-Automation/seqviz)
    DNA/RNA sequence viewer, allowing you to visualize sequences, annotations,
    primers, restriction sites, translations, and highlights directly within
    Streamlit.

    Parameters
    ----------
    seq : str
        The DNA, RNA, or amino acid sequence to display.
    viewer : {"linear", "circular", "both", "both_flip"}, default="both"
        Layout of the viewer(s):
        - `"linear"`: Only the linear view.
        - `"circular"`: Only the circular view.
        - `"both"`: Circular on the left and linear on the right.
        - `"both_flip"`: Linear on the left and circular on the right.
    name : str, optional
        Name of the sequence or plasmid. Displayed at the center of the
        circular viewer.
    annotations : list of dict, optional
        Sequence annotations. Each dict should include `start`, `end`,
        `name`, and `direction` (1 for forward, -1 for reverse).
    primers : list of dict, optional
        Primer regions. Same format as `annotations`.
    translations : list of dict, optional
        Sequence regions to translate and display as amino acids.
        Each dict should include `start`, `end`, and `direction`.
    enzymes : list of str or dict, optional
        Restriction enzymes to highlight. Can be a list of enzyme names
        or custom enzyme site definitions.
    highlights : list of dict, optional
        Sequence regions to visually highlight.
    zoom_linear : int, default=50
        Zoom level for the linear viewer (0–100).
    colors : list, optional
        Custom color palette for annotations and highlights.
    bp_colors : dict, optional
        Mapping of base pairs or indexes to custom colors.
    style : dict, optional
        CSS style overrides, e.g. `{"height": "70vh", "width": "100%"}`.
    search : dict, optional
        Predefined search configuration.
    show_complement : bool, default=True
        Whether to show the complement strand.
    rotate_on_scroll : bool, default=True
        Whether the circular viewer rotates when scrolling.
    disable_external_fonts : bool, default=False
        If True, prevents SeqViz from loading external fonts.
    show_index : bool, default=True
        Whether to display sequence index ticks.
    key : str or None, optional
        An optional unique key that identifies this component instance.

    Returns
    -------
    dict
        A dictionary containing the current selection and search results.

    Example
    -------
    ```python
    import streamlit as st
    from st_seqviz import SeqViz

    st.title("SeqViz Example")

    seq = "ATGCGTACTGACTGATCGTAGCTAG"
    result = SeqViz(
        seq=seq,
        name="Example Plasmid",
        viewer="both",
        annotations=[{"start": 2, "end": 10, "name": "geneX", "direction": 1}],
    )

    st.write(result)
    ```
    """
    result = out(
        key=key if key else f"seqviz-{name}",
        data={
            "seq": seq,
            "viewer": viewer,
            "name": name,
            "annotations": annotations,
            "primers": primers,
            "translations": translations,
            "enzymes": enzymes,
            "highlights": highlights,
            "zoom": {"linear": zoom_linear},
            "colors": colors,
            "bpColors": bp_colors,
            "style": style,
            "search": search,
            "showComplement": show_complement,
            "rotateOnScroll": rotate_on_scroll,
            "disableExternalFonts": disable_external_fonts,
            "showIndex": show_index,
        },
    )
    return result
