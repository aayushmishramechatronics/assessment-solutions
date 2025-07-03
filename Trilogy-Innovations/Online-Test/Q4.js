/**
 * @param {number} a 
 * @param {number} b 
 * @returns {number}
 * @param {string[]} fractions
 * @returns {string[]}
 */
function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function solution(fractions) {
  let res = [];

  for (let expr of fractions) {
    let parts = expr.split('+');
    let frac1 = parts[0].split('/');
    let frac2 = parts[1].split('/');

    let x = parseInt(frac1[0]);
    let y = parseInt(frac1[1]);
    let u = parseInt(frac2[0]);
    let v = parseInt(frac2[1]);

    let num = x * v + u * y;
    let den = y * v;

    let g = gcd(num, den);
    num = num / g;
    den = den / g;
    res.push(num + "/" + den);
  }
  return res;
}
