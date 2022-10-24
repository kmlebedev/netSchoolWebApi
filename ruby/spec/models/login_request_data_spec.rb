=begin
#NetSchool

#The API for the NetSchool irTech project

OpenAPI spec version: 5.10.63221

Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 3.0.35
=end

require 'spec_helper'
require 'json'
require 'date'

# Unit tests for SwaggerClient::LoginRequestData
# Automatically generated by swagger-codegen (github.com/swagger-api/swagger-codegen)
# Please update as you see appropriate
describe 'LoginRequestData' do
  before do
    # run before each test
    @instance = SwaggerClient::LoginRequestData.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of LoginRequestData' do
    it 'should create an instance of LoginRequestData' do
      expect(@instance).to be_instance_of(SwaggerClient::LoginRequestData)
    end
  end
  describe 'test attribute "warn_type"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
