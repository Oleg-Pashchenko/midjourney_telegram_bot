
import replicate

model = replicate.models.get("tstramer/midjourney-diffusion")
version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")

# https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#input
inputs = {
    # Input prompt
    'prompt': "Поэт Александр Сергеевич Пушкин на параде ЛГБТ",
    'width': 576,
    'height': 1024,
    'prompt_strength': 0.8,
    'num_outputs': 1,
    'num_inference_steps': 50,
    'guidance_scale': 7.5,
    'scheduler': "DPMSolverMultistep",

    # Random seed. Leave blank to randomize the seed
    # 'seed': ...,
}
import time
start = time.time()
# https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#output-schema
output = version.predict(**inputs)
print(output)
print(time.time() - start)
