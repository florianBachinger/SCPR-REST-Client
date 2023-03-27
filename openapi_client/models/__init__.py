# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.double_range import DoubleRange
from openapi_client.model.scpr_model_type import SCPRModelType
from openapi_client.model.scpr_parameters import SCPRParameters
from openapi_client.model.shape_constraint import ShapeConstraint
from openapi_client.model.training_request import TrainingRequest
from openapi_client.model.version import Version
