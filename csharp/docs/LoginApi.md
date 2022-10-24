# IO.Swagger.Api.LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Getauthdata**](LoginApi.md#getauthdata) | **POST** /auth/getdata | 
[**Login**](LoginApi.md#login) | **POST** /login | 
[**Logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**Prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**Prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

<a name="getauthdata"></a>
# **Getauthdata**
> GetAuthData Getauthdata ()



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
    public class GetauthdataExample
    {
        public void main()
        {
            var apiInstance = new LoginApi();

            try
            {
                GetAuthData result = apiInstance.Getauthdata();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling LoginApi.Getauthdata: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAuthData**](GetAuthData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="login"></a>
# **Login**
> Login Login (int? loginType, int? cid, int? sid, int? pid, int? cn, int? sft, int? scid, string UN, string PW, int? lt, string pw2, int? ver)



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
    public class LoginExample
    {
        public void main()
        {
            var apiInstance = new LoginApi();
            var loginType = 56;  // int? | 
            var cid = 56;  // int? | 
            var sid = 56;  // int? | 
            var pid = 56;  // int? | 
            var cn = 56;  // int? | 
            var sft = 56;  // int? | 
            var scid = 56;  // int? | 
            var UN = UN_example;  // string | 
            var PW = PW_example;  // string | 
            var lt = 56;  // int? | 
            var pw2 = pw2_example;  // string | 
            var ver = 56;  // int? | 

            try
            {
                Login result = apiInstance.Login(loginType, cid, sid, pid, cn, sft, scid, UN, PW, lt, pw2, ver);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling LoginApi.Login: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loginType** | **int?**|  | 
 **cid** | **int?**|  | 
 **sid** | **int?**|  | 
 **pid** | **int?**|  | 
 **cn** | **int?**|  | 
 **sft** | **int?**|  | 
 **scid** | **int?**|  | 
 **UN** | **string**|  | 
 **PW** | **string**|  | 
 **lt** | **int?**|  | 
 **pw2** | **string**|  | 
 **ver** | **int?**|  | 

### Return type

[**Login**](Login.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
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
