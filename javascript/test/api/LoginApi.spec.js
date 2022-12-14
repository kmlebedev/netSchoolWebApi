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

  beforeEach(function() {
    instance = new NetSchool.LoginApi();
  });

  describe('(package)', function() {
    describe('LoginApi', function() {
      describe('logindata', function() {
        it('should call logindata successfully', function(done) {
          // TODO: uncomment logindata call and complete the assertions
          /*

          instance.logindata(function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(NetSchool.LoginData);

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('prepareemloginform', function() {
        it('should call prepareemloginform successfully', function(done) {
          // TODO: uncomment, update parameter values for prepareemloginform call and complete the assertions
          /*
          var opts = {};

          instance.prepareemloginform(opts, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(NetSchool.PrepareEmLoginForm);

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('prepareloginform', function() {
        it('should call prepareloginform successfully', function(done) {
          // TODO: uncomment, update parameter values for prepareloginform call and complete the assertions
          /*
          var opts = {};

          instance.prepareloginform(opts, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(NetSchool.PrepareLoginForm);

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
    });
  });

}));
