function solution(hp) {
    var answer = 0;
    
    const first = Math.floor(hp/5)
    const second = Math.floor((hp-(5 * first)) / 3)
    const third = Math.floor(hp-(5*first + 3*second)/1)
    
    answer = first + second + third
    
    return answer;
}