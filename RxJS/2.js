console.clear();

var source = [1, 2, 3, 4, 5];

//var source = Rx.Observable.fromArray([0, 1, 2, 3, 4, 5]);

//var source = Rx.Observable.interval(500).take(10);

source.filter(x => x % 2 === 1)
  .map(x => x + '!')
  .forEach(x => console.log(x));

