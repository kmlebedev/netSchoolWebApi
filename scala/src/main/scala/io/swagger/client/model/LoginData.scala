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
 * @param productName 
 * @param version 
 * @param schoolLogin 
 * @param emLogin 
 * @param esiaLogin 
 * @param esiaLoginPage 
 * @param esiaMainAuth 
 * @param esiaButton 
 * @param signatureLogin 
 * @param cacheVer 
 * @param windowsAuth 
 * @param enableSms 
 * @param esaLogin 
 * @param esaLoginPage 
 */
case class LoginData (
  productName: Option[String] = None,
  version: Option[String] = None,
  schoolLogin: Option[Boolean] = None,
  emLogin: Option[Boolean] = None,
  esiaLogin: Option[Boolean] = None,
  esiaLoginPage: Option[String] = None,
  esiaMainAuth: Option[Boolean] = None,
  esiaButton: Option[Boolean] = None,
  signatureLogin: Option[Boolean] = None,
  cacheVer: Option[String] = None,
  windowsAuth: Option[Boolean] = None,
  enableSms: Option[Boolean] = None,
  esaLogin: Option[Boolean] = None,
  esaLoginPage: Option[String] = None
)

