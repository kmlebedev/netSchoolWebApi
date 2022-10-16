# IO.Swagger.Api.DiaryApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DiaryAssignnDetails**](DiaryApi.md#diaryassignndetails) | **GET** /student/diary/assigns/{assignId} | 

<a name="diaryassignndetails"></a>
# **DiaryAssignnDetails**
> DiaryAssignDetails DiaryAssignnDetails (int? assignId, int? studentId)



returns assign information

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class DiaryAssignnDetailsExample
    {
        public void main()
        {

            var apiInstance = new DiaryApi();
            var assignId = 56;  // int? | 
            var studentId = 56;  // int? | 

            try
            {
                DiaryAssignDetails result = apiInstance.DiaryAssignnDetails(assignId, studentId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DiaryApi.DiaryAssignnDetails: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignId** | **int?**|  | 
 **studentId** | **int?**|  | 

### Return type

[**DiaryAssignDetails**](DiaryAssignDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
