/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let lastword=s.trim().split(" ")
    
    return lastword[lastword.length-1].length
};