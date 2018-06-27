import gpytorch


class AcquisitionFunction(gpytorch.Module):
    def __init__(self, gp_model):
        super(AcquisitionFunction, self).__init__()
        self.gp_model = gp_model

    def forward(self, candidate_set):
        pass
