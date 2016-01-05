var fibonacci = function (n) {

  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  if (n < 0) {
    throw new Error("n should >= 0");
  }
  if (n > 10) {
    throw new Error("n should <= 10");
  }
  if (typeof n !== 'number') {
    throw new Error("n should be a number");
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

if (require.main === module) {
  var n = Number(process.argv[2]);
  console.log("fibonacci(" + n + ") is", fibonacci(n));
}

exports.fibonacci = fibonacci;




