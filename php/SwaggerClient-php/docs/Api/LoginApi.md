# Swagger\Client\LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

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

