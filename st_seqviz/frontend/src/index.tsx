import { Component, ComponentArgs } from "@streamlit/component-v2-lib";
import { StrictMode } from "react";
import { createRoot, Root } from "react-dom/client";

import SeqVizStreamlit, {
  SeqVizStreamlitDataShape,
  SeqVizStreamlitStateShape,
} from "./SeqVizStreamlit";

// Handle the possibility of multiple instances of the component to keep track
// of the React roots for each component instance.
const reactRoots: WeakMap<ComponentArgs["parentElement"], Root> = new WeakMap();

const SeqVizStreamlitRoot: Component<
  SeqVizStreamlitStateShape,
  SeqVizStreamlitDataShape
> = (args) => {
  const { data, parentElement, setStateValue } = args;

  // Get the react-root div from the parentElement that we defined in our
  // `st.components.v2.component` call in Python.
  const rootElement = parentElement.querySelector(".react-root");

  if (!rootElement) {
    throw new Error("Unexpected: React root element not found");
  }

  // Check to see if we already have a React root for this component instance.
  let reactRoot = reactRoots.get(parentElement);
  if (!reactRoot) {
    // If we don't, create a new root for the React application using the React
    // DOM API.
    // @see https://react.dev/reference/react-dom/client/createRoot
    reactRoot = createRoot(rootElement);
    reactRoots.set(parentElement, reactRoot);
  }

  // Here we are accessing the data passed from Streamlit on the Python side.
  const {
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
  } = data;

  // Render/re-render the React application into the root using the React DOM
  // API.
  reactRoot.render(
    <StrictMode>
      <SeqVizStreamlit
        setStateValue={setStateValue}
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
      />
    </StrictMode>,
  );

  // Return a function to cleanup the React application in the Streamlit
  // component lifecycle.
  return () => {
    const reactRoot = reactRoots.get(parentElement);

    if (reactRoot) {
      reactRoot.unmount();
      reactRoots.delete(parentElement);
    }
  };
};

export default SeqVizStreamlitRoot;
