/**
 * NetSchool
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 5.10.63221
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
package io.swagger.client.model


/**
 * @param weekStart 
 * @param weekEnd 
 * @param weekDays 
 * @param termName 
 * @param className 
 */
case class Diary (
  weekStart: Option[String] = None,
  weekEnd: Option[String] = None,
  weekDays: Option[List[DiaryWeekDays]] = None,
  termName: Option[String] = None,
  className: Option[String] = None
)

