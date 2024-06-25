# import transformers
# from transformers import AutoConfig, AutoModelForCausalLM
# from datasets import load_dataset

# import ray
# from ray.train.huggingface.transformers import (
#     RayTrainReportCallback,
#     prepare_trainer,
# )
# from ray.train import ScalingConfig

# # Dataset
# def preprocess(examples):
#     ...

# hf_datasets = load_dataset("wikitext", "wikitext-2-raw-v1")
# processed_ds = hf_datasets.map(preprocess, ...)

# ray_train_ds = ray.data.from_huggingface(processed_ds["train"])
# ray_eval_ds = ray.data.from_huggingface(processed_ds["evaluation"])

# # [1] Define the full training function
# # =====================================
# def train_func():
#     MODEL_NAME = "gpt2"
#     model_config = AutoConfig.from_pretrained(MODEL_NAME)
#     model = AutoModelForCausalLM.from_config(model_config)

#     # [2] Build Ray Data iterables
#     # ============================
#     train_dataset = ray.train.get_dataset_shard("train")
#     eval_dataset = ray.train.get_dataset_shard("evaluation")

#     train_iterable_ds = train_dataset.iter_torch_batches(batch_size=8)
#     eval_iterable_ds = eval_dataset.iter_torch_batches(batch_size=8)

#     args = transformers.TrainingArguments(
#         output_dir=f"{MODEL_NAME}-wikitext2",
#         evaluation_strategy="epoch",
#         save_strategy="epoch",
#         logging_strategy="epoch",
#         learning_rate=2e-5,
#         weight_decay=0.01,
#         max_steps=100,
#     )

#     trainer = transformers.Trainer(
#         model=model,
#         args=args,
#         train_dataset=train_iterable_ds,
#         eval_dataset=eval_iterable_ds,
#     )

#     # [3] Inject Ray Train Report Callback
#     # ====================================
#     trainer.add_callback(RayTrainReportCallback())

#     # [4] Prepare your trainer
#     # ========================
#     trainer = prepare_trainer(trainer)
#     trainer.train()

# # Build a Ray TorchTrainer
# scaling_config = ScalingConfig(num_workers=4, use_gpu=True)
# ray_trainer = TorchTrainer(
#     train_func,
#     scaling_config=scaling_config,
#     datasets={"train": ray_train_ds, "evaluation": ray_eval_ds},
# )
# result = ray_trainer.fit()

if __name__ == "__main__":
    print("Training...")
