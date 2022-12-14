/*
 * NetSchool
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 5.10.63221
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.35
 *
 * Do not edit the class manually.
 *
 */
import {ApiClient} from "../ApiClient";
import {DiaryAssignDetails} from '../model/DiaryAssignDetails';

/**
* Diary service.
* @module api/DiaryApi
* @version 5.10.63221
*/
export class DiaryApi {

    /**
    * Constructs a new DiaryApi. 
    * @alias module:api/DiaryApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instanc
    e} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }

    /**
     * Callback function to receive the result of the diaryAssignnDetails operation.
     * @callback moduleapi/DiaryApi~diaryAssignnDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DiaryAssignDetails{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * returns assign information
     * @param {Number} assignId 
     * @param {Number} studentId 
     * @param {module:api/DiaryApi~diaryAssignnDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    diaryAssignnDetails(assignId, studentId, callback) {
      
      let postBody = null;
      // verify the required parameter 'assignId' is set
      if (assignId === undefined || assignId === null) {
        throw new Error("Missing the required parameter 'assignId' when calling diaryAssignnDetails");
      }
      // verify the required parameter 'studentId' is set
      if (studentId === undefined || studentId === null) {
        throw new Error("Missing the required parameter 'studentId' when calling diaryAssignnDetails");
      }

      let pathParams = {
        'assignId': assignId
      };
      let queryParams = {
        'studentId': studentId
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = ['bearerAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DiaryAssignDetails;

      return this.apiClient.callApi(
        '/student/diary/assigns/{assignId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

}