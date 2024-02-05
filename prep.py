import runpod
import os
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig

base_model_id = "./zephyr"

tokenizer = AutoTokenizer.from_pretrained(
    base_model_id, add_bos_token=True, trust_remote_code=True
)

config = PeftConfig.from_pretrained("./superflows")
model = AutoModelForCausalLM.from_pretrained(base_model_id)
