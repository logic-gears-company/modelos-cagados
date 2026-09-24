import subprocess
import time
from pathlib import Path
from datetime import datetime


ROOT = Path("/root/Modelos")
IMAGE_DIR = ROOT / "outputs/images"
AUDIO_DIR = ROOT / "outputs/audio"
TEXT_DIR = ROOT / "outputs/text"


def run(command):
    subprocess.run(command, cwd=ROOT, check=True)


def image(prompt):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output = IMAGE_DIR / f"image-{timestamp}.png"

    run([
        "python",
        "image.py",
        "--prompt",
        prompt,
        "--output",
        str(output),
        "--steps",
        "20",
    ])

    run([
        "python",
        "github_image.py",
        str(output),
    ])

    print(f"\nGitHub: {output}")


def text(prompt):
    run([
        "python",
        "text.py",
    ])


def music(prompt):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output = AUDIO_DIR / f"music-{timestamp}.wav"

    run([
        "python",
        "music.py",
        "--prompt",
        prompt,
        "--output",
        str(output),
        "--seconds",
        "5",
    ])


def voice(prompt):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output = AUDIO_DIR / f"voice-{timestamp}.wav"

    run([
        "python",
        "voice.py",
        "--text",
        prompt,
        "--output",
        str(output),
    ])


print("""
==========================================
       MODELOS — MINI AI LAB
==========================================

/imagen  <prompt>   Generar imagen + subir GitHub
/texto   <prompt>   Generar texto español
/musica  <prompt>   Generar música
/voz     <texto>    Generar voz

/salir               Salir
==========================================
""")

while True:
    try:
        command = input("\nTú: ").strip()

        if not command:
            continue

        if command == "/salir":
            break

        if command.startswith("/imagen "):
            image(command[8:])
            continue

        if command.startswith("/texto "):
            text(command[7:])
            continue

        if command.startswith("/musica "):
            music(command[8:])
            continue

        if command.startswith("/voz "):
            voice(command[5:])
            continue

        print("Comandos: /imagen /texto /musica /voz /salir")

    except KeyboardInterrupt:
        print("\nSaliendo...")
        break
