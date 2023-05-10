import warming_model
from warming_model import plan_b
import matplotlib.pyplot as plt

params = warming_model.params_enzyme_default

df = warming_model.plan_b.temperature_regulating(params, warming_model.temp)