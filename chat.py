import subprocess

def ollama_query(prompt, model_name="llama3.1:8b"):
    result = subprocess.run(
        ["ollama", "run", model_name, prompt],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()

response = ollama_query("Explain the benefits of running LLaMA locally on GPU.")
print(response)
