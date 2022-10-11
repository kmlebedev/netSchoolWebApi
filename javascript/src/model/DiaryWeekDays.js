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
import {ApiClient} from '../ApiClient';
import {DiaryLesson} from './DiaryLesson';

/**
 * The DiaryWeekDays model module.
 * @module model/DiaryWeekDays
 * @version 4.30.43656
 */
export class DiaryWeekDays {
  /**
   * Constructs a new <code>DiaryWeekDays</code>.
   * @alias module:model/DiaryWeekDays
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>DiaryWeekDays</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/DiaryWeekDays} obj Optional instance to populate.
   * @return {module:model/DiaryWeekDays} The populated <code>DiaryWeekDays</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new DiaryWeekDays();
      if (data.hasOwnProperty('date'))
        obj._date = ApiClient.convertToType(data['date'], 'Date');
      if (data.hasOwnProperty('lessons'))
        obj.lessons = ApiClient.convertToType(data['lessons'], [DiaryLesson]);
    }
    return obj;
  }
}

/**
 * @member {Date} _date
 */
DiaryWeekDays.prototype._date = undefined;

/**
 * @member {Array.<module:model/DiaryLesson>} lessons
 */
DiaryWeekDays.prototype.lessons = undefined;
