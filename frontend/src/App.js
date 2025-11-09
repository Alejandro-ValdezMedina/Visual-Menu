import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [menuItems, setMenuItems] = useState([]);
  const [generatedImage, setGeneratedImage] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    const response = await fetch("http://localhost:8000/api/upload-image", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setMenuItems(data.items);
  };

  const handleItemClick = async (itemName) => {
    const response = await fetch(`http://localhost:8000/api/generate/${itemName}`);
    const data = await response.json();
    setGeneratedImage(data.image_url);
  };

  return (
    <div className = "App">
      <h1> Visual Menu</h1>
      <input
      type = "file"
      accept = "image/*"
      onChange = {handleFileChange}
      />

      <button onClick = {handleUpload}>
        Upload Menu
      </button>

      <div>
  <h2> Menu Items:</h2>
  {menuItems.map((item, index) => (
    <div key={index}>
      <h3>{item.name}</h3>
      
      <p 
        style={{cursor: "pointer", color: "blue"}} 
        onClick={() => handleItemClick(item.description)}
      >
        {item.description}
      </p>
    </div>
  ))}
</div>
      {generatedImage && (
        <div>
          <h2> Generated Image:</h2>
          <img src = {generatedImage} alt = "Generated Image" />
        </div>
      )}
    </div>
  );
}

export default App;
