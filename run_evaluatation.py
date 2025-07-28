import os, json, argparse
from dotenv import load_dotenv
from openai import OpenAI
import evaluate
from rich.console import Console

console = Console()
load_dotenv()
client = OpenAI()
rouge = evaluate.load("rouge")

def get_prompt(prompt_path):
    with open(prompt_path, "r") as f:
        return f.read()

def call_llm(prompt, user_input):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

def score(dataset_path, prompt):
    preds, refs = [], []
    with open(dataset_path, "r") as f:
        for line in f:
            item = json.loads(line)
            output = call_llm(prompt, item["input"])
            preds.append(output)
            refs.append(item["target"])
            console.log(f"[bold green]✓[/] ID {item['id']} done")
    scores = rouge.compute(predictions=preds, references=refs)
    console.rule("[bold cyan]Evaluation Complete")
    for k, v in scores.items():
        console.print(f"[bold yellow]{k}[/]: {v:.3f}")
    return scores

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--set", required=True, help="Path to JSONL dataset")
    parser.add_argument("--prompt", required=True, help="Path to .md prompt")
    args = parser.parse_args()

    prompt_text = get_prompt(args.prompt)
    score(args.set, prompt_text)
