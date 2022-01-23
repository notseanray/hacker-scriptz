use std::env;
use evalexpr::*;

fn main() {
    let args: String = env::args().skip(1).collect::<Vec<String>>().join(" ");
    match eval(&args) {
        Ok(v) => println!("{v}"),
        Err(e) => println!("{e}"),
    };
}
