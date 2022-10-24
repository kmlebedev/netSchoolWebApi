=begin
#NetSchool

#The API for the NetSchool irTech project

OpenAPI spec version: 5.10.63221

Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 3.0.35
=end

module SwaggerClient
  class LoginApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # returns all login data
    # @param [Hash] opts the optional parameters
    # @return [GetAuthData]
    def getauthdata(opts = {})
      data, _status_code, _headers = getauthdata_with_http_info(opts)
      data
    end

    # returns all login data
    # @param [Hash] opts the optional parameters
    # @return [Array<(GetAuthData, Integer, Hash)>] GetAuthData data, response status code and response headers
    def getauthdata_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LoginApi.getauthdata ...'
      end
      # resource path
      local_var_path = '/auth/getdata'

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] 

      return_type = opts[:return_type] || 'GetAuthData' 

      auth_names = opts[:auth_names] || []
      data, status_code, headers = @api_client.call_api(:POST, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type)

      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LoginApi#getauthdata\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
    # returns all login data
    # @param login_type 
    # @param cid 
    # @param sid 
    # @param pid 
    # @param cn 
    # @param sft 
    # @param scid 
    # @param un 
    # @param pw 
    # @param lt 
    # @param pw2 
    # @param ver 
    # @param [Hash] opts the optional parameters
    # @return [Login]
    def login(login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver, opts = {})
      data, _status_code, _headers = login_with_http_info(login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver, opts)
      data
    end

    # returns all login data
    # @param login_type 
    # @param cid 
    # @param sid 
    # @param pid 
    # @param cn 
    # @param sft 
    # @param scid 
    # @param un 
    # @param pw 
    # @param lt 
    # @param pw2 
    # @param ver 
    # @param [Hash] opts the optional parameters
    # @return [Array<(Login, Integer, Hash)>] Login data, response status code and response headers
    def login_with_http_info(login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LoginApi.login ...'
      end
      # verify the required parameter 'login_type' is set
      if @api_client.config.client_side_validation && login_type.nil?
        fail ArgumentError, "Missing the required parameter 'login_type' when calling LoginApi.login"
      end
      # verify the required parameter 'cid' is set
      if @api_client.config.client_side_validation && cid.nil?
        fail ArgumentError, "Missing the required parameter 'cid' when calling LoginApi.login"
      end
      # verify the required parameter 'sid' is set
      if @api_client.config.client_side_validation && sid.nil?
        fail ArgumentError, "Missing the required parameter 'sid' when calling LoginApi.login"
      end
      # verify the required parameter 'pid' is set
      if @api_client.config.client_side_validation && pid.nil?
        fail ArgumentError, "Missing the required parameter 'pid' when calling LoginApi.login"
      end
      # verify the required parameter 'cn' is set
      if @api_client.config.client_side_validation && cn.nil?
        fail ArgumentError, "Missing the required parameter 'cn' when calling LoginApi.login"
      end
      # verify the required parameter 'sft' is set
      if @api_client.config.client_side_validation && sft.nil?
        fail ArgumentError, "Missing the required parameter 'sft' when calling LoginApi.login"
      end
      # verify the required parameter 'scid' is set
      if @api_client.config.client_side_validation && scid.nil?
        fail ArgumentError, "Missing the required parameter 'scid' when calling LoginApi.login"
      end
      # verify the required parameter 'un' is set
      if @api_client.config.client_side_validation && un.nil?
        fail ArgumentError, "Missing the required parameter 'un' when calling LoginApi.login"
      end
      # verify the required parameter 'pw' is set
      if @api_client.config.client_side_validation && pw.nil?
        fail ArgumentError, "Missing the required parameter 'pw' when calling LoginApi.login"
      end
      # verify the required parameter 'lt' is set
      if @api_client.config.client_side_validation && lt.nil?
        fail ArgumentError, "Missing the required parameter 'lt' when calling LoginApi.login"
      end
      # verify the required parameter 'pw2' is set
      if @api_client.config.client_side_validation && pw2.nil?
        fail ArgumentError, "Missing the required parameter 'pw2' when calling LoginApi.login"
      end
      # verify the required parameter 'ver' is set
      if @api_client.config.client_side_validation && ver.nil?
        fail ArgumentError, "Missing the required parameter 'ver' when calling LoginApi.login"
      end
      # resource path
      local_var_path = '/login'

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      header_params['Content-Type'] = @api_client.select_header_content_type(['application/x-www-form-urlencoded'])

      # form parameters
      form_params = opts[:form_params] || {}
      form_params['LoginType'] = login_type
      form_params['cid'] = cid
      form_params['sid'] = sid
      form_params['pid'] = pid
      form_params['cn'] = cn
      form_params['sft'] = sft
      form_params['scid'] = scid
      form_params['UN'] = un
      form_params['PW'] = pw
      form_params['lt'] = lt
      form_params['pw2'] = pw2
      form_params['ver'] = ver

      # http body (model)
      post_body = opts[:body] 

      return_type = opts[:return_type] || 'Login' 

      auth_names = opts[:auth_names] || []
      data, status_code, headers = @api_client.call_api(:POST, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type)

      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LoginApi#login\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
    # returns all login data
    # @param [Hash] opts the optional parameters
    # @return [LoginData]
    def logindata(opts = {})
      data, _status_code, _headers = logindata_with_http_info(opts)
      data
    end

    # returns all login data
    # @param [Hash] opts the optional parameters
    # @return [Array<(LoginData, Integer, Hash)>] LoginData data, response status code and response headers
    def logindata_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LoginApi.logindata ...'
      end
      # resource path
      local_var_path = '/logindata'

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] 

      return_type = opts[:return_type] || 'LoginData' 

      auth_names = opts[:auth_names] || []
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type)

      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LoginApi#logindata\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
    # returns all prepareemloginform
    # @param [Hash] opts the optional parameters
    # @option opts [String] :cache_ver 
    # @return [PrepareEmLoginForm]
    def prepareemloginform(opts = {})
      data, _status_code, _headers = prepareemloginform_with_http_info(opts)
      data
    end

    # returns all prepareemloginform
    # @param [Hash] opts the optional parameters
    # @option opts [String] :cache_ver 
    # @return [Array<(PrepareEmLoginForm, Integer, Hash)>] PrepareEmLoginForm data, response status code and response headers
    def prepareemloginform_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LoginApi.prepareemloginform ...'
      end
      # resource path
      local_var_path = '/prepareemloginform'

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'cacheVer'] = opts[:'cache_ver'] if !opts[:'cache_ver'].nil?

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] 

      return_type = opts[:return_type] || 'PrepareEmLoginForm' 

      auth_names = opts[:auth_names] || []
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type)

      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LoginApi#prepareemloginform\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
    # returns all prepareloginform
    # @param [Hash] opts the optional parameters
    # @option opts [String] :cache_ver 
    # @return [PrepareLoginForm]
    def prepareloginform(opts = {})
      data, _status_code, _headers = prepareloginform_with_http_info(opts)
      data
    end

    # returns all prepareloginform
    # @param [Hash] opts the optional parameters
    # @option opts [String] :cache_ver 
    # @return [Array<(PrepareLoginForm, Integer, Hash)>] PrepareLoginForm data, response status code and response headers
    def prepareloginform_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LoginApi.prepareloginform ...'
      end
      # resource path
      local_var_path = '/prepareloginform'

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'cacheVer'] = opts[:'cache_ver'] if !opts[:'cache_ver'].nil?

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] 

      return_type = opts[:return_type] || 'PrepareLoginForm' 

      auth_names = opts[:auth_names] || []
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type)

      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LoginApi#prepareloginform\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
