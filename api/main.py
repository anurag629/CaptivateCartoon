import shutil
import os
import uvicorn
from io import BytesIO
import base64

# Project imports
import captivatecartoon as cc

# FastAPI imports
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import JSONResponse
from auth_token import auth_token
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    '''
    This is the root of the API.
    '''
    return {"Hello": "World"}


# API endpoint `imagetodetail` which will accept image and then call the `image_to_detail(img)` function which return detail from the `imageToDetail.py`.
@app.post("/imagetodetail/")
async def imagetodetail(file: UploadFile):
    '''
    This API endpoint will accept image and then call the `image_to_detail(img)` function which return detail from the `imageToDetail.py`.
    '''
    try:
        # Save the uploaded file to a directory
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Call any function with the saved file path
        result = cc.detail(file_location)
        prompts = cc.prompt(file_location)

        # Gettting the caption and story
        cap = cc.caption(prompts['caption'])
        stor = cc.story(prompts['story'])

        # Delete the file
        os.remove(file_location)

        # Return the result
        return {"result": result,
                "caption": cap,
                "story": stor,
                }
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": str(e)})




@app.get("/texttoimage/")
def texttoimage(text: str):
    '''
    This API endpoint will accept text and then call the `text_to_image(text)` function which return image from the `textToImage.py`.
    '''
    try:
        # Call any function with the saved file path
        result = cc.text_to_image(text)

        # Return the result
        return {"result": result}
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": str(e)})
    

    
# at last, the bottom of the file/module
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5044)
