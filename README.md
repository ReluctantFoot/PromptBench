# PromptBench: LLM Prompt Engineering Evaluation Suite

PromptBench is a simple, reproducible framework for testing how different prompts affect the quality of LLM outputs with real metrics, datasets, and task-specific examples.

Test prompts on real tasks  
Score them with ROUGE / F1 / accuracy  
Measure *prompt quality*, not just model output  
Powered by Python, OpenAI API, and evaluate

---

## Quick Start

1. Clone the repo  
2. Install requirements  
3. Add your OpenAI key to `.env`
4. Run with flags

```bash
git clone https://github.com/yourusername/PromptBench.git
cd PromptBench
pip install -r requirements.txt
python run_evaluatation.py --set datasets/summarize.jsonl --prompt prompts/01_summarize.md
```

## How to Add Your Own Dataset & Prompt

### 1. Create a new dataset

Make a `.jsonl` file inside the `datasets/` folder.

Each line should be a complete JSON object with:
- `id`: a unique test case ID
- `input`: the input that will be sent to the LLM
- `target`: the correct or ideal model response (used for scoring)

**Example:**
```json
{"id": "001", "input": "NASA plans a lunar mission in 2026.", "target": "- NASA to launch in 2026\n- Mission to the Moon"}
```

### 2. Write a prompt file in Markdown

Create a .md file in the prompts/ folder with one or more prompt variants.
```markdown
## Baseline
Summarize the following sentence in one bullet.

## Refined
You are a concise editor. Summarize the sentence in exactly 1 bullet (max 15 words).
Only return the bullet point.
```
