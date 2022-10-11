# Swagger\Client\DiaryApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diaryAssignnDetails**](DiaryApi.md#diaryassignndetails) | **GET** /student/diary/assigns/{assignId} | 

# **diaryAssignnDetails**
> \Swagger\Client\Model\DiaryAssignDetails diaryAssignnDetails($assign_id, $student_id)



returns assign information

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\DiaryApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$assign_id = 56; // int | 
$student_id = 56; // int | 

try {
    $result = $apiInstance->diaryAssignnDetails($assign_id, $student_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DiaryApi->diaryAssignnDetails: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_id** | **int**|  |
 **student_id** | **int**|  |

### Return type

[**\Swagger\Client\Model\DiaryAssignDetails**](../Model/DiaryAssignDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

