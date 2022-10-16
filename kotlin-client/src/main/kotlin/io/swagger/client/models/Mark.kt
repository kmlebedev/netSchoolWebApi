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
 * @param assignmentId 
 * @param studentId 
 * @param mark 
 * @param dutyMark 
 */
data class Mark (

    val assignmentId: kotlin.Int? = null,
    val studentId: kotlin.Int? = null,
    val mark: kotlin.Int? = null,
    val dutyMark: kotlin.Boolean? = null
) {
}