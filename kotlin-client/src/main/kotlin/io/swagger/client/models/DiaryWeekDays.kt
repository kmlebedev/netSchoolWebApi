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

import io.swagger.client.models.DiaryLesson

/**
 * 
 * @param date 
 * @param lessons 
 */
data class DiaryWeekDays (

    val date: java.time.LocalDate? = null,
    val lessons: kotlin.Array<DiaryLesson>? = null
) {
}