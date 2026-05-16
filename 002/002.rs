fn main(){
    let mut a = 1;
    let mut b = 2;
    let mut total = 0;

    while b < 4000000{
        if b % 2 == 0{
            total += b;
        }
        (a, b) = (b, a+b)
    }
    println!("Total is {}.", total)
}