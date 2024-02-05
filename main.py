import runpod
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig

base_model_id = "./zephyr"
ft_model_id = "./superflows"

tokenizer = AutoTokenizer.from_pretrained(
    base_model_id, add_bos_token=True, trust_remote_code=True
)

config = PeftConfig.from_pretrained(ft_model_id)
model = AutoModelForCausalLM.from_pretrained(base_model_id)

ft_model = PeftModel.from_pretrained(model, ft_model_id).to("cuda")

# pipe = pipeline(
#     "text-generation",
#     model="Superflows/Superflows-1",
#     torch_dtype=torch.bfloat16,
#     device_map="auto",
#     token=os.environ["HF_TOKEN"],
# )


def handler(job):
    print("Received job:", job)
    job_input = job["input"]
    prompt = tokenizer(
        tokenizer.apply_chat_template(
            job_input["messages"], tokenize=False, add_generation_prompt=True
        ),
        return_tensors="pt",
    ).to("cuda")
    return (
        tokenizer.decode(
            ft_model.generate(
                **prompt,
                max_new_tokens=job_input.get("max_tokens", 256),
                temperature=job_input.get("temperature", 0.7)
            )[0],
            skip_special_tokens=True,
        )
        .split("<|assistant|>")[-1]
        .strip()
    )
    # prompt = pipe.tokenizer.apply_chat_template(
    #     job_input["messages"], tokenize=False, add_generation_prompt=True
    # )
    # outputs = pipe(
    #     prompt,
    #     max_new_tokens=job_input["max_tokens"],
    #     do_sample=True,
    #     temperature=0.7,
    #     top_k=50,
    #     top_p=0.95,
    # )
    # return outputs[0]["generated_text"].split("<|assistant|>")[-1].strip()


runpod.serverless.start({"handler": handler})
