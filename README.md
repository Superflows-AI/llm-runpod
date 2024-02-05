### Superflows RunPod setup

This repo is for using the Superflows fine-tuned LLM on https://runpod.io.

You want to download the model weights from hugging face and put all `model-0000X-of-0000Y.safetensors` files in the `/zephyr` directory.

The `adapter_model.safetensors` file should live in the `/superflows` directory.

These files aren't included in this repo because they are too large.

### Deployment
You need to:
1. make a RunPod account
2. build the docker container using the Dockerfile in this repo
3. push the docker container to a container registry
4. deploy the container to RunPod

Reach out to henry@superflows.ai if you have any questions or need help with this process.
