from huggingface_hub import HfApi, list_models

models = list_models(filter="AnimateDiff-Lightning")

for model in models:
    print(model.modelId)
