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
 * @param classmeetingId 
 * @param day 
 * @param number 
 * @param room 
 * @param startTime 
 * @param endTime 
 * @param subjectName 
 * @param assignments 
 */
case class DiaryLesson (
  classmeetingId: Option[String] = None,
  day: Option[date] = None,
  number: Option[Integer] = None,
  room: Option[String] = None,
  startTime: Option[String] = None,
  endTime: Option[String] = None,
  subjectName: Option[String] = None,
  assignments: Option[List[DiaryAssignment]] = None
)

