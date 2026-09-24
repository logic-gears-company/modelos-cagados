import argparse
import time

import scipy.io.wavfile
import torch

from transformers import AutoProcessor, MusicgenForConditionalGeneration


MODEL = "/root/Modelos/models/musicgen-small"


def generate(prompt, output, seconds=5):
    print("Cargando MusicGen Small...")

    processor = AutoProcessor.from_pretrained(
        MODEL,
        local_files_only=True,
    )

    model = MusicgenForConditionalGeneration.from_pretrained(
        MODEL,
        local_files_only=True,
    )

    model = model.to("cpu")

    sampling_rate = model.config.audio_encoder.sampling_rate

    max_new_tokens = int(seconds * 50)

    inputs = processor(
        text=[prompt],
        padding=True,
        return_tensors="pt",
    )

    print(f"Prompt: {prompt}")
    print(f"Duración: {seconds}s")
    print("Generando música...")

    start = time.time()

    with torch.no_grad():
        audio_values = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
        )

    audio = audio_values[0, 0].cpu().numpy()

    scipy.io.wavfile.write(
        output,
        sampling_rate,
        audio,
    )

    print(f"Audio: {output}")
    print(f"Tiempo: {time.time() - start:.2f}s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--prompt", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--seconds", type=int, default=5)

    args = parser.parse_args()

    generate(
        args.prompt,
        args.output,
        args.seconds,
    )
