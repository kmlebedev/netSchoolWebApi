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
package io.swagger.client.apis

import io.swagger.client.models.AssignmentTypes

import io.swagger.client.infrastructure.*

class AssignmentApi(basePath: kotlin.String = "https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221") : ApiClient(basePath) {

    /**
     * 
     * returns all assignment types
     * @return AssignmentTypes
     */
    @Suppress("UNCHECKED_CAST")
    fun assignmentTypes(): AssignmentTypes {
        
        val localVariableConfig = RequestConfig(
                RequestMethod.GET,
                "/grade/assignment/types"
        )
        val response = request<AssignmentTypes>(
                localVariableConfig
        )

        return when (response.responseType) {
            ResponseType.Success -> (response as Success<*>).data as AssignmentTypes
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
        }
    }
}
