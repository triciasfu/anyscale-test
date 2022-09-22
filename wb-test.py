import ray

from ray.air.config import RunConfig, ScalingConfig
from ray.air.result import Result
from ray.train.xgboost import XGBoostTrainer
from ray.air.callbacks.wandb import WandbLoggerCallback

def get_train_dataset() -> ray.data.Dataset:
    dataset = ray.data.read_csv("s3://anonymous@air-example-data/breast_cancer.csv")
    return dataset
    
def train_model(train_dataset: ray.data.Dataset) -> Result:
    """Train a simple XGBoost model and return the result."""
    trainer = XGBoostTrainer(
        scaling_config=ScalingConfig(num_workers=2),
        params={"tree_method": "auto"},
        label_column="target",
        datasets={"train": train_dataset},
        num_boost_round=10,
        run_config=RunConfig(
            callbacks=[
                # This is the part needed to enable logging to Weights & Biases.
                # It assumes you've logged in before, e.g. with `wandb login`.
                WandbLoggerCallback(
                    save_checkpoints=True,
                )
            ]
        ),
    )
    result = trainer.fit()
    return result
  
train_dataset = get_train_dataset()
result = train_model(train_dataset=train_dataset)
