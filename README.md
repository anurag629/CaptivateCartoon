# CAPTITVATECARTOON

# Image Detail Extractor and Caption, Story Generator

This is a simple web application that allows you to upload an image and get details about the image, caption and story for the image.

## Requirements

- Python 3.6 or higher
- React 16.8 or higher
- FastAPI
- Tensorflow

## Installation

1. Clone the repository:

        git clone https://github.com/anurag629/CaptivateCartoon.git
    

2. Install the backend dependencies:

        cd CaptivateCartoon
        pip install -r requirements.txt


3. Install the frontend dependencies:

        npm install



## Usage

1. Start the backend server:

        cd api
        uvicorn main:app --reload


2. Start the frontend server:
    
        cd app
        npm start


3. Open your web browser and navigate to `http://localhost:3000` to use the application.



## API Endpoints


### `imagetodetail`

This endpoint accepts an image file and returns a JSON object containing details about the image, caption and story for the image.

**Method:** POST

**Endpoint:** `/imagetodetail/`

**Request Body:** A multipart/form-data object containing a single `image` field, which should contain the image file.

**Response Body:** A JSON object containing the following fields:

<!-- "result": result,
                "caption": cap,
                "story": stor,
                 -->
- `result`: A JSON object containing the following fields:
    - `largest_emotion`: The most dominant emotion detected in the image.
    - `second_largest_emotion`: The second most dominant emotion detected in the image.
    - `age`: The age of the person(s) in the image.
    - `dominant_gender`: The gender of the person(s) in the image.
- `caption`: The caption for the image.
- `story`: The story for the image.

## Frontend Components

### `ImageUploader`

This component allows the user to upload an image to the server.

**Props:**

- `onUpload`: A function that will be called when an image is uploaded. The function will be passed the image details as a JSON object.

### `ImageDetails`

This component displays the details of an image that has been uploaded.

**Props:**

- `details`: A JSON object containing the details of the image.

## Backend Functions

### `detail`

This function accepts an image file and returns a JSON object containing details about the image.

**Arguments:**

- `image`: The image file.

**Returns:** Resonse from deepface api.

### `prompt`

This function accepts an image file and returns a JSON object containing prompt for the image.

**Arguments:**

- `image`: The image file.

**Returns:** This function calls `detail` function and returns a JSON object containing prompt for generating caption and story.



### `caption`

This function accepts an image file and returns a JSON object containing caption for the image.

**Arguments:**

- `image`: The image file.

**Returns:** Resonse from chatgpt api.

### `story`

This function accepts an image file and returns a JSON object containing story for the image.

**Arguments:**

- `image`: The image file.

**Returns:** Resonse from chatgpt api.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
