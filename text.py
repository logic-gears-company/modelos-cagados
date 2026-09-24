from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL = "/root/Modelos/models/gpt2-small-spanish"

print("Cargando GPT-2 español...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL,
    local_files_only=True,
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    local_files_only=True,
)

print("Modelo listo.")


def generate(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_new_tokens=120,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id,
    )

    text = tokenizer.decode(
        output[0],
        skip_special_tokens=True,
    )

    return text


if __name__ == "__main__":
    while True:
        try:
            prompt = input("\nTú: ")

            if prompt.lower() in ("salir", "exit", "quit"):
                break

            print("\nIA:", generate(prompt))

        except KeyboardInterrupt:
            break
