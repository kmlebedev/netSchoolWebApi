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
    describe('PrepareLoginForm', function() {
      beforeEach(function() {
        instance = new NetSchool.PrepareLoginForm();
      });

      it('should create an instance of PrepareLoginForm', function() {
        // TODO: update the code to test PrepareLoginForm
        expect(instance).to.be.a(NetSchool.PrepareLoginForm);
      });

      it('should have the property countries (base name: "countries")', function() {
        // TODO: update the code to test the property countries
        expect(instance).to.have.property('countries');
        // expect(instance.countries).to.be(expectedValueLiteral);
      });

      it('should have the property states (base name: "states")', function() {
        // TODO: update the code to test the property states
        expect(instance).to.have.property('states');
        // expect(instance.states).to.be(expectedValueLiteral);
      });

      it('should have the property provinces (base name: "provinces")', function() {
        // TODO: update the code to test the property provinces
        expect(instance).to.have.property('provinces');
        // expect(instance.provinces).to.be(expectedValueLiteral);
      });

      it('should have the property cities (base name: "cities")', function() {
        // TODO: update the code to test the property cities
        expect(instance).to.have.property('cities');
        // expect(instance.cities).to.be(expectedValueLiteral);
      });

      it('should have the property funcs (base name: "funcs")', function() {
        // TODO: update the code to test the property funcs
        expect(instance).to.have.property('funcs');
        // expect(instance.funcs).to.be(expectedValueLiteral);
      });

      it('should have the property schools (base name: "schools")', function() {
        // TODO: update the code to test the property schools
        expect(instance).to.have.property('schools');
        // expect(instance.schools).to.be(expectedValueLiteral);
      });

      it('should have the property cid (base name: "cid")', function() {
        // TODO: update the code to test the property cid
        expect(instance).to.have.property('cid');
        // expect(instance.cid).to.be(expectedValueLiteral);
      });

      it('should have the property sid (base name: "sid")', function() {
        // TODO: update the code to test the property sid
        expect(instance).to.have.property('sid');
        // expect(instance.sid).to.be(expectedValueLiteral);
      });

      it('should have the property pid (base name: "pid")', function() {
        // TODO: update the code to test the property pid
        expect(instance).to.have.property('pid');
        // expect(instance.pid).to.be(expectedValueLiteral);
      });

      it('should have the property cn (base name: "cn")', function() {
        // TODO: update the code to test the property cn
        expect(instance).to.have.property('cn');
        // expect(instance.cn).to.be(expectedValueLiteral);
      });

      it('should have the property sft (base name: "sft")', function() {
        // TODO: update the code to test the property sft
        expect(instance).to.have.property('sft');
        // expect(instance.sft).to.be(expectedValueLiteral);
      });

      it('should have the property scid (base name: "scid")', function() {
        // TODO: update the code to test the property scid
        expect(instance).to.have.property('scid');
        // expect(instance.scid).to.be(expectedValueLiteral);
      });

      it('should have the property hlevels (base name: "hlevels")', function() {
        // TODO: update the code to test the property hlevels
        expect(instance).to.have.property('hlevels');
        // expect(instance.hlevels).to.be(expectedValueLiteral);
      });

      it('should have the property ems (base name: "ems")', function() {
        // TODO: update the code to test the property ems
        expect(instance).to.have.property('ems');
        // expect(instance.ems).to.be(expectedValueLiteral);
      });

    });
  });

}));
