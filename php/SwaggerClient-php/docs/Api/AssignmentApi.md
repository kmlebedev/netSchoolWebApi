# Swagger\Client\AssignmentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignmentTypes**](AssignmentApi.md#assignmenttypes) | **GET** /grade/assignment/types | 

# **assignmentTypes**
> \Swagger\Client\Model\AssignmentTypes assignmentTypes()



returns all assignment types

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\AssignmentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->assignmentTypes();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AssignmentApi->assignmentTypes: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\AssignmentTypes**](../Model/AssignmentTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

