from auth_token import auth_token
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline


device = "cuda" if torch.cuda.is_available() else "cpu"
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id,
                                               revision="fp16",
                                               torch_dtype=torch.float16,
                                               use_auth_token=auth_token
                                               )

pipe.to(device)


def text_to_image(text: str):
    with autocast(device):
        image = pipe(text, guidance_scale=8.5).image[0]

    image.save(f"/uploads/{text[:8]}.jpg")

    return f"/uploads/{text[:8]}.jpg"
