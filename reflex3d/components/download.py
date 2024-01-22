from typing import List, Dict, Any

import reflex as rx
from reflex.components.tags import Tag


class StreamFile(rx.Component):
    tag = "StreamFile"
    # Define the vars and event triggers if needed
    bytes_: rx.Var[str]

    def _get_custom_code(self) -> str:
        return """
const StreamFile = ({ bytes_ }) => {
  const [url, setUrl] = useState(null);

  useEffect(() => {
    if (bytes_ && bytes_.trim() !== "") {
      const byteCharacters = atob(bytes_);
      const byteNumbers = new Array(byteCharacters.length);
      for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
      }
      const byteArray = new Uint8Array(byteNumbers);
      const blob = new Blob([byteArray], { type: 'model/stl' });
      const blobUrl = URL.createObjectURL(blob);
      setUrl(blobUrl);
    }
    else {
    try {
      URL.revokeObjectURL(blobUrl);
    } catch (error) { }
        
    }
  }, [bytes_]);

  return (
    <div>
      {url ? (
        <a href={url} download="model.stl">
          <button>Download STL File</button>
        </a>
      ) : (
        <button disabled>Download STL File</button>
      )}
    </div>
  );
};
        """

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag(name="StreamFile", props={"bytes_": self.bytes_})
