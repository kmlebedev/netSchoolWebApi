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
import {AssignmentTypes} from '../model/AssignmentTypes';

/**
* Assignment service.
* @module api/AssignmentApi
* @version 5.10.63221
*/
export class AssignmentApi {

    /**
    * Constructs a new AssignmentApi. 
    * @alias module:api/AssignmentApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instanc
    e} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }

    /**
     * Callback function to receive the result of the assignmentTypes operation.
     * @callback moduleapi/AssignmentApi~assignmentTypesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AssignmentTypes{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * returns all assignment types
     * @param {module:api/AssignmentApi~assignmentTypesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    assignmentTypes(callback) {
      
      let postBody = null;

      let pathParams = {
        
      };
      let queryParams = {
        
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = ['bearerAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AssignmentTypes;

      return this.apiClient.callApi(
        '/grade/assignment/types', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

}