/*
 * NetSchool
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 5.10.63221
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.35
 *
 * Do not edit the class manually.
 *
 */
(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.NetSchool);
  }
}(this, function(expect, NetSchool) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('Login', function() {
      beforeEach(function() {
        instance = new NetSchool.Login();
      });

      it('should create an instance of Login', function() {
        // TODO: update the code to test Login
        expect(instance).to.be.a(NetSchool.Login);
      });

      it('should have the property at (base name: "at")', function() {
        // TODO: update the code to test the property at
        expect(instance).to.have.property('at');
        // expect(instance.at).to.be(expectedValueLiteral);
      });

      it('should have the property code (base name: "code")', function() {
        // TODO: update the code to test the property code
        expect(instance).to.have.property('code');
        // expect(instance.code).to.be(expectedValueLiteral);
      });

      it('should have the property timeOut (base name: "timeOut")', function() {
        // TODO: update the code to test the property timeOut
        expect(instance).to.have.property('timeOut');
        // expect(instance.timeOut).to.be(expectedValueLiteral);
      });

      it('should have the property accessToken (base name: "accessToken")', function() {
        // TODO: update the code to test the property accessToken
        expect(instance).to.have.property('accessToken');
        // expect(instance.accessToken).to.be(expectedValueLiteral);
      });

      it('should have the property refreshToken (base name: "refreshToken")', function() {
        // TODO: update the code to test the property refreshToken
        expect(instance).to.have.property('refreshToken');
        // expect(instance.refreshToken).to.be(expectedValueLiteral);
      });

      it('should have the property accountInfo (base name: "accountInfo")', function() {
        // TODO: update the code to test the property accountInfo
        expect(instance).to.have.property('accountInfo');
        // expect(instance.accountInfo).to.be(expectedValueLiteral);
      });

      it('should have the property tokenType (base name: "tokenType")', function() {
        // TODO: update the code to test the property tokenType
        expect(instance).to.have.property('tokenType');
        // expect(instance.tokenType).to.be(expectedValueLiteral);
      });

      it('should have the property entryPoint (base name: "entryPoint")', function() {
        // TODO: update the code to test the property entryPoint
        expect(instance).to.have.property('entryPoint');
        // expect(instance.entryPoint).to.be(expectedValueLiteral);
      });

      it('should have the property requestData (base name: "requestData")', function() {
        // TODO: update the code to test the property requestData
        expect(instance).to.have.property('requestData');
        // expect(instance.requestData).to.be(expectedValueLiteral);
      });

      it('should have the property errorMessage (base name: "errorMessage")', function() {
        // TODO: update the code to test the property errorMessage
        expect(instance).to.have.property('errorMessage');
        // expect(instance.errorMessage).to.be(expectedValueLiteral);
      });

    });
  });

}));
