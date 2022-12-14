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
import {Attachment} from './Attachment';
import {Mark} from './Mark';

/**
 * The DiaryAssignment model module.
 * @module model/DiaryAssignment
 * @version 5.10.63221
 */
export class DiaryAssignment {
  /**
   * Constructs a new <code>DiaryAssignment</code>.
   * @alias module:model/DiaryAssignment
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>DiaryAssignment</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/DiaryAssignment} obj Optional instance to populate.
   * @return {module:model/DiaryAssignment} The populated <code>DiaryAssignment</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new DiaryAssignment();
      if (data.hasOwnProperty('mark'))
        obj.mark = Mark.constructFromObject(data['mark']);
      if (data.hasOwnProperty('attachments'))
        obj.attachments = ApiClient.convertToType(data['attachments'], [Attachment]);
      if (data.hasOwnProperty('id'))
        obj.id = ApiClient.convertToType(data['id'], 'Number');
      if (data.hasOwnProperty('typeId'))
        obj.typeId = ApiClient.convertToType(data['typeId'], 'Number');
      if (data.hasOwnProperty('assignmentName'))
        obj.assignmentName = ApiClient.convertToType(data['assignmentName'], 'String');
      if (data.hasOwnProperty('weight'))
        obj.weight = ApiClient.convertToType(data['weight'], 'Number');
      if (data.hasOwnProperty('dueDate'))
        obj.dueDate = ApiClient.convertToType(data['dueDate'], 'Date');
      if (data.hasOwnProperty('classMeetingId'))
        obj.classMeetingId = ApiClient.convertToType(data['classMeetingId'], 'Number');
      if (data.hasOwnProperty('existsTestPlan'))
        obj.existsTestPlan = ApiClient.convertToType(data['existsTestPlan'], 'Boolean');
    }
    return obj;
  }
}

/**
 * @member {module:model/Mark} mark
 */
DiaryAssignment.prototype.mark = undefined;

/**
 * @member {Array.<module:model/Attachment>} attachments
 */
DiaryAssignment.prototype.attachments = undefined;

/**
 * @member {Number} id
 */
DiaryAssignment.prototype.id = undefined;

/**
 * @member {Number} typeId
 */
DiaryAssignment.prototype.typeId = undefined;

/**
 * @member {String} assignmentName
 */
DiaryAssignment.prototype.assignmentName = undefined;

/**
 * @member {Number} weight
 */
DiaryAssignment.prototype.weight = undefined;

/**
 * @member {Date} dueDate
 */
DiaryAssignment.prototype.dueDate = undefined;

/**
 * @member {Number} classMeetingId
 */
DiaryAssignment.prototype.classMeetingId = undefined;

/**
 * @member {Boolean} existsTestPlan
 */
DiaryAssignment.prototype.existsTestPlan = undefined;

