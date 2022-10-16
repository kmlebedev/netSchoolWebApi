# IO.Swagger.Api.AssignmentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AssignmentTypes**](AssignmentApi.md#assignmenttypes) | **GET** /grade/assignment/types | 

<a name="assignmenttypes"></a>
# **AssignmentTypes**
> AssignmentTypes AssignmentTypes ()



returns all assignment types

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class AssignmentTypesExample
    {
        public void main()
        {

            var apiInstance = new AssignmentApi();

            try
            {
                AssignmentTypes result = apiInstance.AssignmentTypes();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AssignmentApi.AssignmentTypes: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssignmentTypes**](AssignmentTypes.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
