import argparse
import time
from pathlib import Path

import torch
from diffusers import DiffusionPipeline


MODEL = "/root/Modelos/models/tiny-sd"


def generate(prompt, output, steps=20, seed=12345):
    print("Cargando modelo de imagen...")

    pipe = DiffusionPipeline.from_pretrained(
        MODEL,
        torch_dtype=torch.float32,
        local_files_only=True,
    )

    pipe = pipe.to("cpu")

    generator = torch.Generator(device="cpu").manual_seed(seed)

    print(f"Prompt: {prompt}")
    print(f"Steps: {steps}")
    print(f"Seed: {seed}")
    print("Generando...")

    start = time.time()

    image = pipe(
        prompt=prompt,
        height=512,
        width=512,
        num_inference_steps=steps,
        generator=generator,
    ).images[0]

    elapsed = time.time() - start

    Path(output).parent.mkdir(parents=True, exist_ok=True)
    image.save(output)

    print(f"Imagen: {output}")
    print(f"Tiempo: {elapsed:.2f}s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--prompt", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--steps", type=int, default=20)
    parser.add_argument("--seed", type=int, default=12345)

    args = parser.parse_args()

    generate(
        args.prompt,
        args.output,
        args.steps,
        args.seed,
    )
