import argparse
import subprocess
from pathlib import Path


MODEL = "/root/Modelos/models/piper/es_ES-davefx-medium.onnx"


def generate(text, output):
    Path(output).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    subprocess.run(
        [
            "python",
            "-m",
            "piper",
            "--model",
            MODEL,
            "--output_file",
            output,
            "--",
            text,
        ],
        check=True,
    )

    print(f"Voz: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--text", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    generate(
        args.text,
        args.output,
    )
