fn main(){
    let mut greatest = 0;
    // let mut product = 0;
    for i in (100..999).rev(){
        for j in (i..999).rev(){
            let product = i * j;
            if product > greatest{
                if ispal(product){
                    greatest = product;
                }
            }else{
                break;
            }


        }
    }
    println!("Greatest: {}", greatest)

}

fn ispal(x: i32) -> bool{
    let word = x.to_string();
    let binding = word.as_bytes();
    let total = word.len();
    
    for idx in 0..total/2{
        if binding[idx] != binding[total-idx-1]{
            return false
        }
        
    }
    return true
}