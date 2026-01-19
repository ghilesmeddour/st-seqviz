import { FrontendRendererArgs } from "@streamlit/component-v2-lib";
import { FC, ReactElement } from "react";
import { SeqViz, SeqVizProps } from "seqviz";
import type { Selection } from "seqviz/dist/selectionContext";

export type SeqVizStreamlitStateShape = {
  selection: Selection;
  matches: any;
};

export type SeqVizStreamlitDataShape = SeqVizProps;

export type SeqVizStreamlitProps = Pick<
  FrontendRendererArgs<SeqVizStreamlitStateShape, SeqVizStreamlitDataShape>,
  "setStateValue"
> &
  SeqVizStreamlitDataShape;

const SeqVizStreamlit: FC<SeqVizStreamlitProps> = ({
  seq,
  viewer,
  name,
  annotations,
  primers,
  translations,
  enzymes,
  highlights,
  zoom,
  colors,
  bpColors,
  style,
  search,
  showComplement,
  rotateOnScroll,
  disableExternalFonts,
  showIndex,
  setStateValue,
}): ReactElement => {
  return (
    <span>
      <SeqViz
        seq={seq}
        viewer={viewer}
        name={name}
        annotations={annotations}
        primers={primers}
        translations={translations}
        enzymes={enzymes}
        highlights={highlights}
        zoom={zoom}
        colors={colors}
        bpColors={bpColors}
        style={style}
        search={search}
        showComplement={showComplement}
        rotateOnScroll={rotateOnScroll}
        disableExternalFonts={disableExternalFonts}
        showIndex={showIndex}
        onSelection={(selection) => {
          setStateValue?.("selection", selection);
        }}
        onSearch={(searchResults) => {
          setStateValue?.("matches", searchResults);
        }}
      />
    </span>
  );
};

export default SeqVizStreamlit;
