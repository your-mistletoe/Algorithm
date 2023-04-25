function solution(n) {
    var arr = [];
    const reversed = n.toString().split('').reverse().join('');
    for (var i of reversed) {
        arr.push(i);
    }
    var rst = arr.map(function(i) {
        return parseInt(i, 10);
    })
    return rst;
}