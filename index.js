const robot = require('robotjs');

function tag(n) {
  robot.keyTap('@');
  robot.keyTap('enter');

  for (let i = 1; i < n - 1; i++) {
    robot.keyTap('@');
    for (let j = 0; j < i; j++) {
      robot.keyTap('down');
    }
    robot.keyTap('enter');
  }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

console.log('Before sleep');
sleep(5000).then(() => {
  console.log('After sleep');
  tag(7);
});