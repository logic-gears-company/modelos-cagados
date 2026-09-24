import subprocess
from pathlib import Path


ROOT = Path("/root/Modelos")


def upload(image):
    image = Path(image)

    subprocess.run(
        ["git", "add", str(image)],
        cwd=ROOT,
        check=True,
    )

    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            f"Add generated image {image.name}",
        ],
        cwd=ROOT,
        check=False,
    )

    subprocess.run(
        ["git", "push", "origin", "main"],
        cwd=ROOT,
        check=True,
    )

    print("Imagen subida a GitHub.")


if __name__ == "__main__":
    import sys

    upload(sys.argv[1])
