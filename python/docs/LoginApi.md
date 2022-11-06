# swagger_client.LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getauthdata**](LoginApi.md#getauthdata) | **POST** /auth/getdata | 
[**login**](LoginApi.md#login) | **POST** /login | 
[**logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**loginform**](LoginApi.md#loginform) | **GET** /loginform | 
[**prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

# **getauthdata**
> GetAuthData getauthdata()



returns all login data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()

try:
    api_response = api_instance.getauthdata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->getauthdata: %s\n" % e)
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

# **login**
> Login login(login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver)



returns all login data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
login_type = 56 # int | 
cid = 56 # int | 
sid = 56 # int | 
pid = 56 # int | 
cn = 56 # int | 
sft = 56 # int | 
scid = 56 # int | 
un = 'un_example' # str | 
pw = 'pw_example' # str | 
lt = 56 # int | 
pw2 = 'pw2_example' # str | 
ver = 56 # int | 

try:
    api_response = api_instance.login(login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login: %s\n" % e)
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
 **un** | **str**|  | 
 **pw** | **str**|  | 
 **lt** | **int**|  | 
 **pw2** | **str**|  | 
 **ver** | **int**|  | 

### Return type

[**Login**](Login.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logindata**
> LoginData logindata()



returns all login data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()

try:
    api_response = api_instance.logindata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->logindata: %s\n" % e)
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

# **loginform**
> LoginForm loginform(cid=cid, sid=sid, pid=pid, cn=cn, sft=sft, lastname=lastname, cache_ver=cache_ver)



returns all loginform

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
cid = 56 # int |  (optional)
sid = 56 # int |  (optional)
pid = 56 # int |  (optional)
cn = 56 # int |  (optional)
sft = 56 # int |  (optional)
lastname = 'lastname_example' # str |  (optional)
cache_ver = 'cache_ver_example' # str |  (optional)

try:
    api_response = api_instance.loginform(cid=cid, sid=sid, pid=pid, cn=cn, sft=sft, lastname=lastname, cache_ver=cache_ver)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->loginform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**|  | [optional] 
 **sid** | **int**|  | [optional] 
 **pid** | **int**|  | [optional] 
 **cn** | **int**|  | [optional] 
 **sft** | **int**|  | [optional] 
 **lastname** | **str**|  | [optional] 
 **cache_ver** | **str**|  | [optional] 

### Return type

[**LoginForm**](LoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepareemloginform**
> PrepareEmLoginForm prepareemloginform(cache_ver=cache_ver)



returns all prepareemloginform

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
cache_ver = 'cache_ver_example' # str |  (optional)

try:
    api_response = api_instance.prepareemloginform(cache_ver=cache_ver)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->prepareemloginform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_ver** | **str**|  | [optional] 

### Return type

[**PrepareEmLoginForm**](PrepareEmLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepareloginform**
> PrepareLoginForm prepareloginform(cid=cid, sid=sid, pid=pid, cn=cn, sft=sft, lastname=lastname, cache_ver=cache_ver)



returns all prepareloginform

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
cid = 56 # int |  (optional)
sid = 56 # int |  (optional)
pid = 56 # int |  (optional)
cn = 56 # int |  (optional)
sft = 56 # int |  (optional)
lastname = 'lastname_example' # str |  (optional)
cache_ver = 'cache_ver_example' # str |  (optional)

try:
    api_response = api_instance.prepareloginform(cid=cid, sid=sid, pid=pid, cn=cn, sft=sft, lastname=lastname, cache_ver=cache_ver)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->prepareloginform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**|  | [optional] 
 **sid** | **int**|  | [optional] 
 **pid** | **int**|  | [optional] 
 **cn** | **int**|  | [optional] 
 **sft** | **int**|  | [optional] 
 **lastname** | **str**|  | [optional] 
 **cache_ver** | **str**|  | [optional] 

### Return type

[**PrepareLoginForm**](PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

