function solution(num_list) {
    // 값 초기화
    let odd_sum = 0
    let even_sum = 0
    // []의 index 번호가 홀수인 것 추출 -> 모두 더함
    // []의 index 번호가 짝수인 것 추출 -> 모두 더함
    // 더한 값을 odd_sum, even_sum으로 각각 저장
    // 두 수 비교하여 큰 값 return
    for (let i=0; i<num_list.length; i++){
        if(i%2==0){
            even_sum +=  num_list[i]
        }
        else{
            odd_sum += num_list[i]
        }
    }
    if(even_sum>odd_sum){
        return even_sum
    }
    
    else{
        return odd_sum
    }


    var answer = 0;
    return answer;
}