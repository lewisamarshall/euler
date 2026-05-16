fn main(){
    let pfactors: [u32; 8] = [2, 3, 5, 7, 11, 13, 17, 19];
    let mut factor_number: [u32; 8] = [0, 0, 0, 0, 0, 0, 0, 0];
    for n in 1..=20{
        for (idx, val) in pfactors.iter().enumerate(){
            let mut j = 0;
            let mut m = n;
            while m % val == 0{
                j += 1;
                m = m / val;
            }
            if j > factor_number[idx]{
                factor_number[idx] = j;
            }
        }
    } 
    let mut product = 1;
    for (idx, val) in pfactors.iter().enumerate(){
        product *= (*val).pow(factor_number[idx]);
    }
    println!("{}", product);

}