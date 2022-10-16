# Swagger\Client\LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getauthdata**](LoginApi.md#getauthdata) | **GET** /auth/getdata | 
[**login**](LoginApi.md#login) | **POST** /login | 
[**logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

# **getauthdata**
> \Swagger\Client\Model\InlineResponse2001 getauthdata()



returns all login data

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\LoginApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->getauthdata();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LoginApi->getauthdata: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\InlineResponse2001**](../Model/InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **login**
> \Swagger\Client\Model\Login login($login_type, $cid, $sid, $pid, $cn, $sft, $scid, $un, $pw, $lt, $pw2, $ver)



returns all login data

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\LoginApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$login_type = 56; // int | 
$cid = 56; // int | 
$sid = 56; // int | 
$pid = 56; // int | 
$cn = 56; // int | 
$sft = 56; // int | 
$scid = 56; // int | 
$un = "un_example"; // string | 
$pw = "pw_example"; // string | 
$lt = 56; // int | 
$pw2 = "pw2_example"; // string | 
$ver = 56; // int | 

try {
    $result = $apiInstance->login($login_type, $cid, $sid, $pid, $cn, $sft, $scid, $un, $pw, $lt, $pw2, $ver);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LoginApi->login: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_type** | **int**|  |
 **cid** | **int**|  |
 **sid** | **int**|  |
 **pid** | **int**|  |
 **cn** | **int**|  |
 **sft** | **int**|  |
 **scid** | **int**|  |
 **un** | **string**|  |
 **pw** | **string**|  |
 **lt** | **int**|  |
 **pw2** | **string**|  |
 **ver** | **int**|  |

### Return type

[**\Swagger\Client\Model\Login**](../Model/Login.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **logindata**
> \Swagger\Client\Model\LoginData logindata()



returns all login data

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\LoginApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->logindata();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LoginApi->logindata: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\LoginData**](../Model/LoginData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **prepareemloginform**
> \Swagger\Client\Model\PrepareEmLoginForm prepareemloginform($cache_ver)



returns all prepareemloginform

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\LoginApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$cache_ver = "cache_ver_example"; // string | 

try {
    $result = $apiInstance->prepareemloginform($cache_ver);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LoginApi->prepareemloginform: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_ver** | **string**|  | [optional]

### Return type

[**\Swagger\Client\Model\PrepareEmLoginForm**](../Model/PrepareEmLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **prepareloginform**
> \Swagger\Client\Model\PrepareLoginForm prepareloginform($cache_ver)



returns all prepareloginform

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\LoginApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$cache_ver = "cache_ver_example"; // string | 

try {
    $result = $apiInstance->prepareloginform($cache_ver);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LoginApi->prepareloginform: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_ver** | **string**|  | [optional]

### Return type

[**\Swagger\Client\Model\PrepareLoginForm**](../Model/PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

