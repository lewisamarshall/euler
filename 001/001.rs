fn main(){
    let mut total = 0;

    for i in 1..1000{
        if i%3==0{
            total += i;
        } else if i % 5 == 0{
            total += i;
        }
    }
    
    println!("total is {}", total);
}