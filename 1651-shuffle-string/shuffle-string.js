/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    const shuffled = Array(s.length);
    [...s].forEach((char, i) => {
        shuffled[indices[i]] = char;
    });
    return shuffled.join('');
};