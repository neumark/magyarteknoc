from .turtle import RenderBackend as turtle_backend
try:
    from .mc import RenderBackend as mc_backend
except ModuleNotFoundError:
    # fall back to using turtle_backend
    mc_backend = turtle_backend


