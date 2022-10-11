/*
 * NetSchool
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 4.30.43656
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.api;

import io.swagger.client.ApiCallback;
import io.swagger.client.ApiClient;
import io.swagger.client.ApiException;
import io.swagger.client.ApiResponse;
import io.swagger.client.Configuration;
import io.swagger.client.Pair;
import io.swagger.client.ProgressRequestBody;
import io.swagger.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import io.swagger.client.model.Diary;
import org.threeten.bp.LocalDate;
import io.swagger.client.model.StudentDiaryInit;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StudentApi {
    private ApiClient apiClient;

    public StudentApi() {
        this(Configuration.getDefaultApiClient());
    }

    public StudentApi(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for studentDiary
     * @param studentId  (required)
     * @param weekStart  (optional)
     * @param weekEnd  (optional)
     * @param withLaAssigns  (optional)
     * @param withPastMandatory  (optional)
     * @param yearId  (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call studentDiaryCall(Integer studentId, LocalDate weekStart, LocalDate weekEnd, Boolean withLaAssigns, Boolean withPastMandatory, Integer yearId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/student/diary";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (studentId != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("studentId", studentId));
        if (weekStart != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("weekStart", weekStart));
        if (weekEnd != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("weekEnd", weekEnd));
        if (withLaAssigns != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("withLaAssigns", withLaAssigns));
        if (withPastMandatory != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("withPastMandatory", withPastMandatory));
        if (yearId != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("yearId", yearId));

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] {  };
        return apiClient.buildCall(localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call studentDiaryValidateBeforeCall(Integer studentId, LocalDate weekStart, LocalDate weekEnd, Boolean withLaAssigns, Boolean withPastMandatory, Integer yearId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'studentId' is set
        if (studentId == null) {
            throw new ApiException("Missing the required parameter 'studentId' when calling studentDiary(Async)");
        }
        
        com.squareup.okhttp.Call call = studentDiaryCall(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * 
     * returns all assignments
     * @param studentId  (required)
     * @param weekStart  (optional)
     * @param weekEnd  (optional)
     * @param withLaAssigns  (optional)
     * @param withPastMandatory  (optional)
     * @param yearId  (optional)
     * @return Diary
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Diary studentDiary(Integer studentId, LocalDate weekStart, LocalDate weekEnd, Boolean withLaAssigns, Boolean withPastMandatory, Integer yearId) throws ApiException {
        ApiResponse<Diary> resp = studentDiaryWithHttpInfo(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId);
        return resp.getData();
    }

    /**
     * 
     * returns all assignments
     * @param studentId  (required)
     * @param weekStart  (optional)
     * @param weekEnd  (optional)
     * @param withLaAssigns  (optional)
     * @param withPastMandatory  (optional)
     * @param yearId  (optional)
     * @return ApiResponse&lt;Diary&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Diary> studentDiaryWithHttpInfo(Integer studentId, LocalDate weekStart, LocalDate weekEnd, Boolean withLaAssigns, Boolean withPastMandatory, Integer yearId) throws ApiException {
        com.squareup.okhttp.Call call = studentDiaryValidateBeforeCall(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId, null, null);
        Type localVarReturnType = new TypeToken<Diary>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * returns all assignments
     * @param studentId  (required)
     * @param weekStart  (optional)
     * @param weekEnd  (optional)
     * @param withLaAssigns  (optional)
     * @param withPastMandatory  (optional)
     * @param yearId  (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call studentDiaryAsync(Integer studentId, LocalDate weekStart, LocalDate weekEnd, Boolean withLaAssigns, Boolean withPastMandatory, Integer yearId, final ApiCallback<Diary> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = studentDiaryValidateBeforeCall(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<Diary>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
    /**
     * Build call for studentDiaryInit
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call studentDiaryInitCall(final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/student/diary/init";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] {  };
        return apiClient.buildCall(localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call studentDiaryInitValidateBeforeCall(final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        
        com.squareup.okhttp.Call call = studentDiaryInitCall(progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * 
     * returns strudent diary init data
     * @return StudentDiaryInit
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public StudentDiaryInit studentDiaryInit() throws ApiException {
        ApiResponse<StudentDiaryInit> resp = studentDiaryInitWithHttpInfo();
        return resp.getData();
    }

    /**
     * 
     * returns strudent diary init data
     * @return ApiResponse&lt;StudentDiaryInit&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<StudentDiaryInit> studentDiaryInitWithHttpInfo() throws ApiException {
        com.squareup.okhttp.Call call = studentDiaryInitValidateBeforeCall(null, null);
        Type localVarReturnType = new TypeToken<StudentDiaryInit>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * returns strudent diary init data
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call studentDiaryInitAsync(final ApiCallback<StudentDiaryInit> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = studentDiaryInitValidateBeforeCall(progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<StudentDiaryInit>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
}