// file: test/index.test.js
var index = require("../index");
var should = require("should");

describe("test/index.test.js", function () {

  it("should equal 0 when n === 0", function () {
    index.fibonacci(0).should.equal(0);
  })

  it("should equal 1 when n === 1", function () {
    index.fibonacci(1).should.equal(1);
  })

  it("should equal 55 when n === 10", function () {
    index.fibonacci(10).should.equal(55);
  });

  it("should throw when n > 10", function () {
    (function () {
      index.fibonacci(11);
    }).should.throw("n should <= 10");
  });

  it("should throw when n < 0", function () {
    (function () {
      index.fibonacci(-1);
    }).should.throw("n should >= 0");
  });

  it("should throw when n isnt Number", function () {
    (function () {
      index.fibonacci("hehe");
    }).should.throw("n should be a number");
  });

});
