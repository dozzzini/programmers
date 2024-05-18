function doesNotIncludeAd(str){
    return !str.includes("ad")
}

function solution(strArr) {
    return strArr.filter(doesNotIncludeAd)
}