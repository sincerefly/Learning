function haveBreakfast(food, drink, callback) {
  console.log('Having backhast of ' + food + ', ' + drink);
  if(callback && typeof(callback) === "function") {
    callback();
  }
}

haveBreakfast('toast', 'coffee', function() {
  console.log('Finish breakfast. Time to go to work');
});
