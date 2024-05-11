fun simplify(input: String): String{
    //"5-x*(3/3)+2"
    var result = ""

    var parentheseList = ArrayList<String>()
    var isOpenParen = false
    var tmp: String = ""
    for (i in input){
        if (i == '(' || isOpenParen) {
            isOpenParen = true
            tmp += i
        }
        if (i == ')')
        {
            isOpenParen = false
            parentheseList.add(tmp)
            tmp = ""
        }
    }
    





    return result
}


fun main(){
    simplify("5-x*(3/3)+2-(5/5)")
}