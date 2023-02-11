from typing import Optional
from torch.nn import functional as F
import torch


class HeadVer3:
    def __init__(self):
        self.wei: Optional[torch.Tensor] = None

    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        """
        :param x: (B, T, C)
        :return: out (B, T, C)
        """
        # --- TODO 4 --- #

        T = x.shape[1]
        tril = torch.tril(torch.ones(x.shape[1], x.shape[1]))
        wei = torch.zeros((T,T))
        wei = wei.masked_fill(tril == 0, float('-inf'))
        self.wei = F.softmax(wei, dim=1)
        out = wei @ x
        # -------------- #
        return out