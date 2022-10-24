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
    describe('LoginAccountInfoUserRoles', function() {
      beforeEach(function() {
        instance = new NetSchool.LoginAccountInfoUserRoles();
      });

      it('should create an instance of LoginAccountInfoUserRoles', function() {
        // TODO: update the code to test LoginAccountInfoUserRoles
        expect(instance).to.be.a(NetSchool.LoginAccountInfoUserRoles);
      });

      it('should have the property userId (base name: "userId")', function() {
        // TODO: update the code to test the property userId
        expect(instance).to.have.property('userId');
        // expect(instance.userId).to.be(expectedValueLiteral);
      });

      it('should have the property schoolId (base name: "schoolId")', function() {
        // TODO: update the code to test the property schoolId
        expect(instance).to.have.property('schoolId');
        // expect(instance.schoolId).to.be(expectedValueLiteral);
      });

      it('should have the property role (base name: "role")', function() {
        // TODO: update the code to test the property role
        expect(instance).to.have.property('role');
        // expect(instance.role).to.be(expectedValueLiteral);
      });

    });
  });

}));
