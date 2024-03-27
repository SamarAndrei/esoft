function deepClone(obj) {
    var cloned ={}
    for (i in obj) cloned[i] = typeof obj[i] == 'object' ? deepClone(obj[i]) : obj[i]
    return cloned
}