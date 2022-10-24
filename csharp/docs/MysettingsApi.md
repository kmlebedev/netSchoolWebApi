# IO.Swagger.Api.MysettingsApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Mysettings**](MysettingsApi.md#mysettings) | **GET** /mysettings | 
[**Yearlist**](MysettingsApi.md#yearlist) | **GET** /mysettings/yearlist | 

<a name="mysettings"></a>
# **Mysettings**
> MySettings Mysettings (string at)



returns my settings

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class MysettingsExample
    {
        public void main()
        {

            var apiInstance = new MysettingsApi();
            var at = at_example;  // string | an authorization header

            try
            {
                MySettings result = apiInstance.Mysettings(at);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling MysettingsApi.Mysettings: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **string**| an authorization header | 

### Return type

[**MySettings**](MySettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="yearlist"></a>
# **Yearlist**
> MySettingsYears Yearlist (string at)



returns all years

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class YearlistExample
    {
        public void main()
        {

            var apiInstance = new MysettingsApi();
            var at = at_example;  // string | an authorization header

            try
            {
                MySettingsYears result = apiInstance.Yearlist(at);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling MysettingsApi.Yearlist: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **string**| an authorization header | 

### Return type

[**MySettingsYears**](MySettingsYears.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
