=begin
#NetSchool

#The API for the NetSchool irTech project

OpenAPI spec version: 4.30.43656

Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 3.0.35
=end

module SwaggerClient
  class DiaryApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # returns assign information
    # @param assign_id 
    # @param student_id 
    # @param [Hash] opts the optional parameters
    # @return [DiaryAssignDetails]
    def diary_assignn_details(assign_id, student_id, opts = {})
      data, _status_code, _headers = diary_assignn_details_with_http_info(assign_id, student_id, opts)
      data
    end

    # returns assign information
    # @param assign_id 
    # @param student_id 
    # @param [Hash] opts the optional parameters
    # @return [Array<(DiaryAssignDetails, Integer, Hash)>] DiaryAssignDetails data, response status code and response headers
    def diary_assignn_details_with_http_info(assign_id, student_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: DiaryApi.diary_assignn_details ...'
      end
      # verify the required parameter 'assign_id' is set
      if @api_client.config.client_side_validation && assign_id.nil?
        fail ArgumentError, "Missing the required parameter 'assign_id' when calling DiaryApi.diary_assignn_details"
      end
      # verify the required parameter 'student_id' is set
      if @api_client.config.client_side_validation && student_id.nil?
        fail ArgumentError, "Missing the required parameter 'student_id' when calling DiaryApi.diary_assignn_details"
      end
      # resource path
      local_var_path = '/student/diary/assigns/{assignId}'.sub('{' + 'assignId' + '}', assign_id.to_s)

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'studentId'] = student_id

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] 

      return_type = opts[:return_type] || 'DiaryAssignDetails' 

      auth_names = opts[:auth_names] || []
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type)

      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DiaryApi#diary_assignn_details\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end