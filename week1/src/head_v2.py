import torch


class HeadVer2:
    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        """
        :param x: (B, T, C)
        :return: out (B, T, C)
        """
        # --- TODO 3 --- #
        # vectorize HeadVer1.__call__()
        wei = torch.tril(torch.ones(x.shape[1], x.shape[1]))
        wei = wei / wei.sum(1, keepdim=True)
        out = wei @ x
        # ------------ #
        return out
