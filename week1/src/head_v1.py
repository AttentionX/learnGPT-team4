import torch


class HeadVer1:
    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        """
        :param x (B, T, C)
        :return: out (B, T, C)
        """
        B, T, C = x.shape
        # --- TODO 2 --- #
        # use nested for loops to take an average of the past into account
        out = torch.zeros((B,T,C))
        for b in range(B):
            for t in range(T):
                prev = x[b,:t+1]
                out[b,t] = torch.mean(prev, dim=0)
        # -------------- #
        return out
