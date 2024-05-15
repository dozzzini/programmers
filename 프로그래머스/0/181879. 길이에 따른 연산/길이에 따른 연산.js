function solution(num_list) {
    let answer = 0;
    let sum =0;
    let mul=1;
    if(num_list.length>=11){
        for(let i = 0; i<num_list.length; i++){
            sum += num_list[i]
        }
        return sum
    }
    else if(num_list.length<=10){
        for(let i=0; i<num_list.length; i++){
            mul = mul * num_list[i]
        }
        return mul
    }
    return answer;
}