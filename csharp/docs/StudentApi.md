# IO.Swagger.Api.StudentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**StudentDiary**](StudentApi.md#studentdiary) | **GET** /student/diary | 
[**StudentDiaryInit**](StudentApi.md#studentdiaryinit) | **GET** /student/diary/init | 

<a name="studentdiary"></a>
# **StudentDiary**
> Diary StudentDiary (int? studentId, DateTime? weekStart = null, DateTime? weekEnd = null, bool? withLaAssigns = null, bool? withPastMandatory = null, int? yearId = null)



returns all assignments

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class StudentDiaryExample
    {
        public void main()
        {
            var apiInstance = new StudentApi();
            var studentId = 56;  // int? | 
            var weekStart = 2013-10-20;  // DateTime? |  (optional) 
            var weekEnd = 2013-10-20;  // DateTime? |  (optional) 
            var withLaAssigns = true;  // bool? |  (optional) 
            var withPastMandatory = true;  // bool? |  (optional) 
            var yearId = 56;  // int? |  (optional) 

            try
            {
                Diary result = apiInstance.StudentDiary(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling StudentApi.StudentDiary: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **int?**|  | 
 **weekStart** | **DateTime?**|  | [optional] 
 **weekEnd** | **DateTime?**|  | [optional] 
 **withLaAssigns** | **bool?**|  | [optional] 
 **withPastMandatory** | **bool?**|  | [optional] 
 **yearId** | **int?**|  | [optional] 

### Return type

[**Diary**](Diary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="studentdiaryinit"></a>
# **StudentDiaryInit**
> StudentDiaryInit StudentDiaryInit ()



returns strudent diary init data

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class StudentDiaryInitExample
    {
        public void main()
        {
            var apiInstance = new StudentApi();

            try
            {
                StudentDiaryInit result = apiInstance.StudentDiaryInit();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling StudentApi.StudentDiaryInit: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StudentDiaryInit**](StudentDiaryInit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
