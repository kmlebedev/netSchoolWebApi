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
import {ApiClient} from '../ApiClient';

/**
 * The PrepareEmLoginFormCountries model module.
 * @module model/PrepareEmLoginFormCountries
 * @version 5.10.63221
 */
export class PrepareEmLoginFormCountries {
  /**
   * Constructs a new <code>PrepareEmLoginFormCountries</code>.
   * @alias module:model/PrepareEmLoginFormCountries
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>PrepareEmLoginFormCountries</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/PrepareEmLoginFormCountries} obj Optional instance to populate.
   * @return {module:model/PrepareEmLoginFormCountries} The populated <code>PrepareEmLoginFormCountries</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new PrepareEmLoginFormCountries();
      if (data.hasOwnProperty('id'))
        obj.id = ApiClient.convertToType(data['id'], 'Number');
      if (data.hasOwnProperty('name'))
        obj.name = ApiClient.convertToType(data['name'], 'String');
    }
    return obj;
  }
}

/**
 * @member {Number} id
 */
PrepareEmLoginFormCountries.prototype.id = undefined;

/**
 * @member {String} name
 */
PrepareEmLoginFormCountries.prototype.name = undefined;

