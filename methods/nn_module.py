import pytorch_lightning as pl

from methods.models.pwcnet import pwcnet


class NNModule(pl.LightningModule):
    def __init__(self) -> None:
        super().__init__()

        self.model_fn = pwcnet()

    def training_step(self, batch, batch_idx: int):
        return super().training_step(*args, **kwargs)
        