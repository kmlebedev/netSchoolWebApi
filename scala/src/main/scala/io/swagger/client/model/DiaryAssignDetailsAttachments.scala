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
 * @param id  for example: '''1111'''
 * @param name  for example: '''Дз 5К.doc'''
 * @param originalFileName  for example: '''Дз 5К.doc'''
 * @param description  for example: '''nil'''
 */
case class DiaryAssignDetailsAttachments (
  id: Option[Integer] = None,
  name: Option[String] = None,
  originalFileName: Option[String] = None,
  description: Option[String] = None
)

