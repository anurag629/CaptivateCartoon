import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [caption, setCaption] = useState("");
  const [story, setStory] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Create a new form data object
    const formData = new FormData();
    formData.append("file", file);

    try {
      // Make an API request to the backend
      const response = await axios.post(
        "https://anurag629-legendary-succotash-rx6v95wqj6x3p5j7-8000.preview.app.github.dev/imagetodetail/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      // Set the result, caption and story states with the response data
      setResult(response.data.result);
      setCaption(response.data.caption);
      setStory(response.data.story);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Submit</button>
      </form>

      {result && (
        <div>
          <p>Largest Emotion: {result.largest_emotion}</p>
          <p>Second Largest Emotion: {result.second_largest_emotion}</p>
          <p>Age: {result.age}</p>
          <p>Dominant Gender: {result.dominant_gender}</p>
        </div>
      )}

      {caption && <p>{caption}</p>}
      {story && <p>{story}</p>}
    </div>
  );
}

export default App;
