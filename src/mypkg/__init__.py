# read version from installed package
from importlib.metadata import version
__version__ = version("mypkg")

# populate package namespace (para tener count_words... en el directorio de namespaces de mypkg al hacer import mypkg)
from mypkg.mypkg import count_words
from mypkg.plotting import plot_words
from mypkg.datasets import get_flatland