import shutil
import os

# from .details import detail
from .prompts import prompt
from .storys import story
from .captions import caption
from .details import detail


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
    result = detail(file_location)
    prompts = prompt(file_location)

    # Gettting the caption and story
    cap = caption(prompts['caption'])
    stor = story(prompts['story'])

    # Delete the file
    os.remove(file_location)

    # Return the result
    return {"result": result,
            "caption": cap,
            "story": stor,
            }
