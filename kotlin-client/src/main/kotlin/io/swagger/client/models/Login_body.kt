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
package io.swagger.client.models


/**
 * 
 * @param loginType 
 * @param cid 
 * @param sid 
 * @param pid 
 * @param cn 
 * @param sft 
 * @param scid 
 * @param uN 
 * @param pW 
 * @param lt 
 * @param pw2 
 * @param ver 
 */
data class LoginBody (

    val loginType: kotlin.Int? = null,
    val cid: kotlin.Int? = null,
    val sid: kotlin.Int? = null,
    val pid: kotlin.Int? = null,
    val cn: kotlin.Int? = null,
    val sft: kotlin.Int? = null,
    val scid: kotlin.Int? = null,
    val uN: kotlin.String? = null,
    val pW: kotlin.String? = null,
    val lt: kotlin.Int? = null,
    val pw2: kotlin.String? = null,
    val ver: kotlin.Int? = null
) {
}