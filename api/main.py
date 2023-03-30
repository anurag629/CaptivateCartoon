import shutil
import os
import captivatecartoon as cc

from fastapi import FastAPI, File, UploadFile

print("Hello from api/main.py")


app = FastAPI()


@app.get("/")
def read_root():
    '''
    This is the root of the API.
    '''
    return {"Hello": "World"}


# API endpoint `imagetodetail` which will accept image and then call the `image_to_detail(img)` function which return detail from the `imageToDetail.py`.
@app.post("/imagetodetail/")
async def imagetodetail(file: UploadFile = File(...)):
    '''
    This API endpoint will accept image and then call the `image_to_detail(img)` function which return detail from the `imageToDetail.py`.
    '''
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
