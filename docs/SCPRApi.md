# openapi_client.SCPRApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**train**](SCPRApi.md#train) | **POST** /SCPR | 


# **train**
> str train()



### Example


```python
import time
import openapi_client
from openapi_client.api import scpr_api
from openapi_client.model.training_request import TrainingRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scpr_api.SCPRApi(api_client)
    training_request = TrainingRequest(
        x=[
            [
                3.14,
            ],
        ],
        y=[
            3.14,
        ],
        inputs=[
            "inputs_example",
        ],
        target="target_example",
        algorithm_parameters=SCPRParameters(
            model_type=SCPRModelType(0),
            degree=1,
            alpha=0,
            _lambda=3.14,
            shuffled_restarts=1,
            max_variables_in_interaction=1,
            input_variable_scaling={
                "key": DoubleRange(
                    lower_bound=3.14,
                    upper_bound=3.14,
                ),
            },
            constraints=[
                ShapeConstraint(
                    variable_name="variable_name_example",
                    order_derivative=1,
                    interval=DoubleRange(
                        lower_bound=3.14,
                        upper_bound=3.14,
                    ),
                ),
            ],
            algorithm_version=Version(
                major=1,
                minor=1,
                build=1,
                revision=1,
            ),
            max_sdp_solver_iterations=1,
            positivstellensatz_poly_degree=1,
            min_coeff_value=3.14,
        ),
    ) # TrainingRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.train(training_request=training_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCPRApi->train: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_request** | [**TrainingRequest**](TrainingRequest.md)|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

