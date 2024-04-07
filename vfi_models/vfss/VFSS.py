import itertools
import numpy as np
from .model.VFSS_infer_b import Model_inference
import torch


class VFSS:
    def __init__(self):
        self.cache = False
        self.amount_input_img = 2

        torch.set_grad_enabled(False)
        torch.backends.cudnn.enabled = True
        torch.backends.cudnn.benchmark = True

        self.model = Model_inference()
        self.model.eval()

    def execute(self, I0, I1, timestep):
        with torch.inference_mode():
            middle = self.model(I0, I1, timestep).cpu()
        return middle