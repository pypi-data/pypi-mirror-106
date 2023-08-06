from msys.registration import get_registered


def get_optimizers():
    return get_registered("msys_opt.optimizers")