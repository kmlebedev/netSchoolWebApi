/*
 * NetSchool
 * The API for the NetSchool irTech project
 *
 * OpenAPI spec version: 4.30.43656
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
    describe('LoginData', function() {
      beforeEach(function() {
        instance = new NetSchool.LoginData();
      });

      it('should create an instance of LoginData', function() {
        // TODO: update the code to test LoginData
        expect(instance).to.be.a(NetSchool.LoginData);
      });

      it('should have the property productName (base name: "productName")', function() {
        // TODO: update the code to test the property productName
        expect(instance).to.have.property('productName');
        // expect(instance.productName).to.be(expectedValueLiteral);
      });

      it('should have the property version (base name: "version")', function() {
        // TODO: update the code to test the property version
        expect(instance).to.have.property('version');
        // expect(instance.version).to.be(expectedValueLiteral);
      });

      it('should have the property esiaLoginPage (base name: "esiaLoginPage")', function() {
        // TODO: update the code to test the property esiaLoginPage
        expect(instance).to.have.property('esiaLoginPage');
        // expect(instance.esiaLoginPage).to.be(expectedValueLiteral);
      });

      it('should have the property cacheVer (base name: "cacheVer")', function() {
        // TODO: update the code to test the property cacheVer
        expect(instance).to.have.property('cacheVer');
        // expect(instance.cacheVer).to.be(expectedValueLiteral);
      });

      it('should have the property schoolLogin (base name: "schoolLogin")', function() {
        // TODO: update the code to test the property schoolLogin
        expect(instance).to.have.property('schoolLogin');
        // expect(instance.schoolLogin).to.be(expectedValueLiteral);
      });

      it('should have the property emLogin (base name: "emLogin")', function() {
        // TODO: update the code to test the property emLogin
        expect(instance).to.have.property('emLogin');
        // expect(instance.emLogin).to.be(expectedValueLiteral);
      });

      it('should have the property windowsAuth (base name: "windowsAuth")', function() {
        // TODO: update the code to test the property windowsAuth
        expect(instance).to.have.property('windowsAuth');
        // expect(instance.windowsAuth).to.be(expectedValueLiteral);
      });

      it('should have the property enableSms (base name: "enableSms")', function() {
        // TODO: update the code to test the property enableSms
        expect(instance).to.have.property('enableSms');
        // expect(instance.enableSms).to.be(expectedValueLiteral);
      });

      it('should have the property esiaMainAuth (base name: "esiaMainAuth")', function() {
        // TODO: update the code to test the property esiaMainAuth
        expect(instance).to.have.property('esiaMainAuth');
        // expect(instance.esiaMainAuth).to.be(expectedValueLiteral);
      });

      it('should have the property esiaButton (base name: "esiaButton")', function() {
        // TODO: update the code to test the property esiaButton
        expect(instance).to.have.property('esiaButton');
        // expect(instance.esiaButton).to.be(expectedValueLiteral);
      });

      it('should have the property signatureLogin (base name: "signatureLogin")', function() {
        // TODO: update the code to test the property signatureLogin
        expect(instance).to.have.property('signatureLogin');
        // expect(instance.signatureLogin).to.be(expectedValueLiteral);
      });

    });
  });

}));
