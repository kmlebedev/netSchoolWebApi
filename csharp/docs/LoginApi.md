# IO.Swagger.Api.LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**Prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**Prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

<a name="logindata"></a>
# **Logindata**
> LoginData Logindata ()



returns all login data

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class LogindataExample
    {
        public void main()
        {
            var apiInstance = new LoginApi();

            try
            {
                LoginData result = apiInstance.Logindata();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling LoginApi.Logindata: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginData**](LoginData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="prepareemloginform"></a>
# **Prepareemloginform**
> PrepareEmLoginForm Prepareemloginform (string cacheVer = null)



returns all prepareemloginform

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PrepareemloginformExample
    {
        public void main()
        {
            var apiInstance = new LoginApi();
            var cacheVer = cacheVer_example;  // string |  (optional) 

            try
            {
                PrepareEmLoginForm result = apiInstance.Prepareemloginform(cacheVer);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling LoginApi.Prepareemloginform: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cacheVer** | **string**|  | [optional] 

### Return type

[**PrepareEmLoginForm**](PrepareEmLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="prepareloginform"></a>
# **Prepareloginform**
> PrepareLoginForm Prepareloginform (string cacheVer = null)



returns all prepareloginform

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PrepareloginformExample
    {
        public void main()
        {
            var apiInstance = new LoginApi();
            var cacheVer = cacheVer_example;  // string |  (optional) 

            try
            {
                PrepareLoginForm result = apiInstance.Prepareloginform(cacheVer);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling LoginApi.Prepareloginform: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cacheVer** | **string**|  | [optional] 

### Return type

[**PrepareLoginForm**](PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
