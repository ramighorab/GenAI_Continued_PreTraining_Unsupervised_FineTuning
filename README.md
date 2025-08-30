# My POC GenAI project for LLM Continued Pre-training (a.k.a. Unsupervised Fine-tuning) on custom docs 

This project demonstrates how to perform continued pre-training (unsupervised fine-tuning) on a local language model to adapt it to a specialized domain. Using Meta's Llama 3 8B model, the script processes a collection of custom PDF documents—in this case, economic reports from sources like the UN and UK Parliament—to create a training corpus. The fine-tuning is accomplished in an efficient manner by leveraging Parameter-Efficient Fine-Tuning (PEFT) with LoRA. The repository includes the full end-to-end pipeline, from data preparation to training, and concludes with an inference script that compares the newly specialized model's responses against the original base model to highlight the enhanced domain-specific knowledge.

### Prerequisites

1. Install the required packages (only if you'll run locally on your machine):

```bash
pip install -r requirements.txt
```

### Running the project
The project is simply stored as a Jupyter notebook. Recommended to run from Google Colab, with a T4 GPU (free tier should be enough)