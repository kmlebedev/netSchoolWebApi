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
import {DiaryAssignment} from './DiaryAssignment';

/**
 * The DiaryLesson model module.
 * @module model/DiaryLesson
 * @version 5.10.63221
 */
export class DiaryLesson {
  /**
   * Constructs a new <code>DiaryLesson</code>.
   * @alias module:model/DiaryLesson
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>DiaryLesson</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/DiaryLesson} obj Optional instance to populate.
   * @return {module:model/DiaryLesson} The populated <code>DiaryLesson</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new DiaryLesson();
      if (data.hasOwnProperty('classmeetingId'))
        obj.classmeetingId = ApiClient.convertToType(data['classmeetingId'], 'String');
      if (data.hasOwnProperty('day'))
        obj.day = ApiClient.convertToType(data['day'], 'Date');
      if (data.hasOwnProperty('number'))
        obj._number = ApiClient.convertToType(data['number'], 'Number');
      if (data.hasOwnProperty('room'))
        obj.room = ApiClient.convertToType(data['room'], 'String');
      if (data.hasOwnProperty('startTime'))
        obj.startTime = ApiClient.convertToType(data['startTime'], 'String');
      if (data.hasOwnProperty('endTime'))
        obj.endTime = ApiClient.convertToType(data['endTime'], 'String');
      if (data.hasOwnProperty('subjectName'))
        obj.subjectName = ApiClient.convertToType(data['subjectName'], 'String');
      if (data.hasOwnProperty('assignments'))
        obj.assignments = ApiClient.convertToType(data['assignments'], [DiaryAssignment]);
    }
    return obj;
  }
}

/**
 * @member {String} classmeetingId
 */
DiaryLesson.prototype.classmeetingId = undefined;

/**
 * @member {Date} day
 */
DiaryLesson.prototype.day = undefined;

/**
 * @member {Number} _number
 */
DiaryLesson.prototype._number = undefined;

/**
 * @member {String} room
 */
DiaryLesson.prototype.room = undefined;

/**
 * @member {String} startTime
 */
DiaryLesson.prototype.startTime = undefined;

/**
 * @member {String} endTime
 */
DiaryLesson.prototype.endTime = undefined;

/**
 * @member {String} subjectName
 */
DiaryLesson.prototype.subjectName = undefined;

/**
 * @member {Array.<module:model/DiaryAssignment>} assignments
 */
DiaryLesson.prototype.assignments = undefined;

