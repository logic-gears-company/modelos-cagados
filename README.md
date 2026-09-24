# Modelos

Mini laboratorio local de IA para experimentación.

## Componentes

- Tiny-SD — generación de imágenes
- GPT-2 Small Spanish — generación de texto en español
- MusicGen Small — generación básica de música
- Piper es_ES-davefx-medium — síntesis de voz en español

## Estructura

- `models/` — modelos locales, no incluidos en Git
- `outputs/images/` — imágenes generadas
- `outputs/audio/` — audio generado
- `outputs/text/` — texto generado
- `image.py` — generación de imágenes
- `text.py` — generación de texto
- `music.py` — generación de música
- `voice.py` — síntesis de voz
- `chat.py` — interfaz unificada
- `github_image.py` — subida automática de imágenes a GitHub
