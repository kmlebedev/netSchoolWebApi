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

import io.swagger.client.models.LoginAccountInfoUserRolesRole

/**
 * 
 * @param userId 
 * @param schoolId 
 * @param role 
 */
data class LoginAccountInfoUserRoles (

    val userId: kotlin.Int? = null,
    val schoolId: kotlin.Int? = null,
    val role: LoginAccountInfoUserRolesRole? = null
) {
}