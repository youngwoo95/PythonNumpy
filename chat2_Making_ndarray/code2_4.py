import numpy as np
import torch

math_score = np.array([80,90])
phy_score = np.array(90)
chem_score = np.array(100)

print(f"{type(math_score) = }\t {math_score.ndim = }\t {math_score.shape = }")
print(f"{type(phy_score) = }\t {phy_score.ndim = }\t {phy_score.shape = }")
print(f"{type(chem_score) = }\t {chem_score.ndim = }\t {chem_score.shape = }")

torch_math_score = torch.tensor([80,90])
print(f"{torch_math_score.shape =}")