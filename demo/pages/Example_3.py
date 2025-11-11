import streamlit as st

from st_seqviz import SeqViz

st.set_page_config(
    page_title="DNA, RNA, and protein sequence viewer",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

c1, c2 = st.columns(2, border=True)

with c1:
    _ = SeqViz(
        seq="TTGACGGCTAGCTCAGTCCTAGGTACAGTGCTAGC",
        name="J23100",
        annotations=[
            {"name": "promoter", "start": 0, "end": 34, "direction": 1, "color": "blue"}
        ],
    )

with c2:
    _ = SeqViz(
        seq="tcgcgcgtttcggtgatgacggtgaaaacctctgacacatgca",
        name="L09136",
        viewer="both_flip",
    )

c1, c2 = st.columns(2, border=True)

with c1:
    st.markdown("### mCherry")
    _ = SeqViz(
        name="mCherry",
        seq="MVSKGEEDNMAIIKEFMRFKVHMEGSVNGHEFEIEGEGEGRPYEGTQTAKLKVTKGGPLPFAWDILSPQFMYGSKAYVKHPADIPDYFKQSFPEGFTWERVTTYEDGGVLTATQDTSLQDGCLIYNVKIRGVNFPSDGPVMQKKTMGWEASTERLYPRDGVLKGEIHKALKLKDGGHYDAEVKTTYKAKKPVQLPGAYNVNIKLDITSHNEDYTIVEQYERAEGRHSTGGMDELYK",
        viewer="linear",
    )

with c2:
    _ = SeqViz(
        name="mNeonGreen",
        seq="MVSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKQHDFFKSAMPEGYIQERTIFFKDDGNYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNYNSHNVYIMADKQKNGIKVNFKIRHNIEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSALSKDPNEKRDHMVLLEFVTAAGITLGMDELYK",
        viewer="circular",
    )
