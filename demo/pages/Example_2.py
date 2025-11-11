import streamlit as st

from st_seqviz import SeqViz

st.set_page_config(
    page_title="DNA, RNA, and protein sequence viewer",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded",
)

seq = st.text_input(
    "Sequence",
    value="TTGACGGCTAGCTCAGTCCTAGGTACAGTGCTAGC",
    placeholder="Sequence to render. Can be a DNA, RNA, or amino acid sequence.",
)
name = st.text_input("Name", value="J23100", placeholder="Name of the sequence.")

sv = SeqViz(
    seq=seq,
    name=name,
    key=f"seqviz-{name}-example-2",
)

st.sidebar.json(sv, expanded=1)
