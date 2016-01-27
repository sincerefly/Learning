// Logic (functional)
function main() {
  return Rx.Observable.timer(0, 1000)
  .map( i => `seconds elapsed ${i}`);
}

// Effects (imperative)
function DOMEffect(text$) {
  text$.subscribe(text => {
    const container = document.querySelector('#app');
    container.textContent = text;
  });
}

function consoleLogEffect(msg$) {
  msg$.subscribe(msg => console.log(msg));
}

const sink = main();
DOMEffect(sink);
consoleLogEffect(sink);


