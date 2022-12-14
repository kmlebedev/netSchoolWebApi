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

import io.swagger.client.models.StudentDiaryInitStudents

/**
 * 
 * @param students 
 * @param currentStudentId 
 * @param weekStart 
 * @param yaClass 
 * @param yaClassAuthUrl 
 * @param newDiskToken 
 * @param newDiskWasRequest 
 * @param ttsuRl 
 * @param externalUrl 
 * @param weight 
 * @param maxMark 
 * @param withLaAssigns 
 */
data class StudentDiaryInit (

    val students: kotlin.Array<StudentDiaryInitStudents>? = null,
    val currentStudentId: kotlin.Int? = null,
    val weekStart: java.time.LocalDate? = null,
    val yaClass: kotlin.Boolean? = null,
    val yaClassAuthUrl: kotlin.String? = null,
    val newDiskToken: kotlin.String? = null,
    val newDiskWasRequest: kotlin.Boolean? = null,
    val ttsuRl: kotlin.String? = null,
    val externalUrl: kotlin.String? = null,
    val weight: kotlin.Boolean? = null,
    val maxMark: kotlin.Int? = null,
    val withLaAssigns: kotlin.Boolean? = null
) {
}