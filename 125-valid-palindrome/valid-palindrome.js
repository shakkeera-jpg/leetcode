/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let cleanstr=s.replace(/[^a-zA-Z0-9]/g,"").toLowerCase()
    let reversed=cleanstr.split("").reverse().join("")
    if(reversed===cleanstr){
        return true
    }
    return false
};