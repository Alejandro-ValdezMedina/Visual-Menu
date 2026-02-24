import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [menuItems, setMenuItems] = useState([]);
  const [generatedImage, setGeneratedImage] = useState({});
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a file");
      return;
    }
    
    setIsLoading(true);
  
    try {
      const formData = new FormData();
      formData.append("file", selectedFile);
  
      const response = await fetch("http://localhost:8000/api/upload-image", {
        method: "POST",
        body: formData,
      });
  
      const data = await response.json();
      setMenuItems(data.items);
  
      const images = {};
      for (const item of data.items) {
        const imageResponse = await fetch(`http://localhost:8000/api/generate/${encodeURIComponent(item.description)}`);
        const imageData = await imageResponse.json();
        images[item.name] = imageData.image_url;
      }
      
      setGeneratedImage(images);
      setIsLoading(false);
    } catch (error) {
      console.error("Error:", error);
      setIsLoading(false);
      alert("Failed to process menu. Please try again.");
    }
  };

  return (
    <div className = "App">
      <h1> Visual Menu</h1>
      <p className="subtitle">Upload a menu photo and see AI-generated images of each dish</p>
      <div className="upload-section">
        <div className="file-input-wrapper">
          <input 
            type="file" 
            accept="image/*" 
            onChange={handleFileChange}
            id="file-input"
          />
          <label htmlFor="file-input" className="file-input-label">
            Choose Menu Image
          </label>
          {selectedFile && (
            <span className="file-name">{selectedFile.name}</span>
          )}
          
        </div>
        <br />
        <button onClick={handleUpload} disabled={isLoading}>
          {isLoading ? "Processing... Please wait" : "Upload Menu"}
        </button>
      </div>

        {isLoading && (
          <div className="loading-message">
            Analyzing menu and generating images... This may take a few moments.
          </div>
        )}

<div className="menu-items-section">
  {menuItems.length > 0 ? (
    <>
      <h2>Menu Items:</h2>
      {menuItems.map((item, index) => (
        <div key={index} className="menu-item-card">
          <h3>{item.name}</h3>
          <p>{item.description}</p>
          {generatedImage[item.name] && (
            <img src={generatedImage[item.name]} alt={item.name} />
          )}
        </div>
      ))}
    </>
  ) : (
    <div className="empty-state">
      Upload a menu image to get started
    </div>
  )}
</div>
</div>
  );
}

export default App;
