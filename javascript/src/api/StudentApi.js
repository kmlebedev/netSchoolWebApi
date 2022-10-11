/*
 * NetSchool
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 4.30.43656
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
import {Diary} from '../model/Diary';
import {StudentDiaryInit} from '../model/StudentDiaryInit';

/**
* Student service.
* @module api/StudentApi
* @version 4.30.43656
*/
export class StudentApi {

    /**
    * Constructs a new StudentApi. 
    * @alias module:api/StudentApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instanc
    e} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }

    /**
     * Callback function to receive the result of the studentDiary operation.
     * @callback moduleapi/StudentApi~studentDiaryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Diary{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * returns all assignments
     * @param {Number} studentId 
     * @param {Object} opts Optional parameters
     * @param {Date} opts.weekStart 
     * @param {Date} opts.weekEnd 
     * @param {Boolean} opts.withLaAssigns 
     * @param {Boolean} opts.withPastMandatory 
     * @param {Number} opts.yearId 
     * @param {module:api/StudentApi~studentDiaryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    studentDiary(studentId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'studentId' is set
      if (studentId === undefined || studentId === null) {
        throw new Error("Missing the required parameter 'studentId' when calling studentDiary");
      }

      let pathParams = {
        
      };
      let queryParams = {
        'studentId': studentId,'weekStart': opts['weekStart'],'weekEnd': opts['weekEnd'],'withLaAssigns': opts['withLaAssigns'],'withPastMandatory': opts['withPastMandatory'],'yearId': opts['yearId']
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Diary;

      return this.apiClient.callApi(
        '/student/diary', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
    /**
     * Callback function to receive the result of the studentDiaryInit operation.
     * @callback moduleapi/StudentApi~studentDiaryInitCallback
     * @param {String} error Error message, if any.
     * @param {module:model/StudentDiaryInit{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * returns strudent diary init data
     * @param {module:api/StudentApi~studentDiaryInitCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    studentDiaryInit(callback) {
      
      let postBody = null;

      let pathParams = {
        
      };
      let queryParams = {
        
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = StudentDiaryInit;

      return this.apiClient.callApi(
        '/student/diary/init', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

}