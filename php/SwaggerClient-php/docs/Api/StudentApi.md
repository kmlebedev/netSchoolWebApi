# Swagger\Client\StudentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studentDiary**](StudentApi.md#studentdiary) | **GET** /student/diary | 
[**studentDiaryInit**](StudentApi.md#studentdiaryinit) | **GET** /student/diary/init | 

# **studentDiary**
> \Swagger\Client\Model\Diary studentDiary($student_id, $week_start, $week_end, $with_la_assigns, $with_past_mandatory, $year_id)



returns all assignments

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\StudentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$student_id = 56; // int | 
$week_start = new \DateTime("2013-10-20"); // \DateTime | 
$week_end = new \DateTime("2013-10-20"); // \DateTime | 
$with_la_assigns = true; // bool | 
$with_past_mandatory = true; // bool | 
$year_id = 56; // int | 

try {
    $result = $apiInstance->studentDiary($student_id, $week_start, $week_end, $with_la_assigns, $with_past_mandatory, $year_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StudentApi->studentDiary: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student_id** | **int**|  |
 **week_start** | **\DateTime**|  | [optional]
 **week_end** | **\DateTime**|  | [optional]
 **with_la_assigns** | **bool**|  | [optional]
 **with_past_mandatory** | **bool**|  | [optional]
 **year_id** | **int**|  | [optional]

### Return type

[**\Swagger\Client\Model\Diary**](../Model/Diary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **studentDiaryInit**
> \Swagger\Client\Model\StudentDiaryInit studentDiaryInit()



returns strudent diary init data

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\StudentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->studentDiaryInit();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StudentApi->studentDiaryInit: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\StudentDiaryInit**](../Model/StudentDiaryInit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

