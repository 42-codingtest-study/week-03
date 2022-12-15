// IF문 좀 대신 써 줘 BOJ 19637 송근일 gsong 24살 991206 (곧 생일)
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
// 표준 입력으로 받아도 되고 mac 환경에선 input.txt로 받을 수 도 있게 해주는 코드
solution(input);

function solution(input) {
  let n = input[0].split(" ").map((e) => e * 1)[0]; // n -> 칭호 수
  let m = input[0].split(" ").map((e) => e * 1)[1]; // m -> 유저(대상) 수
  const title_obj = new Object(); // 칭호의 대상 값 지정을 위해 객체 활용
  const answer = [];
  for (let i = 0; i < n; i++) {
    if (!title_obj.hasOwnProperty(input[i + 1].split(" ")[1] * 1))
      // 중복되는 것을 막기 위해 이미 있다면 칭호에 저장 x
      title_obj[input[i + 1].split(" ")[1] * 1] = input[i + 1].split(" ")[0];
  } //{ '10000': 'WEAK', '100000': 'NORMAL', '1000000': 'STRONG' }
  const keyArr = Object.keys(title_obj) // 숫자만 담긴 정렬된 리스트
    .map((e) => e * 1)
    .sort((a, b) => a - b); //[ 10000, 100000, 1000000 ]
  //   console.log(title_obj, keyArr); // { '10000': 'WEAK', '100000': 'NORMAL', '1000000': 'STRONG' } [ 10000, 100000, 1000000 ]
  // 기본 세팅 끝
  for (let j = 0; j < m; j++) {
    let value = input[j + n + 1] * 1;
    let left, right, mid;
    left = 0;
    right = n - 1;
    while (left <= right) {
      mid = parseInt((left + right) / 2);
      value > keyArr[mid] ? (left = mid + 1) : (right = mid - 1);
    } // 각 유저당 해당하는 칭호를 찾기위한 이분탐색
    answer.push(title_obj[keyArr[left]]);
  }
  console.log(answer.join("\n"));
}

// input 예상 출력 값
// WEAK
// WEAK
// WEAK
// NORMAL
// NORMAL
// NORMAL
// STRONG
// STRONG
