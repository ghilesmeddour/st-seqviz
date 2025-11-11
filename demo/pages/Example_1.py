import hashlib
from io import StringIO
from typing import Dict, List

import streamlit as st
from Bio import Entrez, SeqIO
from Bio.SeqRecord import SeqRecord

from st_seqviz import SeqViz


def genbank_to_seqviz_annotations(record: SeqRecord) -> List[Dict]:
    """
    Convert coding sequence (CDS) features from a GenBank SeqRecord
    into a list of annotations compatible with SeqViz.

    Parameters
    ----------
    record : SeqRecord
        A Biopython SeqRecord object parsed from a GenBank file, typically obtained via SeqIO.

    Returns
    -------
    list of dict
        A list of annotation dictionaries. Each annotation contains:
        - name: the gene or product name
        - start: feature start position (0-based)
        - end: feature end position
        - direction: 1 (forward), -1 (reverse), or 0 (unknown)
        - type: feature type (e.g., 'CDS')
        - color: a consistent hex color derived from the feature name

    Notes
    -----
    - Only "CDS" features are included.
    - Feature names are resolved in order of priority: `gene` → `product` → `type`.
    - Colors are deterministically generated from the MD5 hash of the feature name.

    Example
    -------
    >>> record = SeqIO.read("example.gb", "genbank")
    >>> annotations = genbank_to_seqviz_annotations(record)
    >>> print(annotations[0])
    {'name': 'geneX', 'start': 123, 'end': 456, 'direction': 1,
     'type': 'CDS', 'color': '#a1b2c3'}
    """
    annotations = []
    for f in record.features:
        if f.type == "CDS":
            start = int(f.location.start)
            end = int(f.location.end)

            name = (
                f.qualifiers.get("gene", [""])[0]
                or f.qualifiers.get("product", [""])[0]
                or f.type
            )

            strand = getattr(f.location, "strand", 0)
            direction = 1 if strand == 1 else -1 if strand == -1 else 0

            color_hash = hashlib.md5(name.encode("utf-8")).hexdigest()[:6]

            annotations.append(
                {
                    "name": name,
                    "start": start,
                    "end": end,
                    "direction": direction,
                    "type": f.type,
                    "color": f"#{color_hash}",
                }
            )

    return annotations


@st.cache_data
def get_data(
    accession: str = "MN623123.1", email: str = "example@domain.com"
) -> SeqIO.SeqRecord:
    """
    Fetch a nucleotide sequence record from NCBI's GenBank database using an accession ID.

    Parameters
    ----------
    accession : str, optional
        The GenBank accession number of the sequence to fetch (default is "MN623123.1").
    email : str, optional
        Email address used to identify the requester to NCBI (required by NCBI Entrez policy).
        It is recommended to provide a valid contact address when deploying publicly.

    Returns
    -------
    SeqRecord
        A Biopython SeqRecord object containing the full GenBank record, including sequence,
        annotations, and metadata.

    Notes
    -----
    - The provided email is passed to NCBI for API identification.

    Example
    -------
    >>> record = get_data("MN623123.1", email="me@lab.org")
    >>> print(record.id)
    MN623123.1
    >>> print(record.seq[:50])
    ATGGAAGGTCTCCTG...
    """
    Entrez.email = email

    with Entrez.efetch(
        db="nuccore", id=accession, rettype="gb", retmode="text"
    ) as handle:
        record = SeqIO.read(StringIO(handle.read()), "genbank")

    return record


st.set_page_config(
    page_title="DNA, RNA, and protein sequence viewer",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.markdown("### Settings")

accession = st.sidebar.text_input("Accession", value="MN623123.1")
email = st.sidebar.text_input("Email", value="example@domain.com")

viewer = st.sidebar.segmented_control(
    "Topology", ["linear", "circular", "both", "both_flip"], default="both"
)
zoom_linear = st.sidebar.slider("Zoom", min_value=0, max_value=100, step=10, value=50)
search_query = st.sidebar.text_input("Search", placeholder="Search...")
show_complement = st.sidebar.toggle("Show complement", True)
show_index = st.sidebar.toggle("Show index", True)
enzymes = st.sidebar.pills(
    "Enzymes",
    ["PstI", "EcoRI", "XbaI", "SpeI"],
    default=["PstI", "EcoRI", "XbaI", "SpeI"],
    selection_mode="multi",
)

record = get_data(accession, email)
annotations = genbank_to_seqviz_annotations(record)


sv = SeqViz(
    seq=str(record.seq),
    viewer=viewer,
    name=record.id,
    annotations=annotations,
    enzymes=enzymes,
    search={"query": search_query, "mismatch": 0},
    zoom_linear=zoom_linear,
    show_complement=show_complement,
    show_index=show_index,
)

st.sidebar.divider()
st.sidebar.markdown("### Selection and matches")
st.sidebar.json(sv, expanded=1)
