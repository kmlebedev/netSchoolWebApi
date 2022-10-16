# NetSchool.AssignmentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignmentTypes**](AssignmentApi.md#assignmentTypes) | **GET** /grade/assignment/types | 

<a name="assignmentTypes"></a>
# **assignmentTypes**
> AssignmentTypes assignmentTypes()



returns all assignment types

### Example
```javascript
import {NetSchool} from 'net_school';
let defaultClient = NetSchool.ApiClient.instance;


let apiInstance = new NetSchool.AssignmentApi();
apiInstance.assignmentTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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

