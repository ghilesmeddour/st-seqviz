import streamlit as st

pg = st.navigation(
    [
        "pages/Example_1.py",
        "pages/Example_2.py",
        "pages/Example_3.py",
    ],
    expanded=True,
)

pg.run()
