function solution(n) {
    let sum = 0;
    
    if (n % 2 === 1) { // n이 홀수인 경우
        for (let i = 1; i <= n; i += 2) {
            sum += i;
        }
    } else { // n이 짝수인 경우
        for (let i = 2; i <= n; i += 2) {
            sum += i * i;
        }
    }
    
    return sum;
}