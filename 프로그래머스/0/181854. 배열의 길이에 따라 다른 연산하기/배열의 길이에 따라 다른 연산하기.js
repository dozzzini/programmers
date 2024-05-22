function solution(arr, n) {
    var answer = [];
    const length = arr.length
    
    if(length % 2 == 1){
        for(let i=0; i<length; i+= 2){
           arr[i] += n
        }
    }
    else{
        for(let i =1; i<length; i +=2 ){
            arr[i] += n
        }
    }
   
    return arr;
}