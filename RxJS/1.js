console.clear();

var source = Rx.Observable.create(function (observer) {
  observer.onNext(42);
  observer.onCompleted();
});

var sub = source.subscribe(function(x) {
  console.log('next ' + x);
}, function (err) {
  console.error(err);
}, function () {
  console.info('done');
});
